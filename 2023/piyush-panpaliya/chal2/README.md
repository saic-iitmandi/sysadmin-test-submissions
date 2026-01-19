## Challenge 2. Docker Monitoring & Scripting

ok so I am currently helping in winter project about the same so it was a llittle easier for me

- first of all I used docker SDK to access the containers on machine.
- APscheduler is used to schedule the task of monitoring the containers

### Flow:

- When the scripts run for the first time it reads all the containers and stores them in a json file `containers.json` with name and id of it.
- Then it starts the scheduler which runs every hour.
- In which it reads all the containers from `containers.json` and check if the status is `running`
- Reads previous down services from `containerStatus.json` and checks if there are new services down.
- If a new system is down, it sends a mail as follows:

```
services that are still down:
serviceName was down
serviceName was down

=======================

new service(s)down at DD:MM:YY HH:MM:SS :
serviceName Logs:
some logs
===========
serviceName Logs:
some logs

```

PS: I have kept email template very simple and I know its **BAD**

and adds the down service to `containerStatus.json` now just throw it to a daemon

### Improvements

- I am assuming when the script is run all the required containers are present in exited state atleast.
- To add new services the script has to be restarted
- very bad code written for haddling json and file exception
  (was pretty tired after using ruby image from 7 years ago for chal3)
