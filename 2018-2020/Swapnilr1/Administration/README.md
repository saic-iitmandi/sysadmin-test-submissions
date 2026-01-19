# Task 1

I am not yet able to fully solve this problem. However I will describe the approach I have thought of:
Resource used: https://superuser.com/questions/370423/method-to-add-to-an-encrypted-file-without-providing-a-password

I do not know of a way to securely store as well as update the passwords in a SINGLE FILE. However I have thought of a way where I have a container (a directory/folder or archive) where each file would contain username and password for one website.

Let us say web application X (most probably a password manager) is responsible for updating the passwords.

I would then encrypt the contents of this archive/directory using a public key, which would generate an encryption (public) key and a decryption (private) key. I would upload the public key to application X, so that it can encrypt any new password being added. 

When I need to look at the passwords, I enter my passphrase (which acts as a "master password") to access the private key.  

So in essence, new passwords get automatically encrypted (preferably on a Web application) before being added to the PC's hard disk. New encrypted passwords can get added, but nobody can decrypt any password without the private key.

Cons:

1. If the passphrase for the private key is available, the system is completely compromised.

# Task 2: Setting up VPN server

1. I created an AWS account and completed registration. 
2. Then I found the instructions for installing `streisand` at https://github.com/StreisandEffect/streisand/blob/master/README.md
This made the work very simple. 
3. I added an access key to my AWS account, and the rest was handled by `streisand`.




