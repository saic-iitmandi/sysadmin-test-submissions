# Docker Deployment - Nutrient Tracker

## Setup and Deployment

### Build and Run Containers
```bash
docker-compose up --build
```
Got this error 
```69.96               nokogiri
------
Dockerfile:18
--------------------
  16 |     
  17 |     # Install gems
  18 | >>> RUN bundle install
  19 |     
  20 |     # Copy the rest of the application code
--------------------
ERROR: failed to solve: process "/bin/sh -c bundle install" did not complete successfully: exit code: 5
```

# Docker Deployment - TIP

created the ```dockerfile``` and ```docker-compose.yml``` using GPT obv 

then did ```docker-compose up --build```

then ```docker ps``` got the container running 

and there it was on ```http://localhost:3000```
