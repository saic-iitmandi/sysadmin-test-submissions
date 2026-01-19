Installation:
https://docs.docker.com/engine/install/ubuntu/

https://realpython.com/offline-python-deployments-with-docker/
https://realpython.com/dockerizing-flask-with-compose-and-machine-from-localhost-to-the-cloud/
https://realpython.com/docker-in-action-fitter-happier-more-productive/

Basics:

docker system prune
or 
docker rm <id>

eg:sudo docker rm f44ea5411a5a -f

use --rm during 'docker run'




Using apache:

https://www.middlewareinventory.com/blog/docker-reverse-proxy-example/

https://stackoverflow.com/questions/46099348/how-to-use-apache-to-redirect-to-docker-container


https://stackoverflow.com/questions/43786208/multiple-vhosts-on-one-and-the-same-docker-container


https://phoenixnap.com/kb/how-to-set-up-apache-virtual-hosts-ubuntu

__________________________________________________________________________________

Tried Method 2:

https://www.middlewareinventory.com/blog/apache-reverse-proxy-what-how-to-configure-setup-reverse-proxy/

https://www.freecodecamp.org/news/docker-nginx-letsencrypt-easy-secure-reverse-proxy-40165ba3aee2/

```
<VirtualHost *:80>
  ServerName ubuntu.somesite.com

  <Location />
    Order allow,deny
    Allow from all
    Require all granted
  </Location>

  ProxyPass /app1 http://127.0.0.1:8080/
  ProxyPassReverse /app1 http://127.0.0.1:8080/

  ProxyPass /app2/ http://127.0.0.1:8081/
  ProxyPassReverse /app2/ http://127.0.0.1:8081/
</VirtualHost>
```
__________________________________________________________________________________

Docker:(nginx is more complex)

reverse proxy on nginx:

https://stackoverflow.com/questions/46040152/docker-multiple-sites-on-different-ports

https://nginx.org/en/docs/http/request_processing.html

https://www.youtube.com/watch?v=x1fnOJsX6wE

sudo apt install nginx

unlink the 'default' configuration file within sites-enabled

Making our own config in conf.d directory

https://phoenixnap.com/kb/docker-nginx-reverse-proxy

https://www.digitalocean.com/community/questions/how-to-bind-multiple-domains-ports-80-and-443-to-docker-contained-applications


When we are running multiple app that you can’t have them all listen on the same port.So a Nginx reverse proxy must be set up in front of the containers.

For two different app. Bind them to a random port on the local host:

```
docker run -d -p 127.0.0.1:3000:80 coreos/apache /usr/sbin/apache2ctl -D FOREGROUND`

docker run -d -p 127.0.0.1:5000:80 coreos/apache /usr/sbin/apache2ctl -D FOREGROUND
```

Then you can configure an Nginx sconfiguration that looks something like this:

```
upstream app-a {
    server 127.0.0.1:3000;
}

upstream app-b {
    server 127.0.0.1:5000;
}

server {
        listen 80;
        server_name test.com www.test.com;

        location / {
            proxy_pass         http://app-a;
            proxy_redirect     off;
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;

        }
}

server {
        listen 80;
        server_name example.com www.example.com;

        location / {
            proxy_pass         http://app-b;
            proxy_redirect     off;
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;

        }
}
```
### Tried lots of stuff but couldn't make the required working docker :')


### Learning outcomes :

Learnt why and how to set up a docker image.Docker image is specific for the given kernel and utilized the kernel of the OS it is made on.So all running tasks inside the docker can be easily simulated by anyone across the world if we make our docker image public(Provided they have the same kernel).

Leant more in depth about apache and nginx server.

Learnt about Virtual hosts and DNS server and port redirecting.