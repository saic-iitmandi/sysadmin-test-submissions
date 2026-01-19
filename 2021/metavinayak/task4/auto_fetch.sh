cd ~/SAIC/saic_auto_pull # specify the path of local cloned repository here

remote_name="origin"    # remote name to pull from (eg:upstream,upstream2)
branch_name="main"        # remote branch to pull from to a local branch with same name(assumption)

check_remote=$(git remote -v 2>&1 | grep -c $remote_name)
# 2>&1 means to redirect stderr output to the stdout so bash variable can recieve the output.
if [ $check_remote != 0 ] # remote repo exists
then
    echo "Remote url found...checking status"
else
    echo -e "Remote url NOT found.\nTo add remote use:\n'git remote add <Name for remote,eg:upstream,upstream2> <github remote url>'"
    exit 1
fi

# Assumptions:
# 1)The branch specified is present in remote repo
# 2)Pulling is being done in the same named branch in local repo(standard procedure)

branch_exists=$(git branch -v | grep -c $branch_name) # locally

if [ $branch_exists == 1 ]
then
    current_branch=$(git branch -v | grep -c "* $branch_name" )
    if [ $current_branch == 0 ] # branch specified is NOT the current branch
    then
        echo -e "Switching to the specified branch..."
        execute=$(git checkout $branch_name)       # not necessary but preferred
    fi
else
    echo -e "Branch not found locally...creating the branch\n"
    git checkout -b $branch_name
fi

flag=$(git fetch $remote_name $branch_name -v --dry-run 2>&1 | grep -c "up to date")
# echo $flag

if [ $flag == 0 ] # not updated
then
    git fetch $remote_name $branch_name -v
    echo -e '\nRemote repo is outdated...Fetching changes then merging'
else
    echo 'Remote repo has been already fetched...merging changes if not yet merged'
fi

merge_msg=$(git merge $remote_name/$branch_name 2>&1)
merge_status=$(echo $merge_msg | grep -c "Already up to date" )
conflicts=$(echo $merge_msg | grep -c "merge failed" )

if [ $merge_status == 0 ] 
then
    if [ $conflicts != 0 ] # Merge conflicts occur
    then
        echo 'Merge conflicts occured...Aborting merge'
        git merge --abort
    else
        echo 'All fetched changes have been merged successfully.'
    fi
else
    echo "Local repo is up to date with Remote"
fi