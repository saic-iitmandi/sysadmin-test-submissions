FROM alpine:latest
# Install bash, standard docker-cli, and net-tools for netstat
RUN apk add --no-cache bash docker-cli net-tools
WORKDIR /app
COPY docker_manager.sh .
RUN chmod +x docker_manager.sh
ENTRYPOINT ["/bin/bash", "./docker_manager.sh"]