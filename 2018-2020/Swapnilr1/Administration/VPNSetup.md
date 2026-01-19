<b>I am running my VPN on Amazon Web Services (AWS) Mumbai datacentre. </b>

IP address: 13.127.167.195

In case you want to open the home page for the VPN, the credentials are:

username: `streisand`

password: `base.height.tragic.pink.select.six`

You will need to either

1. Install a SSL certificate and then go to the above IP address via a browser. The certificate is embedded in the HTML page whose link is given below. There is a hyperlink in the HTML page from where you can install the certificate.

2. Go to the IP address and the browser will give show a security warning which you need to ignore (and probably add some exception) and continue to the webpage. 

These credentials as well as steps to install the certificate and the embedded certificate is contained in [streisand.html](streisand.html)
(open the page in "Raw" View and save the page using the browser as an HTML file, then open the HTML page)

Once you have accessed https://13.127.167.195/ the ways of connecting to the VPN along with instructions for every platform are shown. 

I have used `OpenVPN` (without `stunnel`)and tested my VPN on Windows and Android.

Instructions for configuring OpenVPN are available at https://13.127.167.195/openvpn/ (I used the `festival-clerk` profile).

<b>NOTE: Only one device can be connected at a time to the VPN. </b>


