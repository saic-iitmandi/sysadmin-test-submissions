docker-compose down
docker-compose pull
echo "Enter the number of web instances:"
read WEB_INSTANCES

docker-compose up -d --scale web=$WEB_INSTANCES