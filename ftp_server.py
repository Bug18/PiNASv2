#! /usr/bin/env python3

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class FTP_main:
    IP = '192.168.1.80'
    FTP_PORT = 21

    def __init__(self, hdd, name, password):
        self.FTP_USER = name
        self.FTP_PASSWORD = password
        self.FTP_DIRECTORY = bytes('/mnt/media/' + hdd)
        self.authorizer = DummyAuthorizer()
        self.authorizer.add_user(self.FTP_USER, self.FTP_PASSWORD, self.FTP_DIRECTORY, perm='elradfmw')

    def start_ftp(self, IP, FTP_PORT):
        self.handler = FTPHandler
        self.handler.authorizer = self.authorizer
        self.handler.max_login_attempts = 5
        self.handler.banner = "FTP ready..."
        self.handler.passive_ports = range(60000, 65535)
        address = (IP, FTP_PORT)
        self.server = FTPServer(address, self.handler)
        self.server.max_cons = 128
        self.server.max_cons_per_ip = 5

        self.server.serve_forever()

