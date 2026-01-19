# Docker

## Solutions

#### Problem Statement-

Upload an ubuntu docker image to docker store with your username. This image should contain a file in the /home directory with the name testfile.sh and the following contents:
```
#!/bin/sh
echo "My name is Sahil Arora, and my container works!"
```
Replace Sahil Arora with your name.

#### Solution

`Dockerimage` File has name of the image which does the above task.

This task introduced me to the usage of Docker and its utility and importance as well as to concepts of containers. 
Followed the instructions [here](https://docs.docker.com/install/) to install `Docker CE` version on my PC locally. Followed the guide [here](https://docs.docker.com/get-started/part1/) to get started with `Docker` and also read the basic concepts of Docker and containerization. A guide at [FreeCodeCamp](https://medium.freecodecamp.org/docker-easy-as-build-run-done-e174cc452599) and the one at [Docker Docs](https://docs.docker.com/get-started/part2/) helped me complete the above task.<br>

To complete the task created a script that that `echo` the needed statement, and in the docker file used `CMD bash testfile.sh` to run it in the terminal of the user. Also the file was moved to the `/home` directory of the container using `ADD . /home`. The docker image was created using `docker build -t friendlyhello .`, from the `CWD`, where `friendlyhello` is the docker image name. The image was tagged to `abhigyank/friendlyhello` to be pushed into [Docker store](https://store.docker.com/community/images/abhigyank/friendlyhello).   

