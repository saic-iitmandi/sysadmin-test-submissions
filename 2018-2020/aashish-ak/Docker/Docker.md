# sysadmin-test Docker

In order to create a docker image, after installing docker i googled about it a bit to know more what is docker and came through this [article](https://docker-curriculum.com/), which is all i needed, it includes a full detailed and well documented tutorial on what is docker and how it operates, so i first created an account on [Docker Hub](https://hub.docker.com) and created an online public [repository](https://hub.docker.com/r/ashish118/hello-sahil/) and then i created a Dockerfile in local repository with the following code:
```txt
FROM alpine
ADD testfile.sh /
CMD ["/testfile.sh"]
```
where `testfile.sh` is the bash script which contains the following code specified in Docker.md in syadmin-test repository:
```txt
#!/bin/sh
echo "My name is Sahil Arora, and my container works!"
```
and in the `Dockerfile` the `FROM alpine` specifies the base image for the Docker Image then after creating the Dockerfile, i built the Docker Image with the following command:
```bash
sudo docker build .
```
and the `Dockerfile` and `testfile.sh` script were in the same directory, then i set the tag of this image in the local repository as `ashish118/hello-sahil` which is the name of my online repository by the following command:
```bash
sudo docker tag f287dfca35d5 ashish118/hello-sahil
```
and then i logged in and pushed my docker image from local repository to my online repository by runnning the following command:
```bash
sudo docker push ashish118/hello-sahil
```
and now anyone can run my docker image from any system by running the following command:
```bash
sudo docker run ashish118/hello-sahil
```
I also took help from this [video tutorial](https://youtu.be/hnxI-K10auY) and [stackoverflow](https://www.stackoverflow.com) was always helpful. It was a great experience learning docker and learning that how it can be really useful in many ways.

---------
By: Aashish Kumar (B16001)
GitHub: [aashish-ak](https://github.com/aashish-ak/)
---------
