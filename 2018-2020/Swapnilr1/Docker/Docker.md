My docker store image is at https://store.docker.com/community/images/swapnilrustagi/sysadmintest/

Please see the `v3` version in the tag, i.e. use `docker run swapnilrustagi/sysadmintest:v3`

## How I made my Docker image

1. I went to the Docker website, created my account on Docker Store, downloaded and installed Docker Community CE. I searched for Docker documentation and found this [excellent getting started page](https://docs.docker.com/get-started/).
2. Part 1 gave me an idea of what actually is a container, what does Docker do.
3. Part 2 showed how to make a Dockerfile and then an image from it. Specifically, it has an example of making a Docker image based on Python and the file shows what each command does by comments. This is how I understood the concept and some syntax of Dockerfile.
4. I searched in the Docker Store for an Ubuntu container, and in tags I found that multiple versions are given. Consequently I edited the sample Dockerfile to use an Ubuntu 16.04 image, and also edited the `WORKDIR` and `ADD` paths to `/home` as was required. I also modified the `CMD` command in docker file to `./testfile.sh`
5. I then saved my Dockerfile in a directory and created the required `testfile.sh` and then proceeded to build the image and run.
However, it gave an error that `testfile.sh` was not found.

## Fixing the error

1. I modified the `CMD` command parameter in Dockerfile to run `ls` at the start. It showed that the `testfile.sh` was copied.
2. After a lot of searching, trying `RUN` instead of `CMD` (though I later found out that `CMD` is the correct one to use here), searching about `File not found` in Dockerfile, I tried `CMD sh /home/testfile.sh` instead of my previous `CMD ./testfile.sh` and it worked.

Note that `v2` and `v3` are minor non-technical corrections from `v1` of my DockerFile. `v1` printed `Sahil Arora` instead of my own name, and `v2` had name as `testscript.sh` instead of being named as `testfile.sh`.


## What I learnt

1. Dockerfile syntax - FROM, WORKDIR, ADD, CMD, RUN etc.
2. Docker syntax - Building, running and uploading Docker images to Docker Store.
3. How containers are different from virtual machines, advantages.
4. A bit about bash/shell scripts.

Finally I tested my Docker image to see how it would work on other computers with [Docker Playground](https://www.katacoda.com/courses/docker/playground).
