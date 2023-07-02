import os
import argparse
import subprocess
import threading
from timeit import default_timer as timer
from datetime import timedelta
from pyfiglet import Figlet
from termcolor import colored

custom_fig = Figlet(font='slant')
print(colored(custom_fig.renderText('ZEUS'),'green'))

print(colored('[#] Zeus v1.0 by ch3atk0d3','green'))
print(colored('[#] https://inventyourshit.com','green'))
print("\n")


start = timer()     # Initializing the program start time.

parser = argparse.ArgumentParser()

parser.add_argument("host", help="Enter the target",default=True)   # adding arguments.

args = parser.parse_args()

hostname = args.host


domain = hostname.split('.')[-1].isalpha()      # checking if the target is a domain or an ip. If it is domain, this will give True.
if domain is True:
    cmd = subprocess.check_output(f" nslookup {hostname} | awk -F': ' 'NR==6 {{ print $2 }} '", shell=True, encoding='utf-8').strip()  #convering domain to ip for masscan.
    cmd = str(cmd)
    scan = os.system(f'masscan {cmd} -p0-65534 --rate 3000 | tee log.txt')          # Using masscan on all ports and saving the result in text file for further analysis.
    os.system("cut -d ' ' -f 4 log.txt | grep -Eo '[0-9]{1,4}' > temp.txt")         # grepping out the port numbers and saving into temp.txt

else:
    scan = os.system(f'masscan {hostname} -p0-65534 --rate 3000 | tee log.txt')      # Using masscan on target ip
    os.system("cut -d ' ' -f 4 log.txt | grep -Eo '[0-9]{1,4}' > temp.txt")          # grepping out the port numbers and saving into temp.txt

def whatweb():
    print("\n")
    print("[+] Initializing Whatweb ")
    print("====================================")
    tech = os.system(f"whatweb {hostname}")


def nmap():
    print("\n")
    print("[+] Initializing Nmap Scan ")
    print("====================================")
    with open('temp.txt', 'r') as f: # opening up the temp file and to check the port numbers saved from the port scan.
        lines = f.readlines()
        # print(lines)
        lines = list(map(str.strip, lines))         # stripping out lines from the output
        mystr = ','.join(map(str, lines))           # joining the port numbers in different lines with a comma.
        # print(mystr)
        service = os.system(f"nmap -Pn -sV -sC -T4 -p {mystr} {hostname}")          # nmap service version detection and default script scan.

def gobuster():
    print("\n")
    print("[+] Initializing Gobuster Scan ")
    print("====================================")
    with open('temp.txt', 'r') as f: # opening up the temp file and to check the port numbers saved from the port scan.
        lines = f.readlines()
        if '80\n' in lines or '443\n' or '8080\n' in lines: #Checking for common web server ports
            os.system(f"gobuster dir -u http://{hostname} -w /home/wh1terose/Desktop/Wordlist/common.txt -t 15")    # gobuster directory scan with threads 20 using common.txt
        else:
            print("No Webserver Running !!!")



trd1 = threading.Thread(target=nmap())          #defining thread 1 running nmap function
trd2 = threading.Thread(target=whatweb())       #defining thread 2 running whatweb function
trd3 = threading.Thread(target=gobuster())      #defining thread 3 running gobuster function

trd1.start() # starting the thread 1
trd2.start() # starting the thread 2
trd3.start() # starting the thread 3

trd1.join() # wait until thread 1 is completely executed
trd2.join() # wait until thread 2 is completely executed
trd3.join() # wait until thread 3 is completely executed

os.system("rm log.txt temp.txt")    # clearing out the temporary files.

end = timer() #Program ending time.
print("Elpased time: ",timedelta(seconds=end-start)) #Displaying elapsed time









