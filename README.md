# Zeus
Zeus is a CTF enumeration tool built in Python that automates the use common of enumeration and scanning tools and minimize the recon time significantly.

The script is built in Python3 and is an attempt to make enumeration faster. 

**Why i made Zeus?**

While solving the rooms from Tryhackme, i was strugling with the speed of Nmap. I could have used some alternatives for port scanning but i have to fall back to Nmap for other service version and NSE scans. So, i just made a custom script taking input ip address or domain as an input and using following tools to enumerate.

- Masscan - For port scanning
- Nmap - Use the ports from Masscan output to run a service version and default script scan on them.
- Gobuster - If any commmon web server port port like 80,443,8080 is found. The script will fire up gobuster on it.


**Installation**

```
git clone https://github.com/ch3atk0d3/Zeus.git
cd Zeus
chmod +x install.sh
sudo ./install.sh

```

**Note**

- Specify the wordlist path for gobuster manually for now. Will update the argument for the same in the next iteration.


**Follow on**

- Invent Your Shit - https://inventyourshit.com/
