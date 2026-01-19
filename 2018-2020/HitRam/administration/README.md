## Password Manager 

The major problems can be broken down as follows - 
1. Restrict the access of the file to other people.
2. Handle the case when the file is lost (drive gets corrupted or someone intensionally did it).

#### Handling problem 1 -

Now-a-days most Operating Systems come with an option to restrict access to files. One can use those options to restrict the access to the files. For eg in Linux one can change the permissions of the file and on Mac, one can setup password to open the file.

One **problem** with this approach is that we will create a backup of this file somewhere (to handle problem 2) and if someone gets access to the servers, our passwords will be leaked. Thus to solve this problem, we will **encrypt** the data with a **master password**. Thus, one would need to remember this password to decrypt the data.

#### Handling problem 2 -

Now this problem is interesting. Because it requires syncing and having backup on and external cloud service. Data storage on external cloud service costs some bucks monthly. How to save the data without costing too much (or anything)?. 

Since we are students, we can get some free private repositories on **github**. I suggest a solution to store this file on a private repository. One can write a simple script to add commits whenver we update this file and push on this repository automatically. There are even open source softwares like **gitwatch** which does the same. This way, we even maintain a history of updates in our file. We have to make sure that the folder in which the file is kept is accessible only to root person which can be done easily. We can even develop a simple software(desktop application) which would perform this functionality. If file gets deleted and we need our passowrds, the software will pull it from the repository. 

So the software would be able to do the following - 

1. Decrypt the contents of the file using master password.
2. Encrypt the contents of thie file with master password as key while updating the file.
3. Automatically commit the changes made in the file.
4. If we are connected to a network and there are commits which are not pushed, then push it on github.

This approach works as long as we are **Students**.

One another approach is to use **Google Spreadsheets**. There is spreadsheets API which can be used by developers to update into spreadsheets. We can write a script to automatically update into the spreadsheet as the file gets updated and retrieve it back once it gets deleted.

Other approach is to use cloud services to store this file but they are free for some period and then would start costing. 

---

## Setting up streisand on Digital Ocean.

Firstly I got free 10$ credits from a website where I was learning about docker. So I made an account on digital ocean and created the cheapest droplet which was for 5$. Since my internet connection was a bit slow, I used the droplet itself to setup the Streisand as Digital Ocean's internet speed was pretty good. I just followed the [streisand's github page](https://github.com/StreisandEffect/streisand) for installation and it worked like a charm. 

I also noticed that the those who setup streisand on AWS server slowed their internet speed as compared to those who setup on Digital ocean's server.
