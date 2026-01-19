# Docker

Docker is used to creat a conatiner that contains only the elements required to run our specific applications so that there is no 
interruption from any other process or application.

## The Dockerfile

The Dockerfile contains all the instructions for creating the docker image. 
We define the files that need to be run on running the image, environment variables, setting up the workdirectory etc.

This dockerfile is used when we build the docker image

So I setup the the Dockerfile to run `testfile.sh` on launch of my container.

## Building and pushing the docker image

```bash
sudo docker build -t image-name

sudo docker tag image-name username/repository:tag

sudo docker push username/repository:tag
```

We can run this image from any other system having docker.io installed using :

```bash
sudo docker run -p 4000:80 ashking13th/uno:p2
```

## Learning resources
1. https://docs.docker.com/get-started/
2. https://docs.docker.com/get-started/part2/
