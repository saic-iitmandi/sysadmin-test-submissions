Starting on the last day I was not able to complete this one

I first started with downloading the virt-manager for KVM/QEMU virtualization as I had read it is better on linux than oracle virtualbox (which i have used before)
Initially i was getting this blank screen then fount out that we need to click on the ctrl+alt+f2 button inside the vm after going full screen
Since i had to use chatgpt and that requires copy paste i basically accessed it via SSH through my ubuntu terminal

Checked the ip4
Then i identified open services
Going to the ip it showed 
Then i checked the backend code
It has an internal endpoint 
GET /internal/export

Then i checked the internal token

Called internal endpoint from within the VM: and got service token

Also i found that the worker accepts POST only

After that i tried determining the authentication field but it returned 403 everytime 🙁

