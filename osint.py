#!/usr/bin/env python3

from argparse import ArgumentParser
import requests
from time import time, sleep
import re

ap = ArgumentParser()
ap.add_argument('-e', '--email', required=False, help='Email Address You Want to Test')
ap.add_argument('-f', '--file', required=False, help='Load a File with Multiple Email Addresses')
ap.add_argument('-fp', '--filepawned', required=False, help='Output file for pawned mail addresses')
ap.add_argument('-d', '--domain', required=False, help='Filter Results by Domain Name')
ap.add_argument('-b', '--breach', required=False, help='Get Info about breach')
ap.add_argument('-n', '--nodumps', required=False, action='store_true', help='Only Check Breach Info and Skip Password Dumps')
ap.add_argument('-l', '--list', required=False, action='store_true', help='Get List of all pwned Domains')
ap.add_argument('-c', '--check', required=False, help='Check if your Domain is pwned')
arg = ap.parse_args()
addr = arg.email
file = arg.file
filepawned = arg.filepawned
domain = arg.domain
breach_name = arg.breach
nodumps = arg.nodumps
list_domain = arg.list
check_domain = arg.check

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow

version = '1.3.0.1'

key = ''
useragent = ''
start = ''
idle_time = 1.6

if "HOME" in environ:
    home = getenv('HOME')
if "USERPROFILE" in environ:
    home = getenv('USERPROFILE')
conf_path = path.join(home, '.config', 'pwnedornot', 'config.json')

# ... (remaining existing code)

def extract_username(email):
    match = re.match(r'(.*)@', email)
    if match:
        return match.group(1)
    else:
        return None

def main():
    global addr, start
    start = time()

    banner()
    read_config()

    extracted_username = extract_username(addr)

    if filepawned is not None and path.exists(filepawned):
        remove(filepawned)

    if list_domain is True:
        domains_list()
    elif check_domain:
        domain_check()
    elif breach_name:
        breach_info()
    elif addr is not None and domain is not None:
        filtered_check(extracted_username)
    elif addr is not None and domain is None:
        check(extracted_username)
    elif file is not None and domain is None:
        print(f'{G}[+] {C}Reading Emails Addresses from {W}{file}\n')
        with open(file) as dict:
            for line in dict:
                line = line.strip()
                addr = line
                if addr != '':
                    check(extracted_username)
                    sleep(idle_time)
    elif file is not None and domain is not None:
        print(f'{G}[+] {C}Reading Emails Addresses from {W}{file}\n')
        print(f'{G}[+] {C}Domain : {W}{domain}')
        with open(file) as dict:
            for line in dict:
                line = line.strip()
                addr = line
                if addr != '':
                    filtered_check(extracted_username)
                    sleep(idle_time)
    else:
        print(f'{R}[-] {C}Error : {W}At least 1 Argument is Required, Try : {G}python3 pwnedornot.py -h{W}')
        exit()

# ... (remaining existing code)

if __name__ == "__main__":
    main()
    quit()
else:
    pass
