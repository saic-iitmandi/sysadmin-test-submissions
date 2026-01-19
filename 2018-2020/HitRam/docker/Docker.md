## Docker 

In this assignment, I learnt about [Docker](https://www.docker.com) which is a containerization technology. The task given was to upload a docker image on [Docker hub](https://hub.docker.com) which on running would echo a message on terminal.

### Setting up docker on Mac

This task was very easy. I followed [Docker docs](https://docs.docker.com/docker-for-mac/) and installed docker on my machine. Just download the dmg file from the link above and install. Create an account on https://hub.docker.com. Now login into docker by using `docker login` command and you are good to go!

### Hello-world

Most of us start learning programming by **Hello-world** program. I started docker with this.

``` 
docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
ca4f61b1923c: Pull complete 
Digest: sha256:66ef312bbac49c39a89aa9bcc3cb4f3c9e7de3788c944158df3ee0176d32b751
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

Then seeing this, I ran `docker run -it ubuntu bash` and saw an ubuntu terminal started within minutes! 

### Terminology 

I got familiar with basic docker commands and few terms like Containers, Images, Docker daemon, Docker client and Docker hub.

### Building a docker image and pushing on Docker hub

I created a `Dockerfile` with the following content

```
# set base image name
FROM ubuntu

# Dockerfile author/maintainer
MAINTAINER Hitesh <hitr9831@gmail.com>

# Copy testfile.sh into home directory
COPY testfile.sh home/

# Run this command when container is running
CMD ["sh", "home/testfile.sh"]

```
The comments pretty much explains everything. 
To build this into an image, run the following command. 
```
docker build -t hiteshr/test_image:firsttry
```
Where test_image is the folder in which `Dockerfile` and `testfile.sh` is present and firsttry is the `tag`.

Now the image is built and you can run using `docker run hiteshr/test_image`.

But for others to access this image, we need to push this image on Docker store which is like github for docker images. 

```
docker push hiteshr/test_image
```

This command will push the image. 
Now anyone can run the image using the command `docker run hiteshr/test_image`

### Resources for learning docker

* https://github.com/docker/labs/tree/master/beginner
* https://www.youtube.com/watch?v=pGYAg7TMmp0&index=1&list=PLoYCgNOIyGAAzevEST2qm2Xbe3aeLFvLc
