downloaded repostries of both websites

created dockerfiles for both websites using scripts attacked along with it

ran "sudo docker build -t saic_website ." for creating docker image for saic website

ran "sudo docker build -t github_website ." for creating docker image for github languages website

created docker compose .yaml file which is attached along with it to create two containers for three containers one for saic website and one for postgresql database and one for website which depends upon postgresql container

ran "sudo docker-compose up -d" to run containers on a single network in background

# LEARNING OUTCOMES:
-learnt about docker containers <br>
-creating a docker image <br>
-got to know about docker compose and how to write scripts for creating docker containers<br> 
-setting up a database container with already available images <br>
-mapping of postgresql data to a directory in localhost from container<br>

 
