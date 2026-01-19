
**The flag I found = SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}**
# The way I found this
* First, I installed the link. And went to the terminal and started extracting it with ** tar -xvzf chall6.tar.gz*.
* This thing I searched how to extract things from these types of files, I know only for .zip extensions.So made a search.
* After this, it extracted all. A few words got my attention, like lost, lost and found. I just moved forward to check what is present in this file.
*  I saw in README.md that there any direclty written flag. But no use.
* And I tried **git grep FLAG $( git rev-list--all,) then also I didn't find anything.
Then I thought that there will histroy of git will not be deleted. So I recovered the lost data from git fsck --lost-found. 
Then I got these a3e00065651d7bb9a54c10a9157696e07903ebac, like this number, and when I saw the ls in the chall6 directory,
new directories showed up like oven.py, baked_goods.txt,

I thought if these were deleted, then the flag must be in this only.,
So I checked them out them and I found one word flag, and I thought there is some code encryption ,
so there may be a link with the list of numbers given in bake_goods.txt.

So I asked how to write code to decode the code because I never saw this type of encryption.
I pasted the code and ran it, but nothing is showe.,
I checked and came to know that I need to find n and e still, and then i use -m in with the thing which I got earlier then i found the n and e and then gave these values and then ran it, it gave the flag.
* The code to decode was taken from Gemini.
