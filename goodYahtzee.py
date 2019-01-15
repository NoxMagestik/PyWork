from tkinter import *
from random import *
import tkinter.messagebox
window = Tk()
height = 900
width = 900
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen
turn = 1
yCount = 0
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (width/2)
y = (hs/2) - (height/2)
myFont = ('helvetica', 20)
otherFont = ('helvetica', 15)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
bHeight = 2
bWidth = 18
bgcolour = 'black'
bColour = 'grey'
topFrame = Frame(window)
topFrame.configure(bg=bgcolour)
topFrame.grid(row='1', column='2')
botFrame = Frame(window)
botFrame.grid(row='2', column='2')
botFrame.configure(bg=bgcolour)
leftFrame = Frame(botFrame)
leftFrame.grid(row='1', column='1')
leftFrame.configure(bg=bgcolour)
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
    numButtons.append(Button(leftFrame, font=otherFont, height=bHeight, width=bWidth, text=str(i + 1) + 's', bg=bColour))
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
    specButtons.append(Button(leftFrame, font=otherFont, height=bHeight, width=bWidth, text=specText, bg=bColour))
    specButtons[-1].configure(command=lambda b=specButtons[-1]: score(b))
    specButtons[-1].grid(row=str(i), column='3', sticky='w')
    specLabels.append(Label(leftFrame, font=otherFont, height=bHeight, width=bWidth, text='0', bg='orange'))
    specLabels[-1].grid(row=str(i), column='4', sticky='w')

specButtons.append(Button(leftFrame, font=otherFont, height=bHeight, width=bWidth, text='Chance', bg=bColour))
specButtons[-1].configure(command=lambda b=specButtons[-1]: score(b))
specButtons[-1].grid(row='6', column='3', sticky='w')
specLabels.append(Label(leftFrame, font=otherFont, height=bHeight, width=bWidth, text='0', bg='orange'))
specLabels[-1].grid(row='6', column='4', sticky='w')
# total score label 1
specLabels.append(Label(leftFrame, font=otherFont, height=bHeight, width=bWidth, text='Total Score:', bg='black', foreground="yellow"))
specLabels[-1].grid(row='7', column='3', sticky='w')
# total score label 2
specLabels.append(Label(leftFrame, font=otherFont, height=bHeight, width=bWidth, text=str(totScore), bg='black', foreground="red"))
specLabels[-1].grid(row='7', column='4', sticky='w')
upperScore = 0
# upper score
numLabels.append(Label(leftFrame, font=otherFont, height=bHeight, width=bWidth, text='Upper Score:', bg='black', foreground='yellow'))
numLabels[-1].grid(row='6', column='1', sticky='w')
numLabels.append(Label(leftFrame, font=otherFont, height=bHeight, width=bWidth, text=str(upperScore), bg='black', foreground='red'))
numLabels[-1].grid(row='6', column='2', sticky='w')
# bonus
numLabels.append(Label(leftFrame, font=otherFont, height=bHeight, width=bWidth, text='Bonus:', bg='black', foreground='yellow'))
numLabels[-1].grid(row='7', column='1', sticky='w')
numLabels.append(Label(leftFrame, font=otherFont, height=bHeight, width=bWidth, text='0', bg='black', foreground='red'))
numLabels[-1].grid(row='7', column='2', sticky='w')

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
            if dice[i]['bg'] == 'orange':
                dice[i]['text'] = str(randint(1, 6))
    calculate()

def calculate():
    global yCount, upperScore, totScore
    found = False
    count = 0
    total = 0
    diceNum = [int(die1['text']), int(die2['text']), int(die3['text']), int(die4['text']), int(die5['text'])]
    diceNum.sort()
    specButtons[5]['state'] = 'normal'
    for i in range(6):
        if numLabels[i]['bg'] != 'red':
            numLabels[i]['text'] = str(diceNum.count(i + 1) * (i + 1))

    # check for three of a kind
    if specLabels[0]['bg'] == 'orange':
        for i in range(6):
            count = diceNum.count(i + 1)
            if count >= 3:
                total = 0
                for j in range(5):
                    total += diceNum[j]
                specLabels[0]['text'] = str(total)
                found = True
                break
        if found == True:
            pass
        else:
            specLabels[0]['text'] = 0


    # check for four in a kind
    if specLabels[1]['bg'] == 'orange':
        for i in range(6):
            count = diceNum.count(i + 1)
            if count >= 4:
                total = 0
                for j in range(5):
                    total += diceNum[j]
                specLabels[1]['text'] = str(total)
                found = True
        if found == True:
            pass
        else:
            specLabels[1]['text'] = 0

    # check for full house
    if specLabels[2]['bg'] == 'orange':
        if diceNum[0] == diceNum[1] == diceNum[2]:
            checked = diceNum[0]
            if diceNum[3] == diceNum[4] and diceNum[3] != checked:
                specLabels[2]['text'] = str(25)
        elif diceNum[2] == diceNum[3] == diceNum[4]:
            checked = diceNum[2]
            if diceNum[0] == diceNum[1] and diceNum[0] != checked:
                specLabels[2]['text'] = str(25)
        else:
            specLabels[2]['text'] = str(0)

    # check for small straight
    works = True
    straightNum = [int(die1['text']), int(die2['text']), int(die3['text']), int(die4['text']), int(die5['text'])]
    if specLabels[3]['bg'] == 'orange':
        for i in range(4):
            if diceNum[i] == diceNum[i + 1]:
                works = False
                del(straightNum[i])
                break
            else:
                pass
        if straightNum[0] == straightNum[1] - 1 == straightNum[2] - 2 == straightNum[3] - 3:
            specLabels[3]['text'] = str(30)
        elif works == True and straightNum[1] == straightNum[2] - 1 == straightNum[3] - 2 == straightNum[4] - 3:
            specLabels[3]['text'] = str(30)
        else:
            specLabels[3]['text'] = str(0)

    # check for large straight
    if specLabels[4]['bg'] == 'orange':
        if diceNum[0] == diceNum[1] - 1 == diceNum[2] - 2 == diceNum[3] - 3 == diceNum[4] - 4:
            specLabels[4]['text'] = str(40)
        else:
            specLabels[4]['text'] = str(0)

    # check for yahtzee
    if yCount != 0:
        if diceNum[0] == diceNum[1] == diceNum[2] == diceNum[3] == diceNum[4]:
            specLabels[5]['text'] = str(100)
            yCount += 1
        else:
            specButtons[5]['state'] = 'disabled'
            specLabels[5]['text'] = str(0)
    else:
        if diceNum[0] == diceNum[1] == diceNum[2] == diceNum[3] == diceNum[4]:
            specLabels[5]['text'] = str(50)
            yCount += 1
        else:
            specLabels[5]['text'] = str(0)
            specButtons[5]['state'] = 'disabled'
    # chance
    if specLabels[6]['bg'] == 'orange':
        specLabels[6]['text'] = str(diceNum[0] + diceNum[1] + diceNum[2] + diceNum[3] + diceNum[4])
    # bonus
    hasDone = False
    if upperScore >= 63:
        numLabels[9]['text'] = '35'
        if hasDone != True:
            totScore += 35
            hasDone = True


def endgame():
    global totScore, window, upperScore
    for i in range(len(numButtons)):
        if numButtons[i]['state'] == 'disabled':
            pass
        else:
            return False
    for i in range(len(specButtons)):
        if specButtons[i]['state'] == 'disabled':
            pass
        else:
            return False
    if upperScore >= 63:
        totScore += 35
    tkinter.messagebox.showinfo("Game Over!", "Your total score was " + str(totScore))
    window.destroy()



def score(button):
    global turn, totScore, rollButton, dice, upperScore
    # score numButtons
    if turn == 1:
        tkinter.messagebox.showinfo("Error!", "You need to actually roll the dice before scoring!")
    else:
        rollButton['text'] = 'Roll 1!'
        for i in range(6):
            if button == numButtons[i]:
                toAdd = int(numLabels[i]['text'])
                totScore += toAdd
                upperScore += toAdd
                numLabels[i]['bg'] = 'red'
                turn = 1
                button['state'] = 'disabled'

        for i in range(7):
            if button == specButtons[i]:
                toAdd = int(specLabels[i]['text'])
                totScore += toAdd

                turn = 1
                if button != specButtons[5]:
                    specLabels[i]['bg'] = 'red'
                    button['state'] = 'disabled'
                else:
                    specLabels[i]['text'] = '0'

        for i in range(len(dice)):
            dice[i]['bg'] = 'orange'
            dice[i]['text'] = ''
        numLabels[7]['text'] = str(upperScore)
        specLabels[8]['text'] = str(totScore)
        endgame()


def keep(button):
    if button['bg'] != 'green':
        button['bg'] = 'green'
    else:
        button['bg'] = 'orange'


window.configure(bg=bgcolour)
window.mainloop()