created an automation script for pulling an image and deploying it in container 
for running it run "bash automation.sh <image name>"

created a docker-compose file attached alongwith that deploys 3 replicas of app and also starting a service for loadbalancing for that depends on app

deploying using command "docker-compose up -d"

by default it uses round robin load balancing that distributes service requests uniformally on all three instances

while running got an error and was not able to resolve it so no demonstration available

# LEARNING OUTCOMES:
- Docker hub<br>
- Scaling and load balancing using docker-compose with nginx<br>
