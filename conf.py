#! /usr/bin/env python3
import socket
import shutil
import os
from ftp_server import *


def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("Your Computer Name is: " + hostname)
    return ip


def check_drives():
    #drives = ['sda1', 'sdb1', 'sdc1', 'sdd1']
    drives = ['C:']
    ext_drives = []
    for drive in drives:
        path = drive #"/mnt/media/" + drive
        try:
            directory = os.listdir(path)
            if directory is not None:
                ext_drives.append(drive)
        except:
            pass
    return ext_drives


def set_drive():
    drives = os.listdir('/dev/')
    for part in drives:
        if "sda1" in part or "sdb1" in part or "sdc1" in part:
            command = 'sudo mount /dev/' + part + ' /mnt/media/' + part
            os.system(command)


def get_drive(drive):
    path = "/mnt/media/" + drive
    drive_content = os.listdir(path)
    return drive_content


def get_into_drive_dir(drive):
    path = "/mnt/media/" + drive
    os.chdir(path)


def get_into_drive_shell(drive):
    path = "/mnt/media/" + drive
    os.chdir(path)
    os.system("pwd")
    os.system("/bin/bash")


def get_drive_info(drives):
    total, used, free = [], [], []

    for drive in drives:
        l = len(drive) - 1
        #path = "/dev/ " + drive[:l]
        path = drive
        total.append(shutil.disk_usage(path)[0] // (2 ** 30))
        used.append(shutil.disk_usage(path)[1] // (2 ** 30))
        free.append(shutil.disk_usage(path)[2] // (2 ** 30))

    return total, used, free


def start_ftp(hdd, name, password):
    user = FTP_main(hdd, name, password)
    user.start_ftp()


# postavi da se drive mounta svaki put kad se rpi upali - prvo provjeri jel treba
# napravi da se pokaze slobodni prostor na diskovima
