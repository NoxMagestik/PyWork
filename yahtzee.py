from tkinter import *
from random import *
window = Tk()
height = 900
width = 900
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (width/2)
y = (hs/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
topFrame = Frame(window)
topFrame.grid(row='1', column='1')
roll = Button(topFrame, text="Start!", font=('helvetica', 20), height=3, width = 8, command=lambda:roll(), bg='red')
roll.pack( side = LEFT )
die1 = Button(topFrame, text="", font=('helvetica', 20), height=3, width=8, command=lambda:keep(die1), bg='orange')
die1.pack(side = RIGHT)
die2 = Button(topFrame, text="", font=('helvetica', 20), height=3, width=8, command=lambda:keep(die3), bg='orange')
die2.pack(side = RIGHT)
die3 = Button(topFrame, text="", font=('helvetica', 20), height=3, width=8, command=lambda:keep(die3), bg='orange')
die3.pack(side = RIGHT)
die4 = Button(topFrame, text="", font=('helvetica', 20), height=3, width=8, command=lambda:keep(die4), bg='orange')
die4.pack(side = RIGHT)
die5 = Button(topFrame, text="", font=('helvetica', 20), height=3, width=8, command=lambda:keep(die5), bg='orange')
die5.pack(side = RIGHT)
dice = [die1, die2, die3, die4, die5]
clicks = 0
def roll():
    global dice
    for i in range(len(dice)):
        dice[i-1]['text'] = str(randint(1, 6))

def keep(button):
    pass

window.mainloop()