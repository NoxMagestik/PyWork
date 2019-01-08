from tkinter import *
from random import *
window = Tk()
height = 900
width = 900
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen
turn = 1
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
totScore = 0
rollButton = Button(topFrame, text="Roll 1!", font=('helvetica', 20), height=3, width = 8, command=lambda:roll(), bg='red')
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
numButtons = []
specButtons = []
numLabels = []
specLabels = []
"""
Ones    
Twos
Threes
Fours
Fives
Sixes

"""
for i in range(6):
    numButtons.append(Button(leftFrame, font=otherFont, height=bHeight, width=bWidth, text=str(i + 1) + 's'))
    numButtons[-1].configure(command=lambda b=numButtons[-1]: score(b))
    numButtons[-1].grid(row=str(i), column='1', sticky='w')
    numLabels.append(Label(leftFrame, font=otherFont, height=bHeight, width=bWidth, text='0', bg='orange'))
    numLabels[-1].grid(row=str(i), column='2', sticky='w')
    if i == 0:
        specText = '3 of a kind'
    elif i == 1:
        specText = '4 of a kind'
    elif i == 2:
        specText = 'Full house'
    elif i == 3:
        specText = 'Small straight'
    elif i == 4:
        specText = 'Large straight'
    elif i == 5:
        specText = 'Yahtzee'
    specButtons.append(Button(leftFrame, font=otherFont, height=bHeight, width=bWidth, text=specText))
    specButtons[-1].configure(command=lambda b=specButtons[-1]: score(b))
    specButtons[-1].grid(row=str(i), column='3', sticky='w')
    specLabels.append(Label(leftFrame, font=otherFont, height=bHeight, width=bWidth, text='0', bg='orange'))
    specLabels[-1].grid(row=str(i), column='4', sticky='w')

specButtons.append(Button(leftFrame, font=otherFont, height=bHeight, width=bWidth, text='Chance'))
specButtons[-1].configure(command=lambda b=specButtons[-1]: score(b))
specButtons[-1].grid(row='6', column='3', sticky='w')
specLabels.append(Label(leftFrame, font=otherFont, height=bHeight, width=bWidth, text='0'))
specLabels[-1].grid(row='6', column='4', sticky='w')

def roll():
    global dice, turn, rollButton, canPlay
    turn += 1

    if turn > 4:


        canPlay = False
    else:
        canPlay = True
        if turn == 4:
            rollButton['text'] = 'Score!'
        else:
            rollButton['text'] = 'Roll ' + str(turn)
    if canPlay:
        for i in range(len(dice)):
            if dice[i - 1]['bg'] == 'orange':
                dice[i-1]['text'] = str(randint(1, 6))
    calculate()

def calculate():
    diceNum = [int(die1['text']), int(die2['text']), int(die3['text']), int(die4['text']), int(die5['text'])]
    for i in range(6):
        numLabels[i]['text'] = 'Possible Score: ' + str(diceNum.count(i + 1) * (i + 1))

def score(button):
    # calculate scores
    pass


def keep(button):
    if button['bg'] != 'green':
        button['bg'] = 'green'
    else:
        button['bg'] = 'orange'

window.mainloop()