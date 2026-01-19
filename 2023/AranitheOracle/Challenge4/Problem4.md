# SAIC SysAdminTest'23

## Challenge 4 - Docker & Networking

Here we are tasked to pull an image from [**Docker Hub**](https://hub.docker.com/search?q=). Then we need to balance the load between multiple instances of the same image.


#### PART-1

For the first part, code is fundamental. Just some known Docker commands like `pull` and `run` are used as you can see below.
For this, I used [this image (lightweight)](https://hub.docker.com/r/metavinayak/matrix) .
~~~bash
#!/bin/bash
img_id="d8e1f39c17d0"
echo "Let's pull the image first"
sleep 1
docker pull metavinayak/matrix
sleep 3
echo "Enter the number of instances of the image you want to create : "
read num
for ((i=1; i<=$num; i++)); do
    docker run -d --name instance${i} -p 808$i:3000 $img_id
done
~~~
The [demonstration](Screenshots/part1demonstration.png) and the [script](part1initial.sh) are attached.

#### PART-2

For the load-balancing purpose, I used **_nginx_**. For this the help I took is listed below:-
>1. https://youtu.be/v81CzSeiQjo?si=gy-ty-7VM-Mn3v2B
>2. https://youtu.be/42Q65H8ch7U?si=lmhVZyvzCanlqDNP
>3. https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/

After all the efforts and pain I was able to set up a _sasta_ load balancer. I created a Dockerfile and docker-compose file with all the required stuff. Then nginx.conf was the last step left for this. All the files required are attached : [Dockerfile](Dockerfile) , [docker-compose.yml](docker-compose.yml), [nginx.conf](nginx.conf). The directory structure must look like this: [Directory Structure](Screenshots/folders.png). Then `docker-compose up --build -d` to build the instances and test the load-balancing. The load balancer is a complete mess and is not optimized  :sweat_smile:  .

The [demonstration](Screenshots/Loadbalancingdemonstration.mp4) of the load-balancer is attached. For this, I used [this image (lightweight)](https://hub.docker.com/r/metavinayak/matrix) .

#### PART-3

For this, I was thinking of creating an architecture in which each instance will have its own access.log and error.log. In this way, we will have isolated logs so that it's easier to identify any kind of issue.Also better organization is a plus point. The default ones are usually simpler and face difficulty in multiple instances.
