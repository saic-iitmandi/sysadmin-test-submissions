# Sahil Yadav, B15130

# Administration Assessment
****

1.	There were many approaches that I came across:

	* We can `rsync` the file with some other machine/rsync daemon itself. This will keep copy of file updated whenever we `rsync` the two hosts. See `man rsync` for more.
	* We can use some [DVCS](https://en.wikipedia.org/wiki/Distributed_version_control) (git, mercurial, etc.) which can maintain a stable copy at every point of time.
	* Though this is a bit complicated (and a bit impractical for what I think), but if possible, we can save a deep copy of our file in [CMOS memory](http://www.pcguide.com/ref/mbsys/bios/comp_CMOS.htm) where the BIOS configuration is stored. This way, the file will be kept safe even if the harddisk gets corrupted. Currently CMOS memory is much less in size (around 64 bytes each), and the data we will be having in a year is around 140 kB (144,000 lines in total assuming 50 characters per line,i.e, 50 bytes constitute one line), it's a bit hard to distribute such amount in the CMOS memory. But we never know what [Moore's law](https://www.britannica.com/topic/Moores-law) has in store for us!

	Since there was no question on the security of content of the file, I have refrained from going on deeper on that aspect. I took help from IRC freenode's `##networking` channel for the last option.

****

2.	This was one of the longest tasks. It took quite sometime to set up Amazon AWS account (due to some authentication reasons,etc.). After a day or two of waiting, I received my credentials. Then I installed `streisand` on my machine. Of course, it showed some [errors](https://github.com/StreisandEffect/streisand/issues/1007) which got resolved by using `python2` and not `python`. During the process I came to know that new accounts can access [EC2 servers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)  only from [three](https://stackoverflow.com/questions/46649542/aws-ec2-cant-launch-an-instance-account-blocked?answertab=votes#tab-top) locations. This step did cost me much of the time. After that, it was easy to set up the VPN which is described in [VPNsetup](https://github.com/me-ydv-5/sys-admin/blob/master/Administration/VPNSetup.md) file.

****
[End of Report]

&copy; Sahil Yadav
