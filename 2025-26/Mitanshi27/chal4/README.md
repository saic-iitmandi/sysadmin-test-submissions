Challenge 4 – The Bakery’s Secret Recipe
Overview

While auditing an exposed directory on the server, I discovered a folder that turned out to be a Git repository related to an internal “bakery” project. At first glance, the files looked harmless, but since version control often retains hidden or deleted data, I decided to analyze the repository more deeply.

The goal was to investigate the repository using forensic techniques and recover any sensitive information left behind.

Initial Investigation

The presence of a .git directory confirmed that the folder was a Git repository. I began by checking the repository status and commit history to understand how the project evolved over time.

Using git log, I noticed multiple commits, which suggested that earlier versions of the project might contain files or data no longer visible in the working directory.

Git Forensics & Hidden Data

To go beyond the current state of the repository, I inspected older commits and explored Git’s internal object storage. While examining the .git/lost-found directory, I discovered orphaned commits that were not referenced by any active branch.

Inspecting these orphaned commits revealed a tree containing additional files that were not present in the main project. These included a Python script and a data file that appeared suspicious.

Analysis of the Hidden Files

The Python script showed logic related to encryption, and the accompanying data file contained a list of numerical values. By reading the script carefully, it became clear that the numbers represented encrypted character values, using RSA-style modular exponentiation.

This confirmed that sensitive information had been deliberately hidden in the repository but was still recoverable through Git object analysis.

Decryption & Flag Recovery

Using the encryption logic and parameters extracted from the repository, I wrote a small decryption routine to reverse the process. After decrypting the numerical values, the output resolved into readable text.

This revealed the flag in the expected format.

Recovered Flag
SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}

Conclusion

This challenge highlights how sensitive data can persist in Git repositories even after being removed from visible files. Commit history, orphaned objects, and internal Git structures can all leak critical information if repositories are not properly cleaned.

It reinforces the importance of auditing version control systems thoroughly, especially when repositories are exposed on public-facing servers.
