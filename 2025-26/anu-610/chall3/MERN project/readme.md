1.  First create a dockerfile and then used lightweight node -alpine verison.

2. Copied all necessary files, and then follwed the instrunction in readme.

3. Then the docker-compose.yml

4. in docker compose, first setup the 
    database,
        for retrieving data on restarting i used volume.
        then set the env variables,
        then set the netowork to royalchess (user-defined bridge)
    
    then the docker file,
        exposed both, ports,
        set the env,
        also set constrains that it will start only if database work properly,
    
    then created the bridge network and volume


4. then just run the command docker compose up --build

5. build executed succesfully.. 

6. App is running succesfully.