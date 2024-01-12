First I downloaded docker after which I pulled two different images of nginx (nginx:1.25 and nginx:3.25) from docker hub and then I ran two different containers on it.
Commands Used:

docker pull nginx:1.25
docker pull nginx:3.25

docker run -d -p 8080:80 --name nginx:1.25
docker run -d -p 8081:81 --name nginx:3.25

Monitoring Method Used: 

The monitoring method I used in this script is a simple periodic check of the status of Docker containers. The script checks whether each container is in the expected state ("Up" or "Healthy") every 60 seconds. If it detects a container that is not in the expected state, it sends an email alert.

monitor_docker Function

1) I used subprocess.check_output to run the docker ps command with the --format option to specify the format of the output. The format includes the container ID, container name, and container status. 

2) I then iterated over the container information list and checked the status of each container and if the status of the container is not in the expected states("Up" or "Healthy") then it would send an email alert using the send_email function.

3) I then used time.sleep(60) to check the status after every 60 seconds.