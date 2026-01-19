
# Challenge 4 – The Bakery’s Secret Recipe

## Overview
During an audit of an exposed directory, a Git repository belonging to an internal bakery project was discovered. Although the files appeared harmless, deeper forensic analysis of the Git history and objects revealed hidden sensitive data.

The objective was to investigate the repository and recover the hidden flag.

---

## Initial Inspection
The provided folder was identified as a Git repository by the presence of a `.git` directory.

Initial commands used:
- `ls -la`
- `git status`
- `git log --oneline --all`

This revealed multiple commits, suggesting that historical data may contain hidden or removed information.


## Git History & Object Analysis
To uncover hidden content, Git forensic techniques were used:

- Examined commit history using:
  ```bash
  git log --oneline --all
