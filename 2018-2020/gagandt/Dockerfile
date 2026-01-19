FROM ubuntu

MAINTAINER GaganDT gagandeep280597@gmail.com

WORKDIR ./home/

RUN touch testfile.sh

RUN echo "#!/bin/sh" >> testfile.sh
RUN echo "echo 'My name is GaganDeep Tomar, and my container works!'" >> testfile.sh
RUN chmod +x testfile.sh

RUN ./testfile.sh
