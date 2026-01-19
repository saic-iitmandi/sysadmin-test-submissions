    STREISAND 

* * *
* * *

* * *
I have attached a copy of certificate in the folder named 13.126.86.131.crt.

Your Streisand Gateway contains step-by-step instructions for the services it provides, and mirrors of all necessary client software.

This document covers the SSL Certificate installation instructions and will show you how to connect to the Gateway to learn how to configure clients to use the Streisand services.

* * *

*   [SSL Certificate Installation](#ssl)
    *   [Windows](#ssl-windows)
    *   [macOS](#ssl-macos)
    *   [Android](#ssl-android)
    *   [iOS](#ssl-ios)
    *   [Chromium](#ssl-chromium)
    *   [Firefox](#ssl-firefox)
    *   [Manual Certificate Verification](#ssl-manual)
*   [Connecting to your Streisand Gateway](#connecting)
    *   [SSL](#connecting-ssl)
    *   [Tor Hidden Service](#connecting-tor)

SSL Certificate Installation
----------------------------
You should install the Gateway's SSL certificate so your browser can automatically verify the integrity of the connection. This prevents anyone from tampering with your traffic and also protects your login credentials. The certificate has been embedded directly into this HTML file.

### Windows

These instructions work for Chrome and Internet Explorer. Firefox uses its own internal Certificate Manager, but it's [easy to configure](#ssl-firefox) too.

1.  Download the SSL certificate embedded in this document.
2.  Double-click to open the downloaded certificate.
3.  Click _Install Certificate..._
4.  The Certificate Import Wizard will start. Click _Next_.
5.  Select _Place all certificates in the following store_ and click _Browse_.
6.  Select _Trusted Root Certification Authorities_ and click _OK_.
7.  Click _Next_ and then click _Finish_.
8.  Confirm that you would like to install the certificate by choosing _Yes_.
9.  Close and re-open your browser.
10.  You are ready to connect. See [Connecting to your Streisand Gateway](#connecting-ssl).

### macOS

These instructions work for Chrome and Safari. Firefox uses its own internal Certificate Manager, but it's [easy to configure](#ssl-firefox) too.

1.  Go to _Applications > Utilities_ and launch _Keychain Access_.
2.  [Download the SSL certificate](#download) embedded in this document.
3.  Drag the downloaded certificate into the login keychain section.
4.  A window will appear asking if you want to trust the certificate. Click _Always Trust_.
5.  Enter your password when you are prompted to do so, and click _Update Settings_.
6.  Right-click on the imported certificate and select _Get Info_.
7.  Click the arrow next to _Trust_ and more options will appear.
8.  Choose _Always Trust_ next to the _Secure Sockets Layer (SSL)_ option.
9.  Close the certificate window and enter your password again.
10.  You are ready to connect. See [Connecting to your Streisand Gateway](#connecting-ssl).

### Android

These instructions work for Chrome. Firefox for Android uses its own internal Certificate Manager but does not provide an interface for importing certificates yet. Chrome is therefore the recommended way to connect to the Streisand Gateway.

#### Less secure, but easy

1.  [Download the SSL certificate](#download) embedded in this document.
2.  Email the downloaded certificate to an account that can be accessed from the Android device.
3.  Open the email and tap the attachment.
4.  A popup will appear. Enter `falcon` for the _Certificate name_, and make sure _VPN and apps_ is selected for the _Credential use_ value.
5.  Tap _OK_.
6.  You are ready to connect. See [Connecting to your Streisand Gateway](#connecting-ssl).

#### More secure

1.  Connect the Android device to your computer.
2.  [Download the SSL certificate](#download) embedded in this document.
3.  Drag the downloaded certificate to the root of the Android device's filesystem.
4.  Launch the _Settings_ application.
5.  Scroll to the _Personal_ section and tap _Security_.
6.  Scroll to the _Credential Storage_ section and tap _Install from storage_.
7.  Select the certificate that you copied to your phone.
8.  Enter `falcon` for the _Certificate name_, and make sure _VPN and apps_ is selected for the _Credential use_ value.
9.  Tap _OK_.
10.  You are ready to connect. See [Connecting to your Streisand Gateway](#connecting-ssl).

### iOS

#### Less secure, but easy

1.  [Download the SSL certificate](#download) embedded in this document.
2.  Email the downloaded certificate to an account that can be accessed from the iOS device.
3.  Open the email in the iOS Mail app, and tap the attachment.
4.  The _Install Profile_ screen will appear. You can view the certificate details and make sure they match the information from the [SSL Verification](#verification) section. Tap _Install_.
5.  Tap _Install_ again when the warning appears.
6.  Tap _Done_.
7.  You are ready to connect. See [Connecting to your Streisand Gateway](#connecting-ssl).

#### More secure

1.  Connect the iOS device to your macOS computer.
2.  Tap _Trust_ if the _Trust This Computer?_ popup appears.
3.  Install the [Apple Configurator 2](https://itunes.apple.com/us/app/apple-configurator-2/id1037126344?mt=12) utility from the Mac App Store.
4.  Launch the Apple Configurator utility and agree to the license.
5.  Click _Start Preparing Devices_.
6.  Click _Install Profiles..._.
7.  Turn the phone on and unlock it.
8.  Click _Next_.
9.  Click _New..._ and enter `falcon` in the _Name_ field of the _General_ section.
10.  Scroll down to the _Certificates_ section.
11.  [Download the SSL certificate](#download) embedded in this document.
12.  Click _Configure_, select the downloaded certificate, and click _Open_.
13.  Click _Save_.
14.  Check the checkbox next to the `falcon` profile you just created. Click _Next_.
15.  The _Install Profile_ screen will appear on your iOS device. Tap _Install_.
16.  Tap _Install_ again when the warning appears.
17.  Tap _Done_.
18.  You are ready to connect. See [Connecting to your Streisand Gateway](#connecting-ssl).

### Chromium

1.  Click the Menu button and go to _Settings_.
2.  Scroll to the bottom of the window and click _Show advanced settings..._
3.  Scroll to the HTTPS/SSL section and click _Manage certificates..._
4.  Go the _Authorities_ tab.
5.  [Download the SSL certificate](#download) embedded in this document.
6.  Click _Import..._, select the downloaded certificate, and click _Open_.
7.  A popup will appear. Check the box next to _Trust this certificate for identifying websites_ and click _OK_.
8.  Click _Done_.
9.  You are ready to connect. See [Connecting to your Streisand Gateway](#connecting-ssl).

### Firefox

1.  Launch Firefox.
2.  Open the _Options_ panel, and select _Preferences_.
3.  Go to the _Privacy & Security_ tab.
4.  Scroll down to the _Security > Certificates_ heading.
5.  Click _View Certificates_.
6.  A window will appear. Click on the _Authorities_ tab.
7.  [Download the SSL certificate](#download) embedded in this document.
8.  Click _Import..._, select the downloaded certificate, and click _Open_.
9.  A popup will appear. Check the box next to _Trust this CA to identify websites_ and click _OK_.
10.  Click _OK_ to close the certificate manager, and then close the _Preferences_ panel.
11.  You are ready to connect. See [Connecting to your Streisand Gateway](#connecting-ssl).

### Manual SSL Verification

_The manual certificate verification option is significantly less secure than installing the certificate using one of the methods above. Your browser will display a warning message, and you are more vulnerable to man-in-the-middle attacks because the fingerprints must be verified on every connection attempt. It should be used with great care, and only as a last resort._

The certificate details should match the following information:

##### Serial Number

`serial=AC1E4B46FE4FA922`

##### Fingerprints

    SHA256 Fingerprint=15:F4:A8:2B:37:07:CA:66:D1:D7:E4:E1:77:BD:08:91:46:8B:CE:67:38:1D:32:BC:BD:38:AE:26:37:18:3C:6F
    SHA1 Fingerprint=7F:BB:23:A1:C8:D0:03:CF:77:0D:74:1B:F4:7E:BA:1A:38:BD:4A:A5
    MD5 Fingerprint=21:A1:E9:9E:FD:15:37:49:97:17:72:85:74:C0:6D:C1
    

If everything checks out, you are ready to connect. See [Connecting to your Streisand Gateway](#connecting-ssl).

Connecting to your Streisand Gateway
------------------------------------

Each connection option takes you to the same place and you can use whichever one is most convenient for you. Fun fact: Your Gateway's unique password was generated by randomly choosing four words from a dictionary with more than 340,000 entries.

### SSL

[https://13.126.86.131](https://13.126.86.131)

username: `streisand` password: `Plasseys-stains-aforetime-gastroenterologists`

### Tor Hidden Service

_All connections to Tor hidden services are fully encrypted._

[http://aamep53rxdess6by.onion](http://aamep53rxdess6by.onion)

username: `streisand` password: `Plasseys-stains-aforetime-gastroenterologists` 
