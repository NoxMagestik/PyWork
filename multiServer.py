from tkinter import *
from random import *
import tkinter.messagebox
import socket
import random as r
import selectors
import types
import time
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Defines the server with the protocol thing
MY_IP = socket.gethostbyname(socket.gethostname())
PORT = r.randint(10000, 35000)
sel = selectors.DefaultSelector()

window = Tk()
window.config(bg='white')
increment = 0
height = 900
width = 900
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen
x = (ws/2) - (width/2)
y = (hs/2) - (height/2)
otherFont = ('helvetica', 15)
bHeight = 2
bWidth = 30
fPasswordLabel = Label(window, font=otherFont, height=bHeight, width=bWidth, text='The first password is ' + MY_IP, bg='white', foreground="red")
fPasswordLabel.grid(row='1', column='1', sticky='w')
sPasswordLabel = Label(window, font=otherFont, height=bHeight, width=bWidth, text='The second password is ' + str(PORT), bg='white', foreground="red")
sPasswordLabel.grid(row='2', column='1', sticky='w')
playerLabels = []
banner = Label(window, font=otherFont, height=bHeight, width=bWidth, text='Players:', bg='white', foreground="red")
banner.grid(row='3', column='1', sticky='w')
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
cRow = 4
serverRunning = True  # Just a variable to say serverRunning is True
server.bind((MY_IP, PORT))
server.listen(50)
server.setblocking(False)
sel.register(server, selectors.EVENT_READ, data=None)
window.update()


def accept_wrapper(sock):
    global playerLabels
    conn, addr = sock.accept()  # Should be ready to read
    playerLabels.append(Label(window, font=otherFont, height=bHeight, width=bWidth, text='{}'.format(addr), bg='white', foreground="red"))
    playerLabels[-1].grid(row=str(cRow), column='1', sticky='w')
    window.update()
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(2048)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing', repr(data.outb), 'to', data.addr)
            sent = sock.sendall(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]


while serverRunning is True:  # loop
    # client, address = server.accept()  # When clients attempt to join, they it takes their info as client, address
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connection(key, mask)
    increment += 1

    cRow += 1
    window.update()