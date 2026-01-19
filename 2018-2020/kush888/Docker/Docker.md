## Docker Assignment 

This assignment was pretty cool and it helped me gain lots of knowledge, few being listed below :
1. What is docker.
2. How to setup docker on linux machine.
3. Basic commands of docker.
4. Running an image from docker cloud which includes running entire different OS on our system. 
4. Docker v/s virtual machines.
5. And much more :D 

### Basic Commands 
```
docker login    - to login into your account 
docker build    - to build new image 
docker ps       - to get the information of running containers 
docker ps -a    - to get the information of all the containers
docker stop     - to stop a running container
docker rm       - to delete a container 
docker run      - to run an image
```

### Installing docker on linux system. 
1. Make an account on docker.com. 
2. Follow the instructions given at https://docs.docker.com/install/linux/docker-ee/ubuntu/ to install docker on your linux machine.



### Steps used for creation of new Ubuntu Image File :
1.  Make a new folder named Docker on Desktop.
2.  Create a file inside this folder named Dockerfile. 
3.  Put the following commands inside this file:
```
    FROM ubuntu
    COPY testfile.sh /home/testfile.sh
    CMD ["/home/testfile.sh"]
```
4. In this, first lines specifies the base image we want to use. 
Second line is used to copy the contents of testfile.sh to a new file named testfile.sh present in home directory.
Third line makes sure that the testfile script runs on running the image file. 
4.  After making the Dockerfile we need to make a script to echo the desired content on the terminal. So we make another file named testfile.sh and put these commands into it :
```
	#!/bin/sh
	echo "My name is Kushagra Singhal, and my container works!"
```
5. Then make this script executable using the command:
```
chmod +x testfile.sh
```
6. to build the image, type following command on your terminal:
```
    docker build .
```
7. to run the image type following command: 
```
    docker run --name testimage $imageid
```

8. Now our image is build and we just need to upload it to docker cloud. To do so type in following command: 
```
docker push kushagra8/testimage
```
9. Voila!! My first ubuntu image is up and running. 
```
docker run kushagra8/testimage 
```



### References 

* https://www.youtube.com/watch?v=JBtWxj9l7zM&t=312s
* https://www.youtube.com/watch?v=hnxI-K10auY&t=648s
* https://docs.docker.com/engine/reference/builder/

### Docker Hub Link 
https://cloud.docker.com/swarm/kushagra8/dashboard/onboarding/cloud-registry