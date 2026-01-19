# How i did - 
1. I made an account on docker hub and made a repo 'lakshay123/sysadmin-test'.
2. Made a file 'testfile'.sh with following content - 
		#!/bin/sh
		echo "My name is Lakshay Arora, and my container works!"
3. Made this file executable using chmod command.
4. Made a Dockerfile with following content -
		FROM ubuntu
		COPY ./testfile.sh ~/
		CMD ["~/testfile.sh"]
   It downloads the ubuntu base image, copies the file ./testfile.sh to the home directory.
   CMD command is used to provide defaults for an executing container(which are set in many cases using a shell script) and diplays the result of the executable provided as argument on the terminal.
5. Build the docker image using 'docker build -t sysadmin-test'.
6. Tag the image using 'docker tag sysadmin-test:latest lakshay123/sysadmin-test:sysadmin-test'.
7. Push the image on docker hub using 'docker push lakshay123/sysadmin-test:sysadmin-test'.

# Resources:
1. https://docs.docker.com/engine/reference/builder/#usage
2. https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html
3. https://www.youtube.com/watch?v=YFl2mCHdv24&t=480s

## Link to the image 
https://hub.docker.com/r/lakshay123/sysadmin-test/

# What I learnt-

### 1. What is Docker 
	Docker is a tool for running applications in an isolated environment which give us advantages similar to running our application inside a virtual machine but with less overhead. 
	1.1 A big advantage is that the app always runs in exactly the same environment so there are no inconsistencies in how it behaves on different machines.
	1.2  It makes it easier to set up and work with somebody else's projects, we don't have to install all of the tools and dependencies that the project needs, we just run the virtual machine and we are done.

### 2. Virtual Machines vs. Docker
	Instead of running and managing a virtual machine, we have containers, the code and the environment are all wrapped up inside a container, but a container is not a full virtual machine. When we run a virtual machine, it gets its own full operating system, which is quite an overhead. Docker creates isolated environments and can start up in seconds, they use fewer resources and take up less disk space and using less memory.

### 3. Containers
	A container is a running instance of an image. An image is a template for creating the environment, it's a snapshot of the system at a particular instant. So it has the application, libraries and dependencies all bundled up in a file.

### 4. Dockerfile
	We can run docker images using command line like 'docker rune ubuntu /bin/bash'. But if we want to run multiple docker commands to build our image, we can use a docker file with the build feature to build our image.

### 5. Build Context
	The build context is the set of files at a specified location PATH or URL. The PATH is a directory on your local filesystem. The URL is a Git repository location.
	A context is processed recursively. So, a PATH includes any subdirectories and the URL includes the repository and its submodules.
### 6. Building an image
	To build an image, we use docker build command.
	It transfers the contents of the build context to docker daemon.
	We can use images from other applications/projects which would make something called a layer of images, the size of the image after the build is the total size of all the images used.
### 7. Tagging and pushing the image on docker hub.
	We can tag an image, which can be helpful to distinguish between versions or other images. To tag we can simply use the -t parameter with docker build or use docker tag command seperately.