
# Steps to use the VPN

This VPN is setup using [Streisand](https://github.com/StreisandEffect/streisand) on an AWS server in Oregan(US).

Streisand VPN Gateway contains step-by-step instructions for the services it provides, and mirrors of all necessary client software.

This document will show you how to connect to the Gateway to learn how to configure clients to use the Streisand services.

* * *
*   [Connecting to your Streisand Gateway](#connecting)
    *   [SSL](#connecting-ssl)
    *   [Tor Hidden Service](#connecting-tor)
*   [Fix Certificate error](#certificate)


<a name="connecting"></a>

## Connecting to your Streisand Gateway

<a name="connecting-ssl"></a>Each connection option takes you to the same place and you can use whichever one is most convenient for you. 

### SSL Service

Go to [https://35.166.238.146](https://35.166.238.146).

Note: You will get the error **Your connection is not private**, on that page click on `ADVANCED` and then click on `Proceed to 35.166.238.146 (unsafe)`.

Use username: `streisand` and password as : `short.trouble.captain.current.rate.thank` on the prompt.

Follow the instructions on the loaded webpage as per your choice.

Tip: If you're on Linux, using `Wireguard` is the best connection option. 
<a name="connecting-tor"></a>

### Tor Hidden Service

_All connections to Tor hidden services are fully encrypted._

[http://smri2p7xq7oeagu3.onion](http://smri2p7xq7oeagu3.onion)

Use username: `streisand` and password as: `short.trouble.captain.current.rate.thank`
Follow the instructions on the loaded webpage as per your choice.

<a name="certificate"></a>

## Fix Certificate error

To fix error **Your connection is not private** on opening [https://35.166.238.146](https://35.166.238.146), follow the instructions [here](https://github.com/abhigyank/sysadmin-solution/blob/master/Administration/certificate.html). 
