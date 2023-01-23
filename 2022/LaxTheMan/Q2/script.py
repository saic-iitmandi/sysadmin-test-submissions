#!/usr/bin/python3

"""
Three files will be modified
1) /etc/apt/apt.conf
2) /etc/environment
3) /etc/bash.bashrc
"""

import os
from dotenv import load_dotenv
load_dotenv()

proxy = os.environ['proxy']
port = os.environ['port']
proxy_ssid = os.environ['proxy_ssid']
gateway_username = os.environ['gateway_username']
gateway_password = os.environ['gateway_password']

apt_ = r'/etc/apt/apt.conf'
bash_ = r'/etc/bash.bashrc'
env_ = r'/etc/environment'

# This function directly writes to the apt.conf file


def writeToApt(flag):
    filepointer = open(apt_, "w")
    if flag:
        filepointer.write(
            'Acquire::http::proxy "http://{0}:{1}/";\n'.format(proxy, port))
        filepointer.write(
            'Acquire::https::proxy  "http://{0}:{1}/";\n'.format(proxy, port))
        filepointer.write(
            'Acquire::ftp::proxy  "ftp://{0}:{1}/";\n'.format(proxy, port))
        filepointer.write(
            'Acquire::socks::proxy  "socks://{0}:{1}/";\n'.format(proxy, port))
    filepointer.close()

# This function writes to the environment file
# Fist deletes the lines containng http:// , https://, ftp://


def writeToEnv(flag):
    # find and delete line containing http://, https://, ftp://
    with open(env_, "r+") as opened_file:
        lines = opened_file.readlines()
        opened_file.seek(0)  # moves the file pointer to the beginning
        for line in lines:
            if r"http://" not in line and r"https://" not in line and r"ftp://" not in line and r"socks://" not in line:
                opened_file.write(line)
        opened_file.truncate()

    # writing starts
    if flag:
        filepointer = open(env_, "a")
        filepointer.write(
            'http_proxy="http://{0}:{1}/"\n'.format(proxy, port))
        filepointer.write(
            'https_proxy="http://{0}:{1}/"\n'.format(proxy, port))
        filepointer.write(
            'ftp_proxy="ftp://{0}:{1}/"\n'.format(proxy, port))
        filepointer.write(
            'socks_proxy="socks://{0}:{1}/"\n'.format(proxy, port))
        filepointer.close()


def writeToBashrc(flag):
    # find and delete http:// , https://, ftp://
    with open(bash_, "r+") as opened_file:
        lines = opened_file.readlines()
        opened_file.seek(0)
        for line in lines:
            if r"http://" not in line and r'"https://' not in line and r"ftp://" not in line and r"socks://" not in line and "unset http_proxy" not in line and "unset https_proxy" not in line and "unset ftp_proxy" not in line:
                opened_file.write(line)
        opened_file.truncate()

    # writing starts
    filepointer = open(bash_, "a")
    if flag:
        filepointer.write(
            'export http_proxy="http://{0}:{1}/"\n'.format(proxy, port))
        filepointer.write(
            'export https_proxy="http://{0}:{1}/"\n'.format(proxy, port))
        filepointer.write(
            'export ftp_proxy="ftp://{0}:{1}/"\n'.format(proxy, port))
        filepointer.write(
            'export socks_proxy="socks://{0}:{1}/"\n'.format(proxy, port))
    else:
        filepointer.write(
            'unset http_proxy\nunset https_proxy\nunset ftp_proxy')
    filepointer.close()
 


def change_proxy(flag):
    if flag:
        print("Setting Proxy")
    else:
        print("Removing Proxy")

    writeToApt(flag)
    writeToEnv(flag)
    writeToBashrc(flag)


def shouldSetProxy():
    import subprocess
    import re
    try:
        iwgetid_output = subprocess.check_output('iwgetid').decode()
        network_ssid = re.findall(
            'ESSID:"(.*)"', iwgetid_output)[0].replace(" ", "")
        if network_ssid == proxy_ssid:
            return True
    except:
        return False
    return False


if __name__ == "__main__":
    change_proxy(shouldSetProxy())
    print("DONE!")
