# **SAIC SysAdmin Test**
## Task 4. Docker Deployments

Run multiple website on different docker conatiners

1. CP DASHBOARD(ReactJS)
- Clone the github repo.
- Change the directory to CP-DASHBOARD
- Make a Dockerfile.
Contents of the docker file are below.
~~~
FROM node:alpine
WORKDIR '/app'
COPY package.json .
RUN npm install --force
COPY . .
CMD ["npm", "start"]
~~~
- After making the Dockerfile, build the image using the command `docker build -t react . --name <conatinername>`
- Run the container using the command `docker run <conatinername>` and type the respective address:port in the browser.


2. STAC IIT Mandi
- Clone the github repo.
- Change the directory to xray-burst-detection
- Make a Dockerfile.
Contents of the docker file are below.
~~~
FROM ubuntu
RUN apt update
RUN apt install python3-pip -y
WORKDIR /app
COPY . .
RUN pip3 install -r /app/requirements.txt
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
~~~
- After this, build the docker image using the command `docker build -t flask . --name <conatinername>`.
- Then run the container and go to the respective address:port to view the site.


3. SAIC IIT Mandi
- Clone the github repo.
- Change the directory to CP-DASHBOARD
- Make a Dockerfile.
- Run the following command in the terminal.
`docker run -d -p -v $HOME/mysite:/usr/share/nginx/html \ --name <containername> nginx`
- The website will be hosted on your local host. You can find the port in the docker desktop app or by using `docker port <containername>`.
