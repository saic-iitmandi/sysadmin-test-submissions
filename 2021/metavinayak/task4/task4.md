## Instructions:

There are 2 scripts and one python file(Flask app) present for task 4

The `auto_fetch.sh` is able to detect whether a repository has changed on a remote branch.It checks whether the **remote url exists or not**.It automatically **switches to the same branch as the remote branch being pulled**.It **also checks for merge conflicts** and informs the user as per the case.

### To use it,just specify the path of local git repository at the start of the file as :
`cd <path to local repo>`

The working of the script is done as comments in file itself.

### See the working of scripts here(video) :

https://drive.google.com/file/d/19hMafpgQvCXeqk3NmQpHfRCr79rOplpu/view?usp=sharing

(Pls open with eductaional id)

------------------------------------------------------------------------------------------------------

## BONUS: 

The `redeploy_after_auto_fetch.sh` performs all the tasks that `auto_fetch.sh` does.However it also locally redeploys the flask app('app.py') in the same repository.

To redeploy some other repo flask app,specify the path of local git repository at the start of the file as :
### `cd <path to local repo>`

The working of the script is done as comments in file itself.

------------------------------------------------------------------------------------------------------

## References :

Google searches.Some previous knowledge of bash.

Performing Dry run(if pull is needed):

https://stackoverflow.com/questions/3258243/check-if-pull-needed-in-git 

https://www.christianengvall.se/check-for-changes-on-remote-origin-git-repository/


https://www.cyberciti.biz/faq/unix-linux-bsd-appleosx-bash-assign-variable-command-output/

Error in assignment to bash variable:

https://stackoverflow.com/questions/28186162/how-do-i-store-the-output-of-a-git-command-in-a-variable


## Learning outcomes :

Learnt more about git workflow(remote vs local), about `--dry-run` flag and automated handling of errors and merge conflicts.

Learnt to check the status of command outputs using Bash variables and grep.

Learnt making conditional statements and error handling in Bash(`exit 1`).

Learnt redeployment automation of Flask app and about git pull automation by combining fetch and merge(better compared to direct pull).