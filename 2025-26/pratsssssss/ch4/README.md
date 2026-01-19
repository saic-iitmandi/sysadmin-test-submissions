**What i had**
We were given a bakery project folder containing a git repo.

**What i did and Where i landed**
- first extracted it and moved the folder to my wsl workspace and then opened it in ubuntu.
- firstly i tried to check for flag manually but didn't got anything lol. 
- then tried grep and still came up with nothing.
- well after some digging it was clear that this was maybe a cryptography or maybe just a general one but with hidden flag maybe or maybe a forensics one.
- then after some time i finally noticed the git repo whihc i totally ignored at first and dived into the other folders.
- well thanks to participating in some ctf challenges before i had some knowledge that atleast what to do when u see a git repo. 
- so i went n analyzed its history and got some dangling commits, where i thought the flag must be cause this was my only progress till now and going back in folders was nothing but pain in ass.
- so now i had dangling commits so i inspected them with git cat-file and got tree objects.
- inspected the tree and got 4 things:
  from first dangling commit's tree i got 2 things 
    1. baked_goods.txt
    2. oven.py
  from second one's tree i got again 2 other things:
    1. .env
    2. README.md

- checked all 4 of em and from .env got 2 variables saying 'our super special secret ingredients' and from baked_goods.txt got an array which was  definitely the encrypted text.
- dig some more and got cypher = [pow(b,e,n)for b in m] in oven.py, did some research and get to know that this matched the signature of RSA encryption. 
- well now i have already enough material so again went on internet did some google and watched some yt clips and finally found a mathematical way to decrypt this. 
- did some calculation and wrote my .py script but was stuck at ASCII conversion part as the code i was using decrypting everything excepts one value which was outside the ASCII range.
- after 2-3 hr, finally decided to go to chatgpt and it gave me reason maybe it's because of my python's version so it gave me another way (Euclidean algorithm), used that in my .py script and now my problem was resolved and finally got the flag which is:
   **SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}** 