# Task 1-
I think data should be secured at all the differnt levels.
	1.Storing file in a safe location. We dont want the file on the desktop where everyone can see, save the file in a folder which is password protected and only super user/administrator has the premission to access.
	2. Using file systems that support encryption. eq. (ext4, NTFS, F2FS, etc.) and encrypt the directory.
	3. I think using JSON format to store the data would be a good option as it allows fast and easy read/write/update
 	   and can be used by many software systems since most of the languages have a JSON parser to parse the data into their own object format.
 	4. Hash the password. Instead of storing it as plain text, we hash the password using a good one way hashing algo(md5, bcrypt etc).
 	5. Salting the passwords. Appending/prepending random text to the password can save it from rainbow table attacks.
 		Salting the hash. We can further append a fixed length random string to the hash.
	6. Using slow hashing algos can slow down the hacking process.
	7. Hashing should be done at the client side sofware first, before moving to the server, because, if the request 	is made through an open public internet, it could be easily sniffed by attackers.
	8. Log retention. Logs should be maintained for opening/viewing/editing the file.
	9. Instead of storing data in an external harddrive, USB or other portable devices, we can back it up on a 
	private cloud which are secure and only one client can access the data.

### Advantages
	1. Json is easy to read/write/update.
	2. There are libraries like ijson which make it possible to read the json data iteratively(just like cursors in sql) which makes reading less memory consuming and a lot faster.
	3. USB/harddrives can be lost, stolen or corrupted easily, but by storing it in a private cloud with regular syncing, even if the harddrive gets corrupt, the data is still secured on the cloud.
	4. Hashing and salting are the most commonly used and secure way to store passwords.

###Disadvatages
		1. Password to the cloud service account or encrypting software could get compromised.
		2. If the cloud service is down or their servers get hacked, then we need other backup modes like HDD, USB etc.
 
# Task 2-
## Making a VPN server - 
### How i did-
	1. Made an account on amazon aws.
	2. Visited console (console.aws.amazon.com) and select EC2 service.
	3. Clicked launch instance.
	4. I selected server running Amazon Linux AMI 2.
	5. General purpose t2.micro is the only free service available. Clicked review and launch.
	6. Clicked edit security groups and added a rule with following attributes - 
		Type - Custom UDP
		Port - 1194
		Source - anywhere
		Clicked review and launch
	7. Clicked launch.
	8. In the pop up i selected make new key pair and saved the key pair. Clicked launch. Now i had a running instance.
	9. went to the streisand github page and from the instructions, installed and setup striesand on the remote server.

## Resources
https://www.comparitech.com/blog/vpn-privacy/how-to-make-your-own-free-vpn-using-amazon-web-services/
https://github.com/StreisandEffect/streisand