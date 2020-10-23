#! /usr/bin/env python3
import tkinter as tk
import socket
from client_conf import *


# socket data
TCP_IP = '192.168.1.6'
TCP_PORT = 9001
BUFFER_SIZE = 4096


# GUI App
window = tk.Tk()
window.title("PiNAS App")
window.geometry('400x400')


def send_start():
    label0.config(text="Connection starting...")
    s.send(b"start")
    s.send(get_ip().encode())

    #label0.config(text="Connection failed! Try again!")
    # napravi da se moze ponovno pokrenuti socket server na webu
    # napravi da se moze primiti poruka


def send_stop():
    label0.config(text="Connection stopping...")


def receive_msg():
    while msg:
        msg = s.recv(BUFFER_SIZE)
    return msg.decode()


frame0 = tk.Frame(window, width=400, height=4)
label0 = tk.Label(frame0, width=400, height=4, text="Idle", bg='white', fg='black', font='bold')
label0.pack()
frame0.pack()

frame1 = tk.Frame(window, width=400, height=100)
button1 = tk.Button(frame1, width=400, height=6, bg='black', fg='white', font='bold', text='Start', command=send_start)
button1.pack()
frame1.pack()

frame2 = tk.Frame(window, width=400, height=100)
button2 = tk.Button(frame1, width=400, height=6, bg='black', fg='white', font='bold', text='Stop', command=send_stop)
button2.pack()
frame2.pack()


# start connection
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
    except:
        label0.config(text="Waiting for connection...")
    finally:
        break

window.mainloop()
