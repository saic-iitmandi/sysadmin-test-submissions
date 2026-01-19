# SAIC SysAdminTest'23

## Challenge 3 - Docker Deployments

Here we are given two websites and we need to deploy them using docker containers.
We also need to Backup a volume mapped data as a zip file every day at 11:55 pm.
At first, let's go through each website one by one.

### [SAIC-website](https://github.com/KamandPrompt/SAIC-Website)

After opening the github page, we can see that it is a basic HTML-CSS-JS-based website which was also mentioned in the task.
I took some help from this video from **freecodecamp** (<https://youtu.be/Wf2eSG3owoA?si=HStbjamGQYug83Fi>).
For hosting this I used the `nginx:latest` as the base image to build.
Then I created a *Dockerfile* with the following contents :---[DockerFile1](Dockerfile1)

~~~Dockerfile
FROM nginx:latest
ADD . /usr/share/nginx/html
~~~

I built an image named website using `docker build --tag website:latest` .
Finally, I ran the image to host the website using `docker run --name SAIC -d -p 9000:80 website:latest .`

### [Github Languages](https://github.com/alex-benoit/github-languages.git)

This website is based on Ruby on Rails.
So I need to build an image using `ruby` as the base image. I googled how to do it and went through a lot of articles and websites.
Then taking information from this: (<https://earthly.dev/blog/rails-with-docker/>) I tried to build an image based on  `ruby:alpine`.

I used the below as the initial Dockerfile:

~~~Dockerfile
FROM ruby:alpine3.19
  RUN apk add \
    build-base \
    postgresql-dev \
    tzdata \
    nodejs
  
  WORKDIR /app
  COPY Gemfile* .
  RUN bundle install
  COPY . .
  EXPOSE 3000
  CMD ["rails", "server", "-b", "0.0.0.0"]
~~~

After running `docker build --tag webs:latest` it threw errors. Basically because of the version dependencies. I made some changes to make the above code run. All efforts were in vain[Error](Screenshots/error.png). After more of googling, I found this: (<https://github.com/shettigarc/rails-on-docker>).

There I found a YouTube link: (<https://youtu.be/a-jcTib9ZPA>) which helped me to create a new Dockerfile. I also made a docker-compose file and made changes to database.yml as needed. But it also failed. Then I noticed the database used here is **PostgreSQL**. Then I went to find this video: (https://youtu.be/dF6VQOZPZBM?si=d1k8iirTlrCiziMw).  But still failed. :(

### PART 2

So here we need to back up a volume mapped data as a zip file to a folder of my choice every day at 11:55 pm. For this I visited a few sites like : (https://docs.docker.com/storage/volumes/#back-up-restore-or-migrate-data-volumes),  (https://stackoverflow.com/questions/26331651/how-can-i-backup-a-docker-container-with-its-data-volumes),  (https://www.docker.com/blog/back-up-and-share-docker-volumes-with-this-extension/). The [backup script](backup.sh) kind of should look like below:

~~~bash
#!/bin/bash
source="pathtothevolumedata"
location="pathtobackuplocation"
cd "$source"
zip -r "$location/backup.zip"
~~~

*source* mentioned above is generally /var/lib/docker/volume on **Linux** but you can get the location by `docker inspect name_of_container` and then under **"Mounts"** section, you can see written as **"Source:"**. 

For the timer part, we can create a cron job in [another script](start.sh) so that when the script runs it will execute the backup script
at 11:55 pm. 

~~~bash
#!/bin/bash
#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "55 23 * * * cd locationtothebackupscript; ./backup.sh" >> mycron
#install new cron file
crontab mycron
rm mycron
~~~

Help : (https://stackoverflow.com/questions/878600/how-to-create-a-cron-job-using-bash-automatically-without-the-interactive-editor)

I hope it runs  :sweat_smile:  :sweat_smile:  :sweat_smile:

### PART3

The network type for [SAIC-website](https://github.com/KamandPrompt/SAIC-Website) will be a bridge network. I guess it is because it has a default and easy setup. The bridge network allows you to map container ports to host ports. 
