THE DETAILED WRITEUP ON HOW THIS FLAG WAS FOUND:

## Environment and Tools Used

- Operating System: Linux

- Shell: Bash

- Tools:

- tar

- ls

- cat

- git

- git log

- git show

- git grep

- git rev-list

- git fsck

- nano

- python3

## Step 1: Initial Setup and Extraction

- The provided file was a compressed archive:

chall6.tar.gz

- The archive was extracted using:

tar -xvzf chall6.tar.gz

- After extraction, the directory contents were inspected:

ls -la

- This revealed:

A .git directory

README.md

menu.txt

The presence of .git confirmed that this was a Git repository.

## Step 2: Initial File Inspection

- The visible files were inspected:

cat README.md
cat menu.txt

- README.md contained basic bakery information and operating hours.

- menu.txt contained a short list of items with no obvious sensitive information.

- At this stage, no flag or encoded data was visible in the working directory.

- Although, in the files, a special emphasis was give to a "cookie"

## Step 3: Commit History Analysis

- The Git commit history was examined:

git log

- Three commits were present (oldest to newest):

the bakery is open

add menu

update hours

## Step 4: Commit Diff Inspection

- Each commit was inspected individually using:

git show <commit_hash>

- Observations:

The update hours commit only modified README.md

The add menu commit added menu.txt

The initial commit added README.md

No secrets were found in file diffs. This eliminated the common case of secrets being added and later removed from tracked files.

This indicated that the flag was likely not present in the visible files or standard diffs.

## Step 5: Repository-Wide Searches (Trial and Error)

- Keyword searches were performed to identify any obvious flag markers:

the presence of the word "cookie" led me to believe this might have something to do with browser cookies, but  the dangling files found later rendered that possibility pretty unlikely.

git grep SAIC
git grep flag
git grep secret
git grep recipe
git grep cookie

These searches returned no results, confirming that the flag was not present in plain text within tracked files.

## Step 6: Git Object Enumeration

- To inspect all Git objects known to the repository, including those not visible in the working tree, the following command was used:

git rev-list --objects --all

- This output listed several object hashes without associated filenames. This suggested the presence of unreferenced or dangling Git objects, which are common hiding places in forensic challenges.

## Step 7: Identification of Dangling Objects

- A full integrity check was performed:

git fsck --full

- This revealed:

Two dangling commits

The presence of dangling commits indicated that content existed in the repository but was not reachable from the current branch.

## Step 8: Inspection of Dangling Commits

- Each dangling commit was inspected using:

git show <dangling_commit_hash>
Findings
Dangling Commit: batch archive

- This commit revealed two previously unseen files:

1) oven.py

2) baked_goods.txt

- oven.py

This file contained Python code showing that:

The flag was encoded byte-by-byte

Each character was encrypted using modular exponentiation

The encryption resembled RSA-style encryption:

cipher = pow(byte, e, n)

- baked_goods.txt

This file contained a list of integers, representing the encrypted form of the flag.

At this point, the encryption logic was known, but the encryption parameters (n and e) were missing.

## Step 9: Initial Decryption Attempt (Trial and Error)

- A Python script was written to brute-force printable ASCII characters by re-encrypting them and matching against the cipher values.

- An initial attempt used guessed values for n and e, which resulted in blank output.
 This confirmed that the encryption parameters were incorrect or incomplete.

- I dont remember the assumed values of n and e, but they were close to the actual values found later.

## Step 10: Merge Commit Analysis

- Further inspection of the dangling commits revealed a merge commit with two parents.

- The merge parents were inspected individually:

git show <parent_commit_hash>

- One of the merge parents revealed a hidden .env file.

- This .env file contained the missing encryption parameters:

n = 13081
e = 19
(AKA THE SECRET RECIPEEEE)

## Step 11: Correct Decryption

With the correct parameters identified, the Python decoding script was updated to use:  (the updated python file is attached in the deliverables folder)

n = 13081
e = 19

The script brute-forced printable ASCII characters (range 32–126), re-encrypted them, and matched them against the cipher values.

Running the script:

python3 decode.py

Successfully produced the flag in the required format:

SAIC{<REDACTED_FLAG>}


## P.S.:
- I had been watching DEXTER since a couple of weeks, and that really got me interested into forensics stuff. What im tryna say is I really enjoyed
  solving this question. 
- Thanks for reading my bullshit P.S. :)
