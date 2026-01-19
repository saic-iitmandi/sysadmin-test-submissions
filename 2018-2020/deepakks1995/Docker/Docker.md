Image had been uploaded to docker hub.

It has been assumed that docker-ce is already installed in the system else refer the documentaion for docker.


Following are the steps used to create the Docker Image

1.	First create a folder named 'falcon' which will be containing all of our work

2.	Then create a file named 'testfile.sh' and type the following contents in the file

	'
	#!/bin/sh

	echo "My name is Deepak Sharma, and my container works!"'

3.	Now we are about to create Dockerfile with the following contents

	'
	FROM ubuntu:latest

	RUN apt-get update
	
	COPY testfile.sh /home/testfile.sh
	
	CMD ["./home/testfile.sh"]
	'

4.	Now build the image using the command below
	'
	$ sudo docker build -t IMAGE_ID .
	'

5. Now push the image to docker hub by first login in the docker hub and then pushing the image to the hub.
	
#Note: 
 IMAGE_ID can be known from the command 
	
	'
	$ sudo docker images -a
	'

6.	To Pull the image from docker hub 
	'
	$docker pull deepakks1995/falcon
	'