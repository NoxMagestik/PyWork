# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:32:04 2018

@author: Daniyal
"""


from tkinter import *
import tkinter.messagebox
playerX = True
turn = 1
isPlaying = True
strategy = 0
played = [False, False, False, False, False, False, False, False, False]
def close_window():
    window.destroy()
def reset():
    global playerX, topLeft, topMiddle, topRight, middleLeft, middleMiddle, middleRight, bottomLeft, bottomMiddle, bottomRight, window, isPlaying, turn, played
    isPlaying = True
    playerX = True
    turn = 1
    topLeft = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    topLeft["command"] = lambda:enter(topLeft)
    topLeft.grid(row="0", column="0")
    topMiddle = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    topMiddle.grid(row="0", column="1")
    topMiddle["command"] = lambda:enter(topMiddle)
    topRight = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    topRight.grid(row="0", column="3")
    topRight["command"] = lambda:enter(topRight)
    middleLeft = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    middleLeft["command"] = lambda:enter(middleLeft)
    middleLeft.grid(row="1", column="0")
    middleMiddle = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    middleMiddle.grid(row="1", column="1")
    middleMiddle["command"] = lambda:enter(middleMiddle)
    middleRight = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    middleRight.grid(row="1", column="3")
    middleRight["command"] = lambda:enter(middleRight)
    bottomLeft = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    bottomLeft.grid(row="2", column="0")
    bottomLeft["command"] = lambda:enter(bottomLeft)
    bottomMiddle = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    bottomMiddle.grid(row="2", column="1")
    bottomMiddle["command"] = lambda:enter(bottomMiddle)
    bottomRight = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    bottomRight.grid(row="2", column="3")
    bottomRight["command"] = lambda:enter(bottomRight)


def enter(button):
    global playerX, topLeft, topMiddle, topRight, middleLeft, middleMiddle, middleRight, bottomLeft, bottomMiddle, bottomRight, window, isPlaying, turn, strategy
    button["text"] = "x"
        
    if turn == 1 and middleMiddle['text'] == "":
        middleMiddle['text'] = "o"
        strategy = 1
    elif turn == 1 and middleMiddle['text'] == "x":
        topLeft['text'] = "o"
        strategy = 2
    else:

        # Checks if there is two in a row from top left
        if topLeft['text'] == 'x' and topMiddle['text'] == 'x':
            topRight['text'] = "o"

        elif topLeft['text'] == 'x' and middleMiddle['text'] == 'x':
            bottomRight['text'] = "o"

        elif topLeft['text'] == 'x' and middleLeft['text'] == 'x':
            bottomLeft['text'] = "o"

        # Checks for two in a row for topMiddle, excluding topleft
        elif topMiddle['text'] == 'x' and topRight['text'] == 'x':
            topLeft['text'] == "o"

        elif topMiddle['text'] == 'x' and middleMiddle['text'] == 'x':
            bottomMiddle['text'] = "o"

        # Checks for two in row for top right, excluding topmiddle
        elif topRight['text'] == 'x' and middleMiddle['text'] == 'x':
            bottomLeft['text'] = "o"

        elif topRight['text'] == 'x' and middleRight['text'] == 'x':
            bottomRight['text'] = "o"
    turn += 1




    # Checks for horizontal three in a row for player X
    if topLeft['text'] == 'x' and topMiddle['text'] == 'x' and topRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
    elif middleLeft['text'] == 'x' and middleMiddle['text'] == 'x' and middleRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
    elif bottomLeft['text'] == 'x' and bottomMiddle['text'] == 'x' and bottomRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
    # Checks for horizontal three in a row for player o
    if topLeft['text'] == 'o' and topMiddle['text'] == 'o' and topRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
    elif middleLeft['text'] == 'o' and middleMiddle['text'] == 'o' and middleRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
    elif bottomLeft['text'] == 'o' and bottomMiddle['text'] == 'o' and bottomRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False

    # Checks for vertical three in a row for player X
    if topLeft['text'] == 'x' and middleLeft['text'] == 'x' and bottomLeft['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
    elif topMiddle['text'] == 'x' and middleMiddle['text'] == 'x' and bottomMiddle['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False

    elif topRight['text'] == 'x' and middleRight['text'] == 'x' and bottomRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False#

    # Checks for vertical three in a row for player o
    if topLeft['text'] == 'o' and middleLeft['text'] == 'o' and bottomLeft['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False

    elif topMiddle['text'] == 'o' and middleMiddle['text'] == 'o' and bottomMiddle['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False

    elif topRight['text'] == 'o' and middleRight['text'] == 'o' and bottomRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False

    # Checks for diagonal three in a row for player X
    if topLeft['text'] == 'x' and middleMiddle['text'] == 'x' and bottomRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False

    elif topRight['text'] == 'x' and middleMiddle['text'] == 'x' and bottomLeft['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False

    # Checks for diagonal three in a row for player O
    if topLeft['text'] == 'o' and middleMiddle['text'] == 'o' and bottomRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False

    elif topRight['text'] == 'o' and middleMiddle['text'] == 'o' and bottomLeft['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False

    # Checks for draw
    if isPlaying:
        if turn >= 10:
            tkinter.messagebox.showinfo('Draw!', 'Both players drew!')
            isPlaying = False

    if isPlaying == False:
        ans = tkinter.messagebox.askquestion('Play again?', 'Do you want to play again?')
        if ans == 'yes':
            reset()
        else:
            close_window()
font=('helvetica', 20)

window = Tk()
window.geometry("900x900")
topLeft = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
topLeft["command"] = lambda:enter(topLeft)
topLeft.grid(row="0", column="0")
topMiddle = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
topMiddle.grid(row="0", column="1")
topMiddle["command"] = lambda:enter(topMiddle)
topRight = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
topRight.grid(row="0", column="3")
topRight["command"] = lambda:enter(topRight)
middleLeft = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
middleLeft["command"] = lambda:enter(middleLeft)
middleLeft.grid(row="1", column="0")
middleMiddle = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
middleMiddle.grid(row="1", column="1")
middleMiddle["command"] = lambda:enter(middleMiddle)
middleRight = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
middleRight.grid(row="1", column="3")
middleRight["command"] = lambda:enter(middleRight)
bottomLeft = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
bottomLeft.grid(row="2", column="0")
bottomLeft["command"] = lambda:enter(bottomLeft)
bottomMiddle = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
bottomMiddle.grid(row="2", column="1")
bottomMiddle["command"] = lambda:enter(bottomMiddle)
bottomRight = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
bottomRight.grid(row="2", column="3")
bottomRight["command"] = lambda:enter(bottomRight)


window.mainloop()