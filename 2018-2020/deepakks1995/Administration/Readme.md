Censorship:

First of all we had to run an instance of AWS EC2 machine:

	1. Make sure you have an active AWS account with all information verified. Now select EC2 from services by loggin in to the console.

	2. Now select the type of OS which you want in your instance. I selected ubuntu and then hit launch

	3. To connect to the instance simply select the instance and hit connect button. This will open a dialog box showing the necessary steps. Just simply follow the steps.

Now we have successfully established a ssh connection to our EC2 instance.

Now just simply follow the steps given in the streisand github page i.e. https://github.com/StreisandEffect/streisand
and install the appropriate libraries in our EC2 instance.

Once the installation has started, we would have to wait for 10 minutes in which simple options will be given to us like the location of our servers, server name , fill in all the info and wait.

Now after successfull installation, a new folder is generated named 'generated_docs' which contains an html file named 'serverName.html'
that contains all the steps required to connect to your VPN server.
