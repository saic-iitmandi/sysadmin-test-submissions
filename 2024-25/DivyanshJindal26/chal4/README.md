# steps
- Create the 'Dockerfile' for backend and the frontend.
- I also wrote the nginx.conf file for the nginx proxy server to redirect requests where they should come to. 
- Then setup the docker-compose to implement the postsql redis using  alpine image, nginx, postgres, frontend and the backend. Also implemented an app network for easier handling between the containers.
- Then started everything up using `sudo docker-compose build` and then `sudo docker-compose up`.

# issues/hurdles
- first try to turning the server on. Error in step 6 while building the frontend. [Error](https://pastebin.com/raw/Zns7r0uA)
- After focusing on this error and rebuilding the frontend's packages by deleting the package-lock file everything built correct;y
- Doing `sudo docker-compose up`, turns on the frontend correctly, completing exercise 1.12.
- Got error while turning the redis on [Error](https://pastebin.com/raw/yeApkV2M)
- The redis was showing to turn on successsfully int he terminal by after going into the docker container, and running ping didnt work thru the redis cli meaning it wasnt listening.
- I had to explicitly allow the redis page using `sudo iptables -A INPUT -p tcp --dport 6379 -j ACCEPT` and then restart everything which finally worked.
- Well kinda. This ended up fucking wiith the backend meaning the backend wasn't even turning on and automatically shutting down immediately [docker ps](https://pastebin.com/raw/bAcLXgxx)
- Upon further and very very long thinking and shitting my brain for 2h I found out in the logs that some module wasn't getting installed [Error](https://pastebin.com/raw/CbQbzfpy)
- So upon advice from Mr. ChatGPT, I updated the dockerfile to use `debian:bullseye-slim` instead of `gcr.io/distroless/base-debian10` as that doesn't include the needed `glibc` versions. But that didn't work either so I had to remake the dockerfile for the backend. Used the image `alpine` and explicilty installed the rqeuired `glibc`.
- After that everything was working in theory, and everything built correctly. And lo and behold visitng the page on localhost:3000 (frontend) work and displayed the frontend. BUTTT nothing was working on it haha. [Logs](https://pastebin.com/raw/PV10FT5K)
- So then I learnt that the API requests were being sent to the same url localhost:3000 while my backend was actually hosted on localhost:8080. So I used a nginx proxy to reroute the requests. I used the 80 port to accept all the requests. If the url was localhost:80/api/.. it redirected the request to localhost:8080/... (the backend) while removing the 'api' part cuz thats how the backend is setup.
- For the frontend, any other requests except the 'api' ones were redirected to the 3000 port but as I was using the 80 port to redirect te frontend as well, I used the 'frontend-service:80' in the nginx.conf file.
- Initially I had hosted the nginx proxy on the port 3000 only cuz I didn't really know how it works, which gave me an error cuz the frontend was also hsoted on the 3000 port. Then I used the 80 port for the nginx. [Error](https://pastebin.com/raw/A1d2dcsn)
- So the frontend and the backend was now working on the 80 port. If the request was sent to localhost:80/api/... it got redirected to the backend and it also removed the 'api' part in it cuz thats how the backend is setup.

- After this, most of the frontend and the backend was working successfully. 
- All the buttons except one was working as you can see in the screenshot 'frontend.png'. Only the one where it sent a POST request to /api/messages to send a new message didn't work. I tried doing the POST request through POSTMAN but that worked and worked correctly however I got a 403 Forbidden in the browser.
- I spent more than 3h or so trying to fix it. Mr. ChatGPT told me multiple things which couldve happened. Also from my past experiences, the major thing which could cause it is CORS. This is because postman bypasses the headers and the CORS testing and thaat could be the reason why postman worked but browser post request didn't. I tried adding the headers back to the nginx.conf proxy as I suspect it mightve been that and tried addings cors allowance in the nginx.conf as well but that didn't work either. 
- Hence to check this I created a text html file to JUST send the https request to the backend portal which also gave me a 403 forbidden message. I haven't been yet able to figure out why this is giving error on JUST post request, but working 100% fine on the GET requests.

- **Final Thing in this: I was unable to make the POST /api/messages route working thru the frontend but everything else works**
- I have also attached a Recording.webm file to show what error I am getting and that the rest of the webpage is working fine :)
- PS. The recording was done when the main website was at port 3001, and I edited the main port to the 80 port (or just localhost) after this

# Setting up securities for DBs
- For the redis and the postgresDB I have added security such that only the stuff on the app network have direct access to them. This way it can only be access by the backend and not even the host device can access the DBs directly. This results in a secure setup which cannot be easily fabricated and broken into.
- I have also added `security_opt: - no-new-privileges:true` for both the redis and the postgres db which makes sure that no new priviledges can be assigned to them after it has been hosted.
- Also, the frontend CANNOT be accessed through any port. The frontend is only exposed thru the nginx redirect on the 80 port making it more secure so that no one can access the frontend directly.
- Only the backend has the environment variables needed to access the DBs making sure even if thru some vulnerability, no one can access the DBs either.
- After this, I set everything up such that NO ONE outside the app network has access to the backend api. This was done by only exposing the backend thru 8080 port to the app network. This meant that only the stuff there can access it thru the 8080 port and no one else. Going to localhost:8080/ping gives not found and postman also errors out. This ensures that the backend can be only accessed thru the frontend making full security. 
- Used a bridge for the network so that no one outside the network can interact with it.