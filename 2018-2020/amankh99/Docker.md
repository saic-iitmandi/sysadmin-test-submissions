Firstly I'am listing the **resources I took help from** - wikipedia.com, techtarget.com, stackoverflow.com and extensively used documentation provided by docker.

**Learning** - 

1.What is containersation?

2.What is virtual machine?

3.How the containersation different from vm's?

4.Advantages and disadvantages of containersation?

5.What is docker image, container and how to work with docker?

This was the first time I solely used application via documentation - so it taught me how to read and apply the things in documentaion

**Final working link**-
https://hub.docker.com/r/amankh99/testfi/

**How to?**

Firstly I made the directory say _demo_ in that directory I created the file named _Dockerfile_ and made another directory in demo named _home_
and in that directory I created the file named _testfile.sh_ and put the following content in it-

#!/bin/sh

echo "My name is Aman Khandelwal, and my container works!"

In _Dockerfile_ we have to put the code which consists of essential commands, environment which is needed for our application to run.
I put the following code in it-

FROM ubuntu

MAINTAINER Aman Khandelwal

COPY home /home

CMD /home/testfile.sh

The first line signifies the the environment we want to work in - ubuntu, this pulls the by default the latest version image of ubuntu because we have not specified the
version.

Second line is not necessary, it tells contact information of the maintainer of the image.

Third line- you may refer to documentation of docker, it copies the file(_testfile.sh_) from source(_home_) and paste the file in destination(_home_) directory.

Fourth line executes the command - _/home/testfile.sh_ on terminal and our message in the file appears.
