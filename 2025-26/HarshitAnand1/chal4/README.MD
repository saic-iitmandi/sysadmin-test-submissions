Q4.
SAIC{ev3n_5t_n0_0n3}


At first,i sawvThe folder only had two files:

README.md

menu.txt

Both of them were just bakery-themed text. Nothing encoded was there.(sad harshit noises--pardon random shit its midnight and deadline just extended to 12:30 i'm just getting weird thots)

Since the challenge description mentioned a Git repository
so i listed EVERYTHING

> ls -la

no time to format :(
there was 

> .git/

then checked the commit history

> git log --oneline --all

to check more i ran

> git fsck --lost-found

this had dangling commits
so i thot i have some clue
then started to inspect these by 
> git show <commit_hash>
it had python script and one file w numbers

so basically it was rsa encryption
n=13081

and factoring it
13081 = 103 × 127

then got the flag

SAIC{ev3n_5t_n0_0n3}

