# Administration

## Solutions

### Problem 1
#### Problem Statement-

Come up with a solution as to how you can store all this information safe for the maximum amount of time. It is compulsory for you to have this file on your PC, you cannot delete it from your PC and store it in a bank locker. Also consider that you have to regularly update this file so updating the file should also be easy. 

#### Solution
To achieve what is required in this task we will be using GnuPG (`gpg`), which can be used for asymmetric and symmetric encryption. It is available by default in Linux systems and is used worldwide by companies to protect confidential data. (It can be installed in other OSes too). [Details](http://www.gnupg.org/gph/en/manual.html)
<br>
GPG uses public key cryptography. With public-key encryption, instead of sharing a password, each party generates a "keypair" consisting of a "public" key and a "secret/private" key. 
<br>
Creating a key pair:<br>
`gpg --gen-key` to generate the key-pair. You should probably use the default settings. <br>
Note: One tricky thing about this key generation on linux is that when generating the key itself the program complained about not having enough entropy and hung until the entropy requirement was met. When googling I discovered that this was a common complaint and most often solved by installing the rng-tools with apt-get as described [here](https://www.howtoforge.com/helping-the-random-number-generator-to-gain-enough-entropy-with-rng-tools-debian-lenny).
<br>Once you have created your key-pair, you can see your generated key by `gpg --list-keys` .<br>
Now we need to save your private key, use `gpg --export-secret-keys -a "Your Name" > yourname.priv` . Now move this file to a removable drive and put that drive in a locker( any place you feel its safe :P). Now we can delete this key from your PC, `gpg --delete-secret-keys "Your Name"`.<br>
Note: Also use `gpg --export-keys -a "Your Name" > yourname.pub` to export and save your public key somewhere in case your harddrive crashes. Save it in your email or cloud.<br>
Now we can encrypt the required file using your Public Key. <br>
`gpg --encrypt -r your@email.com filename` , use the email in your Public Key as the email address so that you use your private key to decrypt. This will create `filename.gpg`. Delete the original `filename` file.<br>
Now that the file is encrypted and safe, anytime you need to update the file, decrypt the file, make changes and encrypt it again.<br>
Plugin your removeable drive with private key  and rum `gpg --import yourname.priv`.<br>
Run `gpg filename.gpg` to decrypt the file, and make changes to it. Repeat the above steps of encryption and removing the private key and you're good to go!

To safeguard the file from dataloss, it is a good idea to backup the encrypted gpg file into a cloud server at least once everyday.

This is probably one of the most safest way in the world to safeguard the file. No one can hack into your file now even with access to your PC.

While the above method is the one of the most safest one, a more robust method can be following - 

Select the file, and choose to compress it with a password. Remember that password! Now delete the original file. To update the file, decompress the file with the password and make changes in it. Compress the file again with a password and delete the original file. 

To safeguard the file from dataloss, it is a good idea to backup the encrypted compressed file into a cloud server at least once everyday.

### Problem 2
#### Problem Statement-
You need to signup on AWS / Digitalocean / some other virtual server providing company and install streisand. Then you need to SETUP YOUR OWN VIRTUAL PRIVATE NETWORK(VPN) according to the instructions given on the streisand github page. All the supported virtual server providers are given on the streisand github page. Choose whatever you like.

#### Solution
An AWS server is used to setup streisand at [https://35.166.238.146/](https://35.166.238.146/). AWS account was setup using credits from Github Student Pack through AWSEducate. The server is hosted in Oregan (USA). 
To setup streisand, its installation procedure was followed from its [github repository](https://github.com/StreisandEffect/streisand).  It took approximately 30 minutes to setup, though the repo stating around 10 mins!

This is the best problem statement among all and enjoyed it thoroughly. Learnt a lot about working of servers, IP tables, ports, setting up virtual servers and about web services as well. To be able to setup our own servers to bypass censorship is awesome. Thank you for this problem statement. 