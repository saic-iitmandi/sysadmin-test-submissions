Flag :- SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3} (even logs can lie trust no one)

in this challenge, i was given a folder that contained a git repository related to a small bakery project . the task was to use forensic techniques to investigate the repository and recover a hidden flag.
(most of the codes for this one was ai , i still knew the process for git investigation)

i first checked the contents of the folder, README.md ,menu.txt and .git
no flag was visible in these files itself

i checked the commit history :-
    git log --oneline --all
output :-
    2084ffc update hours
    0c9b415 add menu
    9c89d2e the bakery is open

all commits looked clean. no flag was visible in any of the files. this suggested that the flag might exist in deleted or hidden git things .

to search for hidden git things, i ran :-
    git fsck --lost-found
this showed two dangling commits ;- (exist in database but not reachable through any branch)
    63570471b6d86a7c63ddb2fc3dd5d55da624e1ea
    a3e00065651d7bb9a54c10a9157696e07903ebac

i inspected the first dangling commit :-
    git show 63570471b6d86a7c63ddb2fc3dd5d55da624e1ea

This commit contained two files:-
    baked_goods.txt
        a list of numbers:
        [8186, 10208, 3632, 12587, ... , 8477]

    oven.py
        n = p*q
        m = flag.encode()
        cypher = [pow(b, e, n) for b in m]

so the flag was encryped , but i didnt know the decryption part so i thought ill use ai , but before decrypting i thought ill first search for p,q,n and e (or only n and e could also work)

i inspected the other dangling commit’s parent:
    git show 47c8d89

this showed a .env file containing:
    n = 13081
    e = 19
13081 = 103 × 127
p = 103
q = 127

then i ran the decrypting python file (ai) to get the output as the flag :- (copy is in the folder)

Flag :- SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}

i also did a raw .git directory search, checked reflog and stash to be sure no other flag is present
i knew deleting data from git can be tough and complicated but i can see that it can also be a high security risk