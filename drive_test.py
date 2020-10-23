#! /usr/bin/python3

import os
import win32api

#os.chdir('D:')
#print(os.listdir())



drives = open('/dev/', 'r')
print(drives)

def finddrives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    print(drives)

finddrives()

'''
def opendrives():
    path = "C:/Users"
    path = os.path.realpath(path)
    os.startfile(path)
'''

#os.system("sudo service apache2 restart ")

def finddrives():
    path = os.pardir("media")
    for name in ['sda', 'sdb', 'sdc', 'sdd']:
        os.listdir("/path/" + name) #???

# this works in linux
import os

drives = os.listdir('/dev/')
for part in drives:
    if "sda1" in part or "sdb1" in part or "sdc1" in part:
        print(part)
        path = "/mnt/media/" + part
        os.chdir(path)
        os.system("pwd")
        os.system("/bin/bash")


