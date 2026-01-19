# Administration

## Question 1

This problem can be divided into two parts:
1) To restrict the access to data.
2) To save it from hard drive crashes.

Solution to part 1:
- Since we would be using the password to attempt login we can not use hashing algorithms to store them because hashing algorithms are not reversible.
- So we need to store the passwords by encrypting them with 2 way encryption. There key required for encrpytion should be stored safely in this method. So storing it in a file is the main disadvantage of this method.

Solution to part 2:

- Many companies which deal with data storage like google, amazon store a single piece of information on multiple servers and periodically update all to same data.
- One possible solution is to have `multiple hard drives` and store this data on them. We can write to one of the hard disk and sync all other hard drives after successful updation/addition of passwords. This sync can happen once every hour to save the data from a single hard disk crash.
- We can also create a `master storage` online which also has the same data but only gets updated `once in a day`. This file can be hosted using an online service.


## Question 2
I have used Amazon AWS free tier service to host the VPN service. I have followed the steps given on https://github.com/StreisandEffect/streisand to setup the VPN. I had no other troubles while following the steps for installation.
