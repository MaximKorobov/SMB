# SMB
Utility for fast **s**wap **m**ouse **b**uttons on Windows OS.

# Motivation

I'm 35 years old. After some time small a pain appear in my right hand's wrist. Sounds similar to [Carpal tunnel syndrome](https://en.wikipedia.org/wiki/Carpal_tunnel_syndrome).

To solve it I started to use left hand more often in daily activity - rotating my car's wheel, clean up the nose and so on.

Using left hand when working on PC is solution too. Especially if one have universal (symmetrical) mouse.

But this doesn't work when playing games. CS:GO, Tank Force and others were created to play using mouse on a right hand.

So one should change default mouse action button in Windows OS settings few times a day. To speed up it I wrote SMB utility. Setting could be changed within one click. Simple as it should be.

# FAQ

## Q: why so small and simple utility has so big (8 megabytes) executable?
A: I know that on pure C++ it's size could be less that a 64 kilobytes. That is how Python + [pyinstaller](https://pyinstaller.org) work together. Patches are welcome to improve the numbers. 

## Q: why did you use pure Python without Qt?
A: there are some reasons:
1. I'm in Moscow, Russian Federation
2. Russian government started some military actions in February of 2022
3. Since then [Qt is not available for Russian IPs](https://forum.qt.io/topic/134724/unlock-qt-in-russia)
4. [Roskomnadzor](https://en.wikipedia.org/wiki/Roskomnadzor) (Federal Service for Supervision of Communications, Information Technology and Mass Media) blocked Windscribe, ProtonVPN and other popular VPN services
5. I didn't find option to download Qt SDK using torrents

## Q: How to build executable by myself?
A: install [pyinstaller](https://pyinstaller.org/en/stable/installation.html), then execute command in system console:
```
pyinstaller <your project's folder>\SMB\smb.py --onefile --noconsole
```
