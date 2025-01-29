## Question 4 - Dockerizing a fullstack app (frontend+backend)

### Steps for containerizing the frontend and backend applications. 
- Make a Dockerfile for frontend (inside frontend folder) and a Dockerfile for backend (inside backend folder) which will provide the environment setup for the docker container
- Created a docker-compose.yml file which arranges the services inside the container.
### Configuration of a secure network for communication between containers.
- I have created two custom network named frontend-network and backend-network which are bridge network type as bridge is the best network type when we need to set up a good communication among the container. As we are using four services i.e. frontend, backend, database, redis frontend need to communicate with backend and backend has to connect to database so internal communication is very important.
### Hosting details
#### Inside docker-compose.yml:
- Backend, database, redis are connected to the backend-network, ensuring that they can communicate with each other but not outside the network.
- Database is not exposed outside the container network (no ports: directive is used instead expose is used to ensure it's only accessible to other services within the backend-network.).
- Backend communicate with the database using an internal Docker network (backend-network).
- Added .env files to secure the _POSTGRES_USER, POSTGRES_PASSWORD_
- Frontend and backend are isolated to prevent direct communication
- Redis is also secured with backend network
#### Changes in Infrastructure
- update trypostgres.go to use environment variables for database connection:


### Best practices to secure the database:
- .env file to secure secret credentials 
- Regularly update your base images to the latest stable versions to avoid any vulnerability to be found and attacked.
- Database backup by using docker volumes.

__NOTE__:

- Attached Dockerfiles of frontend and backend and docker-compose file .

- Also attached some screenshots.
