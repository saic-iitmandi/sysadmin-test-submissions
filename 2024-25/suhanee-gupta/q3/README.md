## CHALLENGE 3- docker deploy for 2 technology stacks

started by cloning both the repositories. im going to be making separate containers for Nutrient Tracker and TIP app and mapping them to ports on localhost.
The nutrient tracker was Ruby based. honestly i had no knowledge about ruby and took a lot of online help for that dockerfile. the TIP project backend was next.js. Finished the dockerfiles for both projects. 
next i made the docker compose file, and started the services.
i chose to make a bridge network here. it seems to be the default for communication between multiple containers from what I have learnt so far. other than that, they also seem very simple to set up, didn't have to make any complex changes in the configurations for this. 
when i ran the services i got multiple errors thrown. seemed to be an error witht the "RUN npm install" command in Dockerfiles and with the bundler as well. i changed the version of npm on my localhost to match the one used in the files. 