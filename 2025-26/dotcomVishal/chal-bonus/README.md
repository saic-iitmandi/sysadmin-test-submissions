In this challenge, I was asked to design a stealthy remote access tunnel between two machines using only raw network communication, while keeping Windows Defender fully enabled and unchanged. The Windows 11 machine had to initiate the connection and provide an interactive shell-like experience over sockets.

Before starting, I already felt that the constraints were extremely strict, because modern Windows security is specifically designed to detect exactly this kind of behavior. So my approach was not only to try building the tunnel, but also to understand why it fails, and what that teaches about Windows internals and endpoint security.

Initial Architecture Idea

My original idea was:

Use a Linux system (inside WSL2) as the command controller.

Let the Windows 11 target initiate a reverse connection.

Exchange commands and outputs manually over sockets.

Avoid any built-in remote administration tools.

This was meant to simulate a minimal command-and-control tunnel using only basic networking concepts.

The First Major Problem – Networking Topology

I quickly discovered that WSL2 does not live on the same network as the Wi-Fi adapter. It runs behind a virtual NAT network.

This taught me:

The Linux IP (172.x.x.x) is invisible to devices on the hotspot (10.x.x.x).

Even though both are on the same laptop, they are on different network layers.

Only the Windows host is visible to the external network.

From this, I understood that virtualized environments must be treated as separate trust zones.

I solved this conceptually by reasoning that the Windows host itself must act as a bridge between the physical network and the WSL environment. This was my first major learning moment about real-world networking design.