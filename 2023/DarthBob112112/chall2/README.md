Used the ubuntu bash shell docker `docker run -it ubuntu bash` from docker hub for testing purposes.
Used mail+postfix to send the mail through gmail smtp relay to the email id.
Set up a cronjob to run the script every ,inute(this can be changed to whatever is most appropropriate

Steps for testing:
1. Download [dockermonitor.sh](dockermonitor.sh). Give it execution permissions.
1. Set up your mail relay on postfix. [How to set up a gmail smtp relay](https://www.tutorialspoint.com/configure-postfix-to-use-gmail-smtp-on-ubuntu). ([Creating App Password for Gmail](https://support.google.com/accounts/answer/185833?hl=en))
2. set up cronjob for the bash script
1. Run the docker `docker run -it ubuntu bash`. Wait for the script to run. Exit the docker by typing exit in the shell. Check your email.

https://github.com/DarthBob112112/sysadmin-test-2023/blob/main/chall2/Screencast%20from%2001-11-2024%2002%2050%2033%20AM.mov

video above
