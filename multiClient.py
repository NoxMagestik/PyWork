from tkinter import *
from random import *
import tkinter.messagebox
import socket
import selectors
sel = selectors.DefaultSelector()
import types
fPass = input("Please enter the first password")#
sPass = int(input("Please enter the second password"))

totScore = 0

def start_connections(host, port):
    server_addr = (host, port)
    
    connid = 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(server_addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    data = types.SimpleNamespace(connid=connid,
                                    outb=b'')
    sel.register(sock, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(2048)  # Should be ready to read
        if recv_data:
            print("received", repr(recv_data), "from connection", data.connid)
            
        """if not recv_data:
            print("closing connection", data.connid)
            sel.unregister(sock)
            sock.close()"""
    if mask & selectors.EVENT_WRITE:
        if not data.outb:
            data.outb = totScore.to_bytes(2, byteorder='big')
        if data.outb:
            print("sending", repr(data.outb), "to connection", data.connid)
            sent = sock.sendall(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]

start_connections(fPass, sPass)
events = sel.select(timeout=1)
for i in range(2):
    events = sel.select(timeout=1)
    if events:
        for key, mask in events:
            service_connection(key, mask)