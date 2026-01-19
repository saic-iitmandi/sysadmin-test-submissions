### I got to know about Git Forensics from this problem

Recovered Flag: `SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}`

<br></br>
# Explanation

1. I extracted the file and used ls -la to check if there were any hidden files/folders.
2. To my surprise there was a hidden folder named `.git`
3. I then ran `git log` and checked each of the 3 commits one by one using `git show <commit_hash>`, but nothing suspicious found there.
4. Then inside the .git i found lost-found folder which git uses for storing dangling commits. So I checked if there were any dangling commits using `git fsck --full`
5. Yes!!, There were 2 dangling commits there. 
    - One of these commits gave code for the encryption scheme and the ciphertext, but 2 vars in the code didn't had their values shown explicitly. They were actually the encryption params.
    - The other commit was merge commit. I checked both of the merge commit hashes and the second hash had the value of these 2 params.

6. I then made a python script which takes each ciphertext (number) 1 - by - 1 and uses all the printable characters (32-127) by hit and trial method to encrypt and check if it matches the ciphertext considered currently. If yes, breaks the loop and adds the char in the final string and continues for each of the ciphertext values.
7. The final string when printed was nothing other than the flag: `SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}`
