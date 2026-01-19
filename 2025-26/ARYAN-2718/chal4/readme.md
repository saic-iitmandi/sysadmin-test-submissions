# Challenge 4 – The Bakery’s Secret Recipe

  

## Introduction

  

This challenge focused on forensic analysis of an exposed directory that initially appeared harmless. The objective was to investigate the folder, identify any hidden or deleted information, and recover the flag.

  

At first glance, the folder only contained basic files related to a small bakery project. However, the presence of a `.git` directory hinted that the real information might be hidden in Git history rather than in the visible files.

  

The challenge turned out to be a mix of Git forensics and basic cryptography, requiring deeper inspection beyond the working directory.

  

All analysis was performed locally on a Windows system using PowerShell.

  

---

  

## System & Tools Used

  

- OS: Windows 11  

- Shell: Windows PowerShell  

- Version Control: Git (Git for Windows)  

- Programming Language: Python 3  

  

Git was used to inspect hidden commits and recover deleted files, while Python was used to decrypt the recovered data.

  

---

  

## Step 1 – Initial Inspection of the Folder

  

After extracting the provided archive, the directory contained:
- README.md  
- menu.txt  
- .git directory  

  
The visible files did not contain anything suspicious, and no flag was present in the working directory.

A recursive search for the flag format (SAIC{}) confirmed that the flag was not stored in any visible file.

This suggested that the flag was likely hidden in Git history rather than in the current state of the repository.

---

## Step 2 – Git Forensics: Identifying Hidden Commits

  

To inspect deleted or unreachable data, a Git filesystem check was performed:

git fsck --no-reflogs


This revealed two dangling commits. Dangling commits are commits that are no longer referenced by any branch but still exist in Git’s object database.

Finding dangling commits strongly indicated that important files had been deleted intentionally and needed to be recovered manually.

  

---

## Step 3 – Recovering Deleted Files from the First Dangling Commit

  
Inspecting the first dangling commit revealed two deleted files:

- oven.py  
- baked_goods.txt  

  
Findings:
- oven.py contained Python code that performed encryption using the pow() function.
- The encryption logic showed that each character of the flag was encrypted individually using RSA-style modular exponentiation.
- baked_goods.txt contained a list of integers, which represented the encrypted form of the flag.

At this point, it was clear that the flag was encrypted and could not be read directly.

---

## Step 4 – Recovering RSA Parameters from the Second Dangling Commit

  

Inspecting the second dangling commit revealed a deleted .env file.

This file contained the RSA public key parameters:

n = 13081  
e = 19  

With the encryption logic from oven.py and the RSA parameters from .env, all the necessary information to decrypt the flag was now available.

---

## Step 5 – Cryptographic Analysis and Decryption


The RSA modulus n was factored as:
13081 = 103 × 127

Using this, Euler’s totient function was calculated:
φ(n) = (103 − 1)(127 − 1) = 12852
The private key exponent d was then computed as the modular inverse of e modulo φ(n):
d = 4735

  

Using these values, a Python script was written to decrypt each number from baked_goods.txt and convert the result back into characters.

---


## Step 6 – Flag Recovery

  

After running the decryption script, the output printed by Python was:

SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}

  

This confirmed successful decryption and recovery of the hidden flag.

---

## Flag Meaning

  

The flag:
Even logs can lie, trust no one.

  

This message directly reflects the core lesson of the challenge:

- Visible files and logs cannot always be trusted
- Deleted Git history can still contain sensitive information
- Proper forensic analysis is required to uncover the truth
---

  

## Screenshots Submitted

The following screenshots were captured and included as part of the documentation:

1. Extracted folder showing .git directory 
2. Search showing no visible flag in working files 
3. Output of git fsck showing dangling commits 
4. Deleted files recovered from the first dangling commit 
5. Encrypted contents of baked_goods.txt 
6. Encryption logic in oven.py 
7. Deleted .env file containing RSA parameters 
8. Python decryption script 
9. Final execution output displaying the flag  
---
## Final Result
- Hidden Git data successfully recovered  
- RSA encryption correctly identified  
- Ciphertext decrypted using derived private key  
- Flag recovered and verified through execution  


Final Flag:

SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}
---

  
