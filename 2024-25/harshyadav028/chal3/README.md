## **Challenge 3 - Docker Deployments**
## Best network to use
I find Docker network type *BRIDGE* as the optimal and best network type for the Ruby on Rails project and also for the Next.js project among all other network types.
I choose bridge because the bridge network type is beneficial in  applications in which there is a need for communication among the containers. In technical terms, bridge provides the container-level isolation which we need in the 
1.  __Ruby on Rails project__ -> this project has package.json and db also linked with it so there is very much need of communication in the container which is easily possible with the bridge network. Also, it has gemfile and gem file.lock files which have the versions of all the dependencies used in the project which is very essential to be coordinated within the container.
2. __NextJS Project__ -> this project obviously has many dependencies in  files(e.g.: *package.json, package-lock.json,tsonfig.json etc.*) which need to be communicated as npm install will install all packages mentioned in package.json and create a node_modules directory which is the core of a Next.js application.

## Brief Document
### Ruby on Rails project 
I have tried the 2023 sys admin test so have a prior idea of deploying the Ruby on Rails project :
1. I cloned the GitHub repo Nutrient-Tracker and then started making a Dockerfile in the root directory. 
2. Docker file -> a Docker file defines the environment setup needed for the Ruby on Rails project.
3.  I started with using official Ruby images available  on Docker Hub version 2.7 as the repo uses Rails version 5.1.4 (got from the gem file) to settle the compatibility of Rails.
4. I wrote the code for installing dependencies like(project dependencies in the gem file, sqlite3 for db used in the project)
5. Then I completed the Dockerfile with setting up a working directory in the container and copying all files into the container.
6. You can learn more by reading the comments ahead of the code
7. Then creating a docker-compose.yml step came as which is essential as Docker-compose.yml -> this file arranges the services for the project in the container.
8. Created a service named nutrient-tracker and set up the build as dockerfile as it contains all the environment setup stuff.
9. Coded port as "3000:3000" (Map port 3000 of the container to port 3000 on the host machine).
10. Created a volume to mount the files within the container.
11. At last set up the network as bridge network justified reason above :)
12. This concludes our docker environment  setup and we are ready to build the image of the directory. 
## Error: 
1. Ruby image version used does not support the bundler version so have to adjust the bundler version to 1.16.0 which is also prescribed in the gem file.

 ### NextJS project

1. It is easy for me as I have learned NextJS and have an idea about the structures of the directory.
2. Firstly cloned the repo then created dockerfile.
3. Used official node image from docker hub. Set up working directory for the container and copied all the files in this directory.
4. Also set up the port of the container in the Dockerfile as EXPOSE 3000.
5. Created docker-compose.yml file in the root directory.
6. Named service of the container and assigned build with dockerfile.
7. Assigned port as “4000:3000" (Map port 4000 of the container to port 3000 on the host machine).
8. Assigned network type as bridge as it is based on container isolation.
9. Assigned whole project directory to /app (working directory of the container) and mounted this with the use of volume.
10. This finishes our docker_compose.yml file.
### Error: 
1. Faced error that node:alpine is not available in my account -> so pulled it from Docker Hub and error resolved.
2. Some dependencies not found error came -> but resolved by running npm install again which recreated the node_modules folder with all dependencies.
* Cannot find module _graceful-fs error_ -> resolved by running npm install graceful-fs may be graceful-fs is used in the project but it is not mentioned in _package.json_ so installed it.
