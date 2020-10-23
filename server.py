import socket
from threading import Thread
from socketserver import ThreadingMixIn
import time
import os
from main_node import *


TCP_IP = '192.168.1.6'
TCP_PORT = 9001
BUFFER_SIZE = 4096

logs = open('connection_log.txt', 'a+')


class ClientThread(Thread):
    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        self.state = "on"
        logs.write(time.asctime(time.localtime()))
        logs.write(" New thread started for " + ip + ":" + str(port) + "\n")
        logs.write("\n")

    def send(self, msg):
        self.sock.send(msg)
        self.sock.close()

    def receive(self):
        data = self.sock.recv(BUFFER_SIZE).decode()
        #print("Msg received: " + str(data))
        if data == "start_con":
            #got_client()
            print(data)
        elif data == "end_con":
            self.state = "off"
            print(data)


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []
state = "on"


while state == "on":
    tcpsock.listen(5)
    (conn, (ip, port)) = tcpsock.accept()
    logs.write('Got connection from ' + str(ip) + " " + str(port))
    newthread = ClientThread(ip, port, conn)
    newthread.send(b"connection_started")
    newthread.receive()
    if newthread.state == "off":
        newthread.send(b"connection_stopped")
        time.sleep(5000)
        break
# napravi provjeru da se ugasi socket server


logs.close()
