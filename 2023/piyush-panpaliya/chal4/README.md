## Challenge 4 - Docker & Networking

this was an easier one so I just wrote some bash scripts for part 1 and 2

### Part 1

```bash
#!/bin/bash
IMAGES=("metavinayak/matrix")

PORT=8000
for IMAGE in "${IMAGES[@]}"; do

    docker stop $PORT || true
    docker rm $PORT || true

    docker image pull $IMAGE
    echo "Running $IMAGE on port $PORT"
    docker run -d --name $PORT -p $PORT:3000 "$IMAGE"
    ((PORT++))
done

```

- it simply loops thorough all the image ids and stop if a same name container is runing
- starts a container from that image

### Part 2

In this we had to create multiple instance and load balance them, so I created a `docker-compose.yaml` with

```yaml
version: '3'

services:
  web:
    image: metavinayak/matrix
    ports:
      - '3000'

  load-balancer:
    image: nginx
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    ports:
      - '8000:80'
    depends_on:
      - web
```

this has two services:

- the web service
- nginx

and I have mounted my conf file in nginx service and it also depends on web service

Now to create multiple instances we use
`docker-compose up -d --scale web=3` this will create 3 containers with random ports on host side and will all run same web image.

now since nginx and these are in same docker network I can call web service with `web:5000` due to the internal DNS it resolves to all the IP of web service containers and nginx simply balances all the requests.

so I a using a bash script that ask for number of instance to run and run the above command

### Part 3 logging
