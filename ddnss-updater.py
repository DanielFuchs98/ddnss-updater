#!/usr/bin/python3

import urllib.request
import re

hostname = "fill_here"
apikey = "fill_here"

print("start ddnss-updater")


def getMyIP():
    url = "https://ip4.ddnss.de/meineip.php"

    req = urllib.request.urlopen(url)
    if req.getcode() == 200:
        resp = req.read()
        match = re.search(
            "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", str(resp))
        return match.group()


def setLastIP(ip):
    f = open("last_ip.txt", "w")
    f.write(ip)
    f.close()


def updateIP(ip):
    req = urllib.request.urlopen(
        "https://ddnss.de/upd.php?key="+apikey+"&host=" + hostname)
    print(req.read())


def getLastIPSet():
    f = open("last_ip.txt", "r")
    val = f.read()
    f.close()
    return val


last_ip = getLastIPSet()
current_ip = getMyIP()

if last_ip != current_ip:
    print("need to update ip")
    updateIP(current_ip)
    setLastIP(current_ip)
else:
    print("no need to update")
