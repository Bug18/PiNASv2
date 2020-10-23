#! /usr/bin/env python3
import socket


def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip
