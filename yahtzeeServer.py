from tkinter import *
from random import *
import tkinter.messagebox
import socket
import random as r
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Defines the server with the protocol thing
MY_IP = socket.gethostbyname(socket.gethostname())
PORT = r.randint(10000, 35000)
window = Tk()
window.config(bg='white')
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
server.listen(30)
window.update()
while serverRunning is True:  # loop
    client, address = server.accept()  # When clients attempt to join, they it takes their info as client, address
    playerLabels.append(Label(window, font=otherFont, height=bHeight, width=bWidth, text='{}'.format(address), bg='white', foreground="red"))
    playerLabels[-1].grid(row=str(cRow), column='1', sticky='w')
    cRow += 1
    window.update()



