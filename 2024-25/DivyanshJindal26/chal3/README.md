# setting up nutrient tracker
- downloaded all contents using git clone
- wrote multiple iterations of dockerfile for it.
- Building the container: `sudo docker-compose build`
- Turning it on: `sudo docker-compose up`

# issues while dockerising it
- both the websites were conflicing and getting hosted on the same url and fucking evreything up.
- had to upgrade the version of devise to make it not throw errors because of "secret_key not set". Tried setting key in the environment variables and editing the content of the said file, didn't work. Manually upgraded the version of it in package.json file. [Error](https://pastebin.com/raw/C95xbfH9)
- Also got this error leading me to finally upgrade the version of device [Error 2](https://pastebin.com/raw/GvNv077Y). The error told me to edit a file which doesn't exist ;-;
- JavaScript runtime wasn't working, so I had to include npm/javascript helpers runtime in the dockerfile of nutrient tracker [Error 3](https://pastebin.com/raw/7EZJ91W7)
- MULTIPLE errors while migrating the redis db as well. Website was turned on but nothing was working and showing me the complete error and telling to migrade db. When used the script it gave, sent multiple errors shown [here](https://pastebin.com/raw/hxaZjqLa) -> fixed by giving it the required perms
- After giving perms, it said ruby.exe not found. So had to manually add the ruby path to the system [Error](https://pastebin.com/raw/xsG5ubPH). Tried doing some things suggested by google, stackoverflow and chatgpt [like this](https://pastebin.com/raw/AFbWf571)
- Ended up remaking all the rails files using rails app:update:bin to remake all the files in the /bin folder which actually worked.
- Got the devise error again, so tried a lot of thing to manually upgrade the versoin of devise and ruby to eradicate [this error](https://pastebin.com/raw/HyDjw0EP)
- Initially it couldn't even find the gemfile in there for some reason. i dont remember how i fixed it :\( [Error](https://pastebin.com/raw/6k3ScgS8)

- another major thing, ubuntu ran out of storage, and when i tried restarting it went into recovery mode or smth, didn't let me do anything, black screen with lots of errors. had to boot ubuntu into recovery mode, and clear lots of shit, googling, and spent around 3h fixing it. Althought after doing that it works fine now lol.

- back to errors. Got this error and installed python stuff to fix it. didn't work and had to bypass it by installing more stuff. [Error](https://pastebin.com/raw/JKfMyDUT). [Another Error](https://pastebin.com/raw/J7Zat89i)
- ok the errors for this end here. now we go to the hosting and erroring of the other TIP website

# hosting of TIP website
- the steps remained mostly the same. just had to edit the dockerfile to install nodejs, then run the npm install and then the npm run build cmd.
- merged the previous website with this one in the same docker-compose file.
- the other steps remain the same

# issues
- well we are back again.
- i don't know why but a LOT, like A LOOOT of times, the website was "docker-compose build"-ing correctly, and even that npm run build was working fine. It was showing all the elements built and stuff. But when I went to turn the website on using docker-compose up, it kept saying that next was not found. From what I can infer, it was because I was specifying the volumes in the dockerfile and it was overwriting it somehow. When i removed that and just put the volume as [], it then worked. [Error](https://pastebin.com/raw/ctDTPNEc)
- honestly this is the only error i can remember in this except the multiple interations of the dockerfile lol cuz its a very very new repo and hence nothing was broken unlike the previous one ;-;

# reason for bridge
- I used the docker network type bridge for both the ruby on rails and the nextjs project.
- I have used bridge on the ruby on rails project because that projec relied on the redisdb and sql and the bridge networks allowed easier and isolated communication between them keeping everything private and seperate and prevents the hot network from viewing it. it also doesn't expose useless ports to the host providing a secure space and preventing data leaks from the db. It 
- For the nextjs project it has more or less the same reasoning. The TIP website involved google sign up which, if exposed, can lead to major issues. Also the backend could be connected to a backend api in the future if needed and using bridge will only expose the neede ports to the public. The nextjs project involved firebase which is easier and more secure in a bridge network. bridge is suitable for web apps which majorly involve the browser and the docker's nextjs container. 