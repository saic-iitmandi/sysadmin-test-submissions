# Setup process to connect to VPN

## For those who want to connect by L2TP/IPsec (nativey supported by macOS, iOS, Android, Windows):

### Windows 10
1. Click on the Start Menu and open Settings by typing "Settings".
2. Click on Network & Internet.
3. Click on VPN.
4. Click on Add a VPN connection.
5. Select Windows (built­in) for the VPN provider field.
6. Enter `saitarunreddy` in the Connection name field (or any other name you want the VPN to be stored as).
7. Enter `13.126.113.201` in the Server name or address field.*
8. Select `L2TP/IPsec` with pre­shared key for the VPN type field.
9. Enter `reciprocalitys‐basenjis‐Robson` for the Pre­shared key.
10. Select User name and password for the Type of sign­in info field.
11. Enter `streisand` in the User name field.
12. Enter `Sasquatchs‐corbiestep` in the Password field.
13. Check the Remember my sign­in info box.
14. Click Save.
15. Click Connect.

### macOS
1. Open System Preferences and go to the Network section.
2. Click the `+` button in the lower-left corner of the window.
3. Select `VPN` from the Interface drop-down menu.
4. Select `L2TP over IPSec` from the VPN Type drop-down menu.
5. Enter `saitarunreddy` for the Service Name (or any other name you want the VPN to be stored as).
6. Click Create.
7. Enter `13.126.113.201` for the Server Address.*
8. Enter `streisand` for the Account Name.
9. Click the Authentication Settings button.
10. In the User Authentication section, select the Password radio button and enter `Sasquatchs‐corbiestep` as its value.
11. In the Machine Authentication section, select the Shared Secret radio button and enter `reciprocalitys‐basenjis‐Robson` as its value.
12. Click OK.
13. Check the Show VPN status in menu bar checkbox.
14. Click the Advanced button and make sure the Send all traffic over VPN connection checkbox is selected.
15. Click the TCP/IP tab, and make sure Link­local only is selected in the Configure IPv6 section.
16. Click OK to close the Advanced settings, and then click Apply to save the VPN connection information.
17. To connect to this VPN use the VPN icon in the menu bar or open Network in System Preferences, click on the Streisand entry in the list of connections. There's a Connect button there.

### Android
1. Launch the Settings application.
2. Tap More... in the Wireless & Networks section.
3. Tap `VPN`.
4. Tap the `+` icon in the top-right of the screen.
5. Enter `saitarunreddy` in the Name field (or any other name you want the VPN to be stored as).
6. Select `L2TP/IPSec PSK` in the Type drop-down menu.
7. Enter `13.126.113.201` in the Server address field.*
8. Enter `reciprocalitys‐basenjis‐Robson` in the IPSec pre­shared key field.
9. Tap Save.
10. Tap the saitarunreddy connection.
11. Enter `streisand` in the Username field.
12. Enter `Sasquatchs‐corbiestep` in the Password field.
13. Check the Save account information checkbox.
14. Tap Connect.

### iOS
1. Go to Settings -> General -> VPN.
2. Tap Add VPN Configuration....
3. Tap Type.
4. Select `L2TP` and go back.
5. Tap Description and enter `saitarunreddy` (or any other name you want the VPN to be stored as).
6. Tap Server and enter `13.126.113.201` .*
7. Tap Account and enter `streisand` .
8. Tap Password and enter `Sasquatchs‐corbiestep` .
9. Tap Secret and enter `reciprocalitys‐basenjis‐Robson` .
10. Tap Done.
11. To activate the VPN, go to Settings -> General -> VPN.
12. Slide the VPN switch on.

### Others
For all other operating systems and any other type of connection services like OpenVPN, OpenSSH, Shadowsocks, Tor, OpenConnect, etc.
Install the required softwares and use these credentials to connect to VPN:
> Name of the VPN: `saitarunreddy` (or any other name you want the VPN to be stored as) <br />
> Server Address*: `13.126.113.201` <br />
> Pre‐shared key or PSK: `reciprocalitys‐basenjis‐Robson` <br />
> CHAP authentication username: `streisand` <br />
> CHAP authentication password: `Sasquatchs‐corbiestep` <br />

*The server's IP address can change, please confirm the server's IP address with the me before connecting.
