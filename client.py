# napravi paket za client app
import socket

TCP_IP = '192.168.1.6'
TCP_PORT = 9001
BUFFER_SIZE = 4096


def setup():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    return s


def recv_data():
    s = setup()
    data = s.recv(BUFFER_SIZE)
    data.decode()
    s.close()
    return data


def send_data(snd_data):
    s = setup()
    data = snd_data.encode()
    s.send(data)
    s.close()
