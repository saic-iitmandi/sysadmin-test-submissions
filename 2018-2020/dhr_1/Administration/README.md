Problem 1:
 In this problem, according to me best possible way to protect out file is to encrypt it. So, first we need to select encryption technique or method, AES 256 will work in this scenario. AES encrytion is symmetric so we don't need private or public keys(We are not sending it to someone else). 

 Next job is to select a passphrase. A passphrase is the weakest link here. So, We can select two passphrases ,then encrypt our original file with 1st one (with armored ascii output ) , then encrypt this output file with the other passphrase. 

 Next job is to write a program(in your favourite language shell script/c/c++ program etc.) to encrypt our data. We can use gpg for this, but i am experiencing some strange problems with it, so i suggest using some library for encryption(like pycrypto,etc.(https://gist.github.com/mimoo/11383475)).

 Now, using this program, we can securely store our passwords and update it whenever we want. Also we can keep an additional copy of this encrypted file on gitlab(because it offers private repositories for free). This way we can make sure our file is safe.

Problem 2:
 
 For this task main resource I used was streisand README.md file. First i tried to install streisand on default settings but by default it was using a $10/month plan and the installation failed due to many issues. So, I created a droplet and installed streisand on it without some features. 