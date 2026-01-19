I started Challenge 2.
In this challenge we have to analyse Docker Container logs, detect critical issues and handle clash scenarios for the containerized websites.

So,First i make a .sh file on my VS code named docker_monitor and write the script for the code for it.

now i opened my ubuntu and opened my folder where i created the file in the ubuntu.
i used the "ls" command to check if the bash is present and yes the file was present so now we move forward.

Now I execute the command "chmod +x docker_monitor.sh" which makes our script executable.

i run the script and as expected it shows us


as we do not have any containers running
So now what does the Script do:
The Script scans all running docker containers,extracts critical and error level logs,detects host port conflicts, and attempts automatic recovery by restarting affected containers. This ensures service stability and quick remediation of common Docker deployment issues.”


Now that i know that the script is working fine.it was time to run containers.

So i make a container using command "docker run -d --name web1 -p 8080:80 nginx"

By running the "docker ps" command i confirm that i have a running container

Now, I run the "Error generator" Container and "Healthy" container
"docker run -d --name buggy-app alpine sh -c 'while true; do echo "[CRITICAL] Database connection failed!"; sleep 5; done'"
"docker run -d --name clean-app alpine sh -c "while true; do echo 'System running smoothly...'; sleep 10; done""

and now it was time to run two containers on different ports:
docker run -d -p 8081:80 --name web-server-1 nginx
docker run -d -p 8082:80 --name web-server-2 nginx

so now i start with PORT CLASH

I try to run another container on same port by using "docker run -d --name web2 -p 8080:80 nginx" which would give me a error 

So to forcefully make the clash i change the line in the scipt from"host_port=$(echo "$mapping" | awk -F: '{print $2}')" to "host_port="8080" " which gives the error in the logs 




This was my attempt at Challenge 2 of sysadmin 25-26

