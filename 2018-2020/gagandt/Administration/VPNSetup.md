OpenConnect / Cisco AnyConnect
	

	Windows
	Download the OpenConnect GUI installer.
	Run the OpenConnect GUI installer.
	Complete the TAP-Windows Setup Wizard.
	Choose the default options, and allow the TAP driver from the OpenVPN project to be installed.
	Launch the OpenConnect application.
	Click the Edit icon (gear) and select 'New profile advanced'.
	Enter streisand for the Name.
	Enter 139.59.87.216:4443 for the Gateway.
	Enter streisand for the Username and click Save.
	Click Connect.
	A prompt will appear during the initial connection asking you to trust the server's certificate. Click The information is accurate and the server will be automatically verified for all future connections.
	Enter fade.adult.insane.spring.already for the Password and click OK.
	Click No when the Windows prompt appears asking Do you want to allow your PC to be discoverable....
	The current beta version of the OpenConnect GUI does not support automatically changing the DNS settings. In order to avoid DNS leaks, the following steps must be performed:
	Right-click on the Windows Start Button.
	Click Network Connections.
	Right-click on the device that you are using to connect (Ethernet or Wi-Fi) and click Properties.
	Double-click Internet Protocol Version 4 (TCP/IPv4).
	Select Use the following DNS server addresses and enter:
	8.8.8.8
	8.8.4.4
	Click OK.
	Click OK to close the connection properties.
	You should be good to go! You can verify that your traffic is being routed properly by looking up your IP address on Google. It should say Your public IP address is 139.59.87.216.

	macOS
	Install Homebrew, if you haven't already.
	Install OpenConnect using Homebrew:

	brew install openconnect

	If installing Homebrew is not an option, you can also download and compile the OpenConnect source code.
	Download the server certificate file, and a client certificate file from the list above.
	Place the downloaded server certificate and a selected client certificate into a separate folder (e.g. streisand-openconnect), open your Terminal, and cd to that directory.
	Run OpenConnect:

	sudo openconnect --cafile ca.crt --certificate your-client-certificate.p12 --key-password 'your-client-certificate-password' --pfs 139.59.87.216:4443

	You should be good to go! You can verify that your traffic is being routed properly by looking up your IP address on Google. It should say Your public IP address is 139.59.87.216.

	Linux
	Install the OpenConnect plugin for NetworkManager.

	sudo apt-get install network-manager-openconnect-gnome

	Download the server certificate file:
	ca.crt
	Open your System Settings.
	Click the Network icon.
	Click the + button in the lower-left of the window.
	Select VPN from the Interface drop-down and click Create.
	Select Cisco AnyConnect Compatible VPN (openconnect) and click Create.
	Enter streisand for the Connection name.
	Enter 139.59.87.216:4443 for the Gateway.
	Select the ca.crt file that you just downloaded for the CA Certificate.
	Click Save.
	Select the VPN in the left-hand menu, and flip the switch to ON. You can also enable/disable the VPN by clicking on the WiFi/Network icon in the menu bar, scrolling to VPN Connections, and clicking on its name.
	Enter streisand for the Username and click Login.
	Enter fade.adult.insane.spring.already for the Password, check Save passwords, and click Login.
	You should be good to go! You can verify that your traffic is being routed properly by looking up your IP address on Google. It should say Your public IP address is 139.59.87.216.

	Android
	Download Cisco AnyConnect from Google Play.
	Launch the application.
	Tap OK to accept the "Supplemental End User License Agreement for AnyConnect® Secure Mobility Client vx.x and other VPN-related Software".
	Tap the menu icon and select Settings.
	Uncheck the Block Untrusted Servers option.
	The server certificate will be imported during the initial login and automatically verified for all future connections.
	Tap the back button.
	Tap Connection and then tap Add New VPN Connection....
	Tap Description and enter streisand.
	Tap Server Address and enter 139.59.87.216:4443.
	Tap Advanced Preferences.
	Tap Certificate.
	Each profile can be downloaded on the device itself using the links above, or copied from your computer via USB.
	Check the Download folder if you downloaded the file directly to the device. This is where Chrome places its files, for example.
	Tap Import, tap File System, and select a client certificate file from the list above that you transferred.
	Enter your client certificate password when the Password prompt is displayed, and tap Connect.
	You'll see a checkmark next to the newly imported certificate. Tap the back button.
	Tap Done twice to save the connection.
	Tap the back button to return to the main screen. You should see streisand in the Connection section.
	Slide the AnyConnect VPN switch On.
	Tap Details when the Security Warning is displayed.
	Tap Import and Continue when the Certificate Summary is displayed.
	Tap Connect on the group selection screen. The correct default has already been chosen.
	If this is your first time using AnyConnect, you will need to accept the Connection Request dialog that Android displays.
	You should be good to go! You can verify that your traffic is being routed properly by looking up your IP address on Google. It should say Your public IP address is 139.59.87.216.
	Prompted for username?
	Some users have reported that their Android AnyConnect clients prompt for a username and password. This is a known bug we don't understand. See the list of Streisand AnyConnect open issues. If you're affected, you could help us understand the bug by reporting your details using the issue list's New issue button's template. Fixes are gratefully accepted too.

	If you're affected, you can use this workaround:

	When prompted for a user, enter streisand
	When prompted for a password, use fade.adult.insane.spring.already

	iOS
	Note: When using AnyConnect for the first time, you may be prompted for a password prior to being connected. Enter streisand for the username, fade.adult.insane.spring.already for the password and continue. Subsequent connections will not prompt you again.
	Note: Only one AnyConnect profile can be configured at any give time. To remove an existing profile, go to Settings -> General -> Profile, tap on the profile you wish to remove, then tap on Remove Profile.
	Transfer a .mobileconfig file for each device you wish to configure:
	major-walk.mobileconfig
	depend-shrimp.mobileconfig
	slam-cargo.mobileconfig
	focus-pill.mobileconfig
	pool-picnic.mobileconfig
	The profile can be emailed to your device (simply tap the attachment), transferred via the Apple Configurator utility, or downloaded directly by viewing these instructions on the device itself.
	Follow the on-screen instructions.
	You will be prompted to enter your device password or pin.

	Download Cisco AnyConnect from the App Store.

	Launch the application.
	Tap OK to enable the software when the dialog box appears.
	Tap Settings.
	Turn off the Block Untrusted Servers switch.
	The server certificate will be imported during the initial login and automatically verified for all future connections.
	Tap Home.
	Slide the AnyConnect VPN switch on.
	Tap Details when the Security Warning is displayed.
	Tap Import in the top-right corner.
	Tap Connect on the group selection screen. The correct default has already been chosen.
	You should be good to go! You can verify that your traffic is being routed properly by looking up your IP address on Google. It should say Your public IP address is 139.59.87.216.