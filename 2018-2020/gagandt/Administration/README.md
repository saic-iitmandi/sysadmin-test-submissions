1.
	Problems we wolud be facing are :
	- Keep this information confidential.
	- Keep a backup of this information.

	Solution(s) :
	The first part :
		We'll probably save this information in a file.
		1.
		We can make a script (python/shell) to encrypt and decrypt the contents of the file.
		=> 	How the information would be encryted-decrypted: 
			- We'll create a script to read from the file except the "S.No" and the "Website" column.
			- Encryption would be using a hashing function which would be two way.
			- An example of the hashing function can be :
				key = user input
				len = str.length()
				for i from 0 to len :
					str[i] = str[i] + (-1)^(i)*key + (-1)^(i-1)*len
				
			- A reverse hashing fucntion can also be created for the encrypted file to decrypt it.

		2.
		easiest option :
		Convert a password protected zip of the file and save it to hard disk.
		
	The second part :
		Outcomes of both the methods would be a file (txt/zip).
		We can either directly upload the file to a cloud storage. 
		Or if we also want to automate this part, we can make an application or script to upload the file on google drive, or a free web hosting platform like 000webhost.
		I implemented the latter solution (somewhat similar) on "http://exodia.in/publicity" (don't click the submit button without entering anything or try to hack. Its for hackers.)
		
	Pros :
		The best benefit of the second soultion would be if we make a portal on website like 000webhost, we can directly enter the data in sql, and on click of single button, we ca download a zip file.

	Cons:
		We'ld have to manually upload the file to google drive or rather we'ld have to run a script to do so.
		

2.
	Didi everythinkg from the documentation.
	Completed at th last minute.
	
	