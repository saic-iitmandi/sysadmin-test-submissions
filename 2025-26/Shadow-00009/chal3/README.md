This my Attempt at Challenge 3 of Sysadmin 25-26

In this question we have been given two repositories for two different projects. We have to deploy both projects using Docker containers on my localhost.
So the first thing i did was opened my ubuntu this question's directory and cloned both repositories.

Then i moved on to make Dockerfile for the frontend and backend of both the repositories.
I wrote the code for all of them.
Now i made .yml file which defines everything that we are going to run in the bash script.
And finally wrote the bash script we need and then deployed the script.

But as expected i got an error as the standard npm did understand the syntax in my Royal-chess's Backend file so i changed it to yarn and again ran the file and found a new error this time where the requested Node.js version needed the higher version than the one in my dockerfile so i changed it to the required version and same with Frontend.

After deploying the file again i got a new error as the frontend was trying to download a package from internet which was only locally available so i made changes to code and also changed the python version in the stac backend deployed the code.

after deploying what i got was monorepo issue and i solved it as well but encountered many more errors. I couldn't solve this question.i have attached all the errors i faced inside the errors folder in this challenge.
Would really like to know what i was doing wrong in this question.