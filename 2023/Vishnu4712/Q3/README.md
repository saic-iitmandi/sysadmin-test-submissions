First I cloned both the repositories.
Command used:

git clone <github_url>

For Dockerfile 1 (HTML-CSS-JS Website): I used nginx image from Alpine Linux as the base image. Then I had set the working directory as "/usr/share/nginx/html". Copied files from SAIC-Website directory to the container. Exposed port 80.

For Dockerfile 2 (Ruby on Rails Website): Used the official Ruby image as the base image. I had set the working directory inside the container to "/app". Copied the Gemfile and Gemfile.lock to install dependencies. Then, copied the rest of the Ruby on Rails application code to the container. Exposed port 3000 for the Rails application.

Docker-Compose File: Defined two services, one for each website (html_css_js_website and ruby_on_rails_website). Specified the build configuration for each service, including the Dockerfile, context, and tag. Mapped host ports to container ports.

Then I ran the "docker-compose build" and "docker-compose run" command which unfortunately gave me an error.
Commands Used:

docker-compose build
docker-compose run