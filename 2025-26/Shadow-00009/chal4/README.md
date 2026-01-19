This is my attempt on the challenge 4 of sysadmin 25-26.

I downloaded the folder and extracted it.

The first thing i did was to use the grep command to see if there is something with "SAIC{" but obviously it wasn't.

So i put the folder onto gpt and asked for the flag and i got it:
SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}
I really didn't expect to get the flag like this so i will be summarizing on what i understood and what should have been done.


When we opened the folder what we see is a .git folder suggesting that this folder is a git repository and what we know about git is that "git remembers".

What would be the things that might have the flag:
Commit history

So what was inside the Commit history?
There were two commits -: "add menu" and "update hours"

In the commit:"0c9b415b8bcf290a471df48b2dc255e1bb94f14d" we find that this file contains RSA related Data and explicit cryptographic components "p, q, e, n, encrypted ciphertext"

RSA security depends on p and q being secrets but since we have both of those it completely breaks the RSA

In the second commit:"2084ffce98c493ee02c07b1943817f2b9acfb6db" we find that the sensitive RSA values have been removed. 

The flag was obtained by using the RSA math on commit 