# Methodology
## Step-1
Extracting the given files in the linux terminal by using ('tar -xvzf chall6.tar.gz') . Once extracted, the directory was entered ( cd chall6) . At this stage, the folder appeared normal and contained common project files such as README.md and menu.txt
## Step-2
While inspecting the directory using a long listing(ls -la), a hidden .git folder was discovered.The presence of the .git directory indicated that this was a Git repository. This is important because Git stores historical data, including previous versions of files that may have been deleted or modified. Exposing a Git repository on a public server is a security risk, as attackers can often recover sensitive data from it.
## Step-3
To understand how the project evolved over time, the commit history was examined using ('git log --oneline --all') . The commits appeared to be related to routine updates for the bakery project, such as updating the menu or business hours. None of the visible commits contained sensitive information or flags.

This suggested that the flag was likely hidden in deleted commits or unreachable Git objects rather than in the active project files.
## Step-4
Used command (git fsck --full) to check the internal structure of a repository and identify broken or unreferenced objects. This command revealed two dangling commits, meaning commits that still exist in Git’s database but are no longer linked to any branch.
 - dangling commit 63570471b6d86a7c63ddb2fc3dd5d55da624e1ea
 - dangling commit a3e00065651d7bb9a54c10a9157696e07903ebac
Dangling commits are often created when developers delete commits or rewrite history. Since Git does not immediately remove these objects, they can still be recovered.
## Step-5 
On further examining the first dangling file using ( git show 6357047 ) , it contained two files:
- baked_goods.txt - This file contained a list of numbers rather than readable text. This strongly suggested that the data was encoded or encrypted.
- oven.py - This file contained a Python script. After reviewing the code, it became clear that the script was performing RSA encryption on a message. Each character of the message was converted into a number and encrypted using mathematical operations.

From this it was concluded that:
- The numbers in baked_goods.txt were encrypted data.
- The encrypted data likely represented the hidden flag.
## Step-6
RSA encryption requires two values:
- A public key (n and e)
- A private key (d)

## Step-7
The second dangling commit was inspected: (git show a3e0006 )

This commit did not directly reveal any useful files. However, inspecting its parent commit uncovered additional information.

git show 47c8d89

This commit revealed a deleted configuration file containing the RSA public key values:

n = 13081

e = 19
## Step-8 
In real-world scenarios, RSA uses very large numbers that are computationally infeasible to factor. In this case, the value of n was small, making it possible to factor manually.

13081 = 103 × 127

Using these factors, Euler’s Totient value was calculated:

φ(n) = (103 − 1)(127 − 1) = 12852

The private key d was then calculated as the modular inverse of e modulo φ(n).

d = 4735

## Step-9
With the private key recovered, the encrypted numbers from baked_goods.txt were decrypted using Python.

flag = bytes([pow(c, d, n) for c in encrypted_values])

This converted each encrypted number back into its original ASCII character.

# Conclusion 
The decrypted output revealed the hidden flag:

SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}


