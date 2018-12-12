from tkinter import *
from random import *
window = Tk()
height = 900
width = 900
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen
turn = 0
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (width/2)
y = (hs/2) - (height/2)
myFont = ('helvetica', 20)
otherFont = ('helvetica', 15)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
bHeight = 2
bWidth = 18
topFrame = Frame(window)
topFrame.grid(row='1', column='2')
botFrame = Frame(window)
botFrame.grid(row='2', column='2')
leftFrame = Frame(botFrame)
leftFrame.grid(row='1', column='1')
rightFrame = Frame(botFrame)
rightFrame.grid(row='1', column='3')
rollButton = Button(topFrame, text="Start!", font=('helvetica', 20), height=3, width = 8, command=lambda:roll(), bg='red')
rollButton.pack( side = LEFT )
die1 = Button(topFrame, text="", font=myFont, height=3, width=8, command=lambda:keep(die1), bg='orange')
die1.pack(side = RIGHT)
die2 = Button(topFrame, text="", font=myFont, height=3, width=8, command=lambda:keep(die2), bg='orange')
die2.pack(side = RIGHT)
die3 = Button(topFrame, text="", font=myFont, height=3, width=8, command=lambda:keep(die3), bg='orange')
die3.pack(side = RIGHT)
die4 = Button(topFrame, text="", font=myFont, height=3, width=8, command=lambda:keep(die4), bg='orange')
die4.pack(side = RIGHT)
die5 = Button(topFrame, text="", font=myFont, height=3, width=8, command=lambda:keep(die5), bg='orange')
die5.pack(side = RIGHT)
dice = [die1, die2, die3, die4, die5]
clicks = 0
canPlay = True
B_1 = Button(leftFrame, text='Ones', font=otherFont, height=bHeight, width=bWidth, command=lambda:score(B_1))
B_1.grid(row='1', column='1')
L_1 = Label(leftFrame, text="0", font=otherFont, height=bHeight, width=bWidth)
L_1.grid(row='1', column='2')

B_3OfKind = Button(rightFrame, text='Three of a kind', font=otherFont, height=bHeight, width=bWidth, command=lambda:score(B_3OfKind))
B_3OfKind.grid(row='1', column='1')
def roll():
    global dice, turn, rollButton, canPlay
    turn += 1
    if turn >= 4:
        rollButton['text'] = 'Score!'

        canPlay = False
    else:
        canPlay = True
        rollButton['text'] = 'Roll ' + str(turn)
    if canPlay:
        for i in range(len(dice)):
            if dice[i - 1]['bg'] == 'orange':
                dice[i-1]['text'] = str(randint(1, 6))


def score(button):
    pass


def keep(button):
    if button['bg'] != 'green':
        button['bg'] = 'green'
    else:
        button['bg'] = 'orange'

window.mainloop()