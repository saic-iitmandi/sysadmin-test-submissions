# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 20:54:34 2024

@author: arani
"""
from emailautomation import auto
import docker
import time
from datetime import datetime
docker_client=docker.from_env()
while True:
    for container in docker_client.containers.list(all=True):
        try:
            container.reload()
            if container.status != 'running':
                current_datetime = datetime.now()
                subject = f"Container Alert - {container.name}"
                body = current_datetime.strftime("%Y-%m-%d %H:%M:%S")+"\n"
                body += f"Container {container.name} has exited or changed state.\n"
                body += f"Container ID: {container.id}\n"
                body += f"Image: {container.image.tags[0]}\n"
                body += f"Status: {container.status}\n"
                auto(subject,body)
        except docker.errors.NotFound:
            body+=f"{container.name} of {container.image.tags[0]} has been removed. \n"
            auto(subject,body)

        time.sleep(100)