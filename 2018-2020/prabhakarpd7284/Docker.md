# Docker
I had come across the term 'Docker' a few days before seeing this task while randomly browsing github pages. I visited https://docker-curriculum.com/ and came to know about Docker and its applications. After following this tutorial, I read the task again and I knew it has to do something with bash script. So, I googled it and found following useful pages:-

For Installation - https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce (Install using the repository)<br>
https://docs.sevenbridges.com/docs/upload-your-docker-image-1<br>
https://docs.sevenbridges.com/docs/upload-your-docker-image-with-a-dockerfile<br>
http://kimh.github.io/blog/en/docker/gotchas-in-writing-dockerfile-en/

My Dockerfile contains :-

>`FROM ubuntu`<br>
`ADD ./testfile.sh /home/testfile.sh`<br>
`CMD ["bash", "/home/testfile.sh"]`<br>

After creating a folder containing **Dockerfile** and **testfile.sh**, I ran following commands :-<br>
>`docker build -t prabhakarpd7284/testhello`<br>
`docker run --name testhello prabhakarpd7284/testhello`<br>
`docker push prabhakarpd7284/testhello`<br>

Link to the image - https://hub.docker.com/r/prabhakarpd7284/testhello/<br> 
For Terminal -  `$docker run prabhakarpd7284/testhello`.