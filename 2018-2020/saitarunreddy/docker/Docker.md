# Steps to create a docker image and publish it in docker hub:
1) Install Docker on your system and create an account in the docker website.
2) Use the credentials to login into docker application.
3) Open the directory where you want to develop your application and create a file with the name `Dockerfile`.
4) Type the code in the Dockerfile to create the required image.
5) Use the `docker build` command in the terminal to create an image.
6) We can use the `docker run` command to test out our images.
7) Once the development of the application is done and successfully made it into an image, we can upload it to desired repositry using the `docker tag` command.
8) We can publish the image to docker hub by using `docker push` command.
9) We can run the published image from any system using the `docker run` command.

## For more details and explanation:
- https://docs.docker.com/get-started/part2/
- https://rominirani.com/docker-tutorial-series-writing-a-dockerfile-ce5746617cd

