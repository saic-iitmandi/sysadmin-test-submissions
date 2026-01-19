I started reading the docker documentaton(https://docs.docker.com/get-started/), learned about image and containers.I installed docker on my laptop, and basically followed the docs till end of part 2.
I learned bash can be  used to run .sh files.The documentation had an example dockerfile to run a .py file with python, i used the same structure to run a .sh file in the working directory.
In the Dockerfile, I used "WORKDIR /home" to make a directory in the container and used "ADD . /home" to add the test.sh file to the working directory.
Then used "CMD ["bash","test.sh"]" to run test.sh and display its content.Then built an image with "sudo docker build -t adityatest .", and ran it using "sudo docker run aditya-test".
Tagged it using "sudo docker tag adityatest adityas1297/systest1" and finally pushed it to https://cloud.docker.com ("sudo docker push adityas1297/systest1
")

"sudo docker run adityas1297/systest1" where adityas1297/systest1 is the IMAGE_NAME in the problem, should run give you the the desired output.
Link to dockerhub - https://hub.docker.com/r/adityas1297/systest1/tags/

To sum up-
1. Read the first two pages of docker documetation.
2. Installed Docker.
3. Created Dockerfile and test.sh
4. Built the image and tested it.
5. Push it to cloud.docker.com


What did I learn - 
1. Difference between containers and Virtual machines.
2. Docker commands like RUN, CMD, EXPOSE, WORKDIR.
3. How a small container can be used for developing an app.

Resources - 
1. https://docs.docker.com/get-started/
2. https://docs.docker.com/get-started/part2/
3. https://deis.com/blog/2015/dockerfile-instructions-syntax/
4. https://deis.com/blog/2015/creating-sharing-first-docker-image/
5. https://stackoverflow.com/questions/16047306/how-is-docker-different-from-a-normal-virtual-machine?rq=1\
6. https://docs.docker.com/install/linux/docker-ce/ubuntu/
