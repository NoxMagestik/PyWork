
# import libraries

from random import randint
from tkinter import *
import tkinter.messagebox
# variable for two player game, if false then next entry will be an 'o'
playerX = True
# turn variable is necessary for draw check, if still playing and turn is 9, then it must be a draw
turn = 0
# isPlaying is false if game is won
isPlaying = True
strategy = 0
# array to track which spaces have been played in, in the order
"""
0 | 1 | 2
----------
3 | 4 | 5
----------
6 | 7 | 8

"""
played = [False, False, False, False, False, False, False, False, False]
# set to false if computer makes successful play
computerHasNotPlayed = True
# ai score
score = 0
comScore = 0
# oScore and xScore only used in 2 player mode
oScore = 0
xScore = 0
# only set to two if the player has made a successful play
playerPlayed = False

def close_window():
    # Closes the window
    window.destroy()


# This is the enter method for the two player game
# two player functions -->
def enter(button):
    # allows the function to change these variables
    global playerX, turn, isPlaying, xScore, oScore
    # checks if it is playerX's turn, if so, enters an x
    if playerX == True:
        # checks if topLeft is played in, if not, then set text to x
        if button == topLeft:
            if played[0] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

            else:
                # sets tkinter passed in as argument's text x
                button["text"] = "x"
                turn += 1
                played[0] = True
                playerX = False
        # checks if topMiddle is played in, if not, then set text to x
        elif button == topMiddle:
            if played[1] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

            else:
                button["text"] = "x"
                turn += 1
                played[1] = True
                playerX = False
        # checks if topRight is played in, if not, then set text to x
        elif button == topRight:
            if played[2] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

            else:
                button["text"] = "x"
                turn += 1
                played[2] = True
                playerX = False
        # checks if middleLeft is played in, if not, then set text to x
        elif button == middleLeft:
            if played[3] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

            else:
                button["text"] = "x"
                turn += 1
                played[3] = True
                playerX = False
        # checks if middleMiddle is played in, if not, then set text to x
        elif button == middleMiddle:
            if played[4] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')
                pass
            else:
                button["text"] = "x"
                turn += 1
                played[4] = True
                playerX = False
        # checks if middleRight is played in, if not, then set text to x
        elif button == middleRight:
            if played[5] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')
                pass
            else:
                button["text"] = "x"
                turn += 1
                played[5] = True
                playerX = False
        # and so on, until bottomRight
        elif button == bottomLeft:
            if played[6] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')
                pass
            else:
                button["text"] = "x"
                turn += 1
                played[6] = True
                playerX = False
        elif button == bottomMiddle:
            if played[7] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')
                pass
            else:
                button["text"] = "x"
                turn += 1
                played[7] = True
                playerX = False
        elif button == bottomRight:
            if played[8] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

                pass
            else:
                button["text"] = "x"
                turn += 1
                played[8] = True
                playerX = False
    # else triggers if playerX is false i.e if it is o's turn
    else:
        # checks if topLeft is played in, if not, then set text to x
        if button == topLeft:
            if played[0] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

            else:
                button["text"] = "o"
                turn += 1
                played[0] = True
                # sets playerX to true, so that an x will be entered next click
                playerX = True
        # checks for each button until bottomRight
        elif button == topMiddle:
            if played[1] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

            else:
                button["text"] = "o"
                turn += 1
                played[1] = True
                playerX = True
        elif button == topRight:
            if played[2] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

            else:
                button["text"] = "o"
                turn += 1
                played[2] = True
                playerX = True
        elif button == middleLeft:
            if played[3] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

            else:
                button["text"] = "o"
                turn += 1
                played[3] = True
                playerX = True
        elif button == middleMiddle:
            if played[4] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')
                pass
            else:
                button["text"] = "o"
                turn += 1
                played[4] = True
                playerX = True
        elif button == middleRight:
            if played[5] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')
                pass
            else:
                button["text"] = "o"
                turn += 1
                played[5] = True
                playerX = True
        elif button == bottomLeft:
            if played[6] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')
                pass
            else:
                button["text"] = "o"
                turn += 1
                played[6] = True
                playerX = True
        elif button == bottomMiddle:
            if played[7] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')
                pass
            else:
                button["text"] = "o"
                turn += 1
                played[7] = True
                playerX = True
        elif button == bottomRight:
            if played[8] == True:
                tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

                pass
            else:
                button["text"] = "o"
                turn += 1
                played[8] = True
                playerX = True


    # Checks for horizontal three in a row for player X
    if topLeft['text'] == 'x' and topMiddle['text'] == 'x' and topRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        xScore += 1
    elif middleLeft['text'] == 'x' and middleMiddle['text'] == 'x' and middleRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        xScore += 1
    elif bottomLeft['text'] == 'x' and bottomMiddle['text'] == 'x' and bottomRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        xScore += 1
    # Checks for horizontal three in a row for player o
    if topLeft['text'] == 'o' and topMiddle['text'] == 'o' and topRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        oScore += 1
    elif middleLeft['text'] == 'o' and middleMiddle['text'] == 'o' and middleRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        oScore += 1
    elif bottomLeft['text'] == 'o' and bottomMiddle['text'] == 'o' and bottomRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        oScore += 1

    # Checks for vertical three in a row for player X
    if topLeft['text'] == 'x' and middleLeft['text'] == 'x' and bottomLeft['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        xScore += 1
    elif topMiddle['text'] == 'x' and middleMiddle['text'] == 'x' and bottomMiddle['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        xScore += 1

    elif topRight['text'] == 'x' and middleRight['text'] == 'x' and bottomRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False#
        xScore += 1

    # Checks for vertical three in a row for player o
    if topLeft['text'] == 'o' and middleLeft['text'] == 'o' and bottomLeft['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        oScore += 1

    elif topMiddle['text'] == 'o' and middleMiddle['text'] == 'o' and bottomMiddle['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        oScore += 1

    elif topRight['text'] == 'o' and middleRight['text'] == 'o' and bottomRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        oScore += 1

    # Checks for diagonal three in a row for player X
    if topLeft['text'] == 'x' and middleMiddle['text'] == 'x' and bottomRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        xScore += 1

    elif topRight['text'] == 'x' and middleMiddle['text'] == 'x' and bottomLeft['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        xScore += 1

    # Checks for diagonal three in a row for player O
    if topLeft['text'] == 'o' and middleMiddle['text'] == 'o' and bottomRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        oScore += 1

    elif topRight['text'] == 'o' and middleMiddle['text'] == 'o' and bottomLeft['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        oScore += 1

    # Checks for draw
    if isPlaying:
        if turn >= 9:
            tkinter.messagebox.showinfo('Draw!', 'Both players drew!')
            isPlaying = False

    if isPlaying == False:
        ans = tkinter.messagebox.askquestion('Play again?', 'Do you want to play again?')
        if ans == 'yes':
            reset()
        else:
            print("X's score was " + str(xScore) + ". O's score was " + str(oScore) + "." )
            close_window()
def reset():
    # sets all variables back to starting value and all buttons' text to black
    global playerX, topLeft, topMiddle, topRight, middleLeft, middleMiddle, middleRight, bottomLeft, bottomMiddle, bottomRight, window, isPlaying, turn
    isPlaying = True
    playerX = True
    turn = 0
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


# ai functions -->
def aienter(button):
    global playerX, topLeft, topMiddle, topRight, middleLeft, middleMiddle, middleRight, bottomLeft, bottomMiddle, bottomRight, window, isPlaying, turn, strategy, score, comScore
    global playerPlayed

    computerHasNotPlayed = True
    # checks if button is played in, if not, enter x
    if button == topLeft:
        if played[0] == True:
            tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

        else:
            button["text"] = "x"
            turn += 1
            played[0] = True
            playerPlayed = True
    elif button == topMiddle:
        if played[1] == True:
            tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

        else:
            button["text"] = "x"
            turn += 1
            played[1] = True
            playerPlayed = True
    elif button == topRight:
        if played[2] == True:
            tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

        else:
            button["text"] = "x"
            turn += 1
            played[2] = True
            playerPlayed = True
    elif button == middleLeft:
        if played[3] == True:
            tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

        else:
            button["text"] = "x"
            turn += 1
            played[3] = True
            playerPlayed = True
    elif button == middleMiddle:
        if played[4] == True:
            tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')
            pass
        else:
            button["text"] = "x"
            turn += 1
            played[4] = True
            playerPlayed = True
    elif button == middleRight:
        if played[5] == True:
            tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')
            pass
        else:
            button["text"] = "x"
            turn += 1
            played[5] = True
            playerPlayed = True
    elif button == bottomLeft:
        if played[6] == True:
            tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')
            pass
        else:
            button["text"] = "x"
            turn += 1
            played[6] = True
            playerPlayed = True
    elif button == bottomMiddle:
        if played[7] == True:
            tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')
            pass
        else:
            button["text"] = "x"
            turn += 1
            played[7] = True
            playerPlayed = True
    elif button == bottomRight:
        if played[8] == True:
            tkinter.messagebox.showinfo('Error!', 'This space has already been played in!')

            pass
        else:
            button["text"] = "x"
            turn += 1
            played[8] = True
            playerPlayed = True

    # win check comes before o play, so that it does not mess up

    # Checks for horizontal three in a row for player X
    if topLeft['text'] == 'x' and topMiddle['text'] == 'x' and topRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        score += 1
    elif middleLeft['text'] == 'x' and middleMiddle['text'] == 'x' and middleRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        score += 1
    elif bottomLeft['text'] == 'x' and bottomMiddle['text'] == 'x' and bottomRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        score += 1

    # Checks for vertical three in a row for player X
    if topLeft['text'] == 'x' and middleLeft['text'] == 'x' and bottomLeft['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        score += 1
    elif topMiddle['text'] == 'x' and middleMiddle['text'] == 'x' and bottomMiddle['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        score += 1

    elif topRight['text'] == 'x' and middleRight['text'] == 'x' and bottomRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        score += 1

    # Checks for diagonal three in a row for player X
    if topLeft['text'] == 'x' and middleMiddle['text'] == 'x' and bottomRight['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        score += 1

    elif topRight['text'] == 'x' and middleMiddle['text'] == 'x' and bottomLeft['text'] == 'x':
        tkinter.messagebox.showinfo('You Won!', 'Player X won!')
        isPlaying = False
        score += 1

    if isPlaying:
        if turn >= 9:
            tkinter.messagebox.showinfo('Draw!', 'Both players drew!')
            isPlaying = False



    if playerPlayed:
        if turn == 1 and middleMiddle['text'] == "":
            middleMiddle['text'] = "o"
            computerHasNotPlayed = False
            played[4] = True
            strategy = 1
        elif turn == 1 and middleMiddle['text'] == "x":
            topLeft['text'] = "o"
            computerHasNotPlayed = False
            played[0] = True
            strategy = 2
        else:
            if isPlaying:
                # offensive plays
                if computerHasNotPlayed:
                    if topLeft['text'] == 'o' and topMiddle['text'] == 'o':
                        if played[2] == True:
                            pass
                        else:
                            topRight['text'] = "o"
                            played[2] = True
                            computerHasNotPlayed = False


                if computerHasNotPlayed:
                    if topLeft['text'] == 'o' and middleMiddle['text'] == 'o':
                        if played[8] == True:
                            pass
                        else:
                            bottomRight['text'] = "o"
                            played[8] = True
                            computerHasNotPlayed = False

                if computerHasNotPlayed:
                    if topLeft['text'] == 'o' and middleLeft['text'] == 'o':
                        if played[6] == True:
                            pass
                        else:
                            bottomLeft['text'] = "o"
                            played[6] = True
                            computerHasNotPlayed = False

                # Checks for two in a row for topMiddle, excluding topleft
                if computerHasNotPlayed:
                    if topMiddle['text'] == 'o' and topRight['text'] == 'o':
                        if played[0] == True:
                            pass
                        else:
                            topLeft['text'] = "o    "
                            played[0] = True
                            computerHasNotPlayed = False

                if computerHasNotPlayed:
                    if topMiddle['text'] == 'o' and middleMiddle['text'] == 'o':
                        if played[7] == True:
                            pass
                        else:
                            bottomMiddle['text'] = "o"
                            played[7] = True
                            computerHasNotPlayed = False

                    # Checks for two in row for top right, excluding topmiddle
                if computerHasNotPlayed:
                    if topRight['text'] == 'o' and middleMiddle['text'] == 'o':
                        if played[6] == True:
                            pass
                        else:
                            bottomLeft['text'] = "o"
                            played[6] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if topRight['text'] == 'o' and middleRight['text'] == 'o':
                        if played[8] == True:
                            pass
                        else:
                            bottomRight['text'] = "o"
                            played[8] = True
                            computerHasNotPlayed = False


                # checks for two in a row for middle left, excluding topleft
                if computerHasNotPlayed:
                    if middleLeft['text'] == 'o' and bottomLeft['text'] == 'o':
                        if played[0] == True:
                            pass
                        else:
                            topLeft['text'] = "o"
                            played[0] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if middleLeft['text'] == 'o' and middleMiddle['text'] == 'o':
                        if played[5] == True:
                            pass
                        else:
                            middleRight['text'] = "o"
                            played[5] = True
                            computerHasNotPlayed = False
                # Checks for two in a row for middlemiddle, excluding top*, and middleleft
                if computerHasNotPlayed:
                    if middleRight['text'] == 'o' and middleMiddle['text'] == 'o':
                        if played[3] == True:
                            pass
                        else:
                            middleLeft['text'] = "o"
                            played[3] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if bottomLeft['text'] == 'o' and middleMiddle['text'] == 'o':
                        if played[2] == True:
                            pass
                        else:
                            topRight['text'] = "o"
                            played[2] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if bottomMiddle['text'] == 'o' and middleMiddle['text'] == 'o':
                        if played[1] == True:
                            pass
                        else:
                            topMiddle['text'] = "o"
                            played[1] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if bottomRight['text'] == 'o' and middleMiddle['text'] == 'o':
                        if played[0] == True:
                            pass
                        else:
                            topLeft['text'] = "o"
                            played[0] = True
                            computerHasNotPlayed = False

                # checks two in a row for middle right
                if computerHasNotPlayed:
                    if bottomRight['text'] == 'o' and middleRight['text'] == 'o':
                        if played[2] == True:
                            pass
                        else:
                            topRight['text'] = "o"
                            played[2] = True
                            computerHasNotPlayed = False
                # checks two in a row for bottom left, excluding middle left and middle middle
                if computerHasNotPlayed:
                    if bottomLeft['text'] == 'o' and bottomMiddle['text'] == 'o':
                        if played[8] == True:
                            pass
                        else:
                            bottomRight['text'] = "o"
                            played[8] = True
                            computerHasNotPlayed = False
                # checks two in a row for bottom middle, excluding bottom left, middle middle
                if computerHasNotPlayed:
                    if bottomRight['text'] == 'o' and bottomMiddle['text'] == 'o':
                        if played[6] == True:
                            pass
                        else:
                            bottomLeft['text'] = "o"
                            played[6] = True
                            computerHasNotPlayed = False

                # Defensive plays
                # Checks if there is two in a row from top left
                if computerHasNotPlayed:
                    if topLeft['text'] == 'x' and topMiddle['text'] == 'x':
                        if played[2] == True:
                            pass
                        else:
                            topRight['text'] = "o"
                            played[2] = True
                            computerHasNotPlayed = False


                if computerHasNotPlayed:
                    if topLeft['text'] == 'x' and middleMiddle['text'] == 'x':
                        if played[8] == True:
                            pass
                        else:
                            bottomRight['text'] = "o"
                            played[8] = True
                            computerHasNotPlayed = False

                if computerHasNotPlayed:
                    if topLeft['text'] == 'x' and middleLeft['text'] == 'x':
                        if played[6] == True:
                            pass
                        else:
                            bottomLeft['text'] = "o"
                            played[6] = True
                            computerHasNotPlayed = False

                # Checks for two in a row for topMiddle, excluding topleft
                if computerHasNotPlayed:
                    if topMiddle['text'] == 'x' and topRight['text'] == 'x':
                        if played[0] == True:
                            pass
                        else:
                            topLeft['text'] = "o"
                            played[0] = True
                            computerHasNotPlayed = False

                if computerHasNotPlayed:
                    if topMiddle['text'] == 'x' and middleMiddle['text'] == 'x':
                        if played[7] == True:
                            pass
                        else:
                            bottomMiddle['text'] = "o"
                            played[7] = True
                            computerHasNotPlayed = False

                    # Checks for two in row for top right, excluding topmiddle
                if computerHasNotPlayed:
                    if topRight['text'] == 'x' and middleMiddle['text'] == 'x':
                        if played[6] == True:
                            pass
                        else:
                            bottomLeft['text'] = "o"
                            played[6] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if topRight['text'] == 'x' and middleRight['text'] == 'x':
                        if played[8] == True:
                            pass
                        else:
                            bottomRight['text'] = "o"
                            played[8] = True
                            computerHasNotPlayed = False


                # checks for two in a row for middle left, excluding topleft
                if computerHasNotPlayed:
                    if middleLeft['text'] == 'x' and bottomLeft['text'] == 'x':
                        if played[0] == True:
                            pass
                        else:
                            topLeft['text'] = "o"
                            played[0] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if middleLeft['text'] == 'x' and middleMiddle['text'] == 'x':
                        if played[5] == True:
                            pass
                        else:
                            middleRight['text'] = "o"
                            played[5] = True
                            computerHasNotPlayed = False
                # Checks for two in a row for middlemiddle, excluding top*, and middleleft
                if computerHasNotPlayed:
                    if middleRight['text'] == 'x' and middleMiddle['text'] == 'x':
                        if played[3] == True:
                            pass
                        else:
                            middleLeft['text'] = "o"
                            played[3] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if bottomLeft['text'] == 'x' and middleMiddle['text'] == 'x':
                        if played[2] == True:
                            pass
                        else:
                            topRight['text'] = "o"
                            played[2] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if bottomMiddle['text'] == 'x' and middleMiddle['text'] == 'x':
                        if played[1] == True:
                            pass
                        else:
                            topMiddle['text'] = "o"
                            played[1] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if bottomRight['text'] == 'x' and middleMiddle['text'] == 'x':
                        if played[0] == True:
                            pass
                        else:
                            topLeft['text'] = "o"
                            played[0] = True
                            computerHasNotPlayed = False

                # checks two in a row for middle right
                if computerHasNotPlayed:
                    if bottomRight['text'] == 'x' and middleRight['text'] == 'x':
                        if played[2] == True:
                            pass
                        else:
                            topRight['text'] = "o"
                            played[2] = True
                            computerHasNotPlayed = False
                # checks two in a row for bottom left, excluding middle left and middle middle
                if computerHasNotPlayed:
                    if bottomLeft['text'] == 'x' and bottomMiddle['text'] == 'x':
                        if played[8] == True:
                            pass
                        else:
                            bottomRight['text'] = "o"
                            played[8] = True
                            computerHasNotPlayed = False
                # checks two in a row for bottom middle, excluding bottom left, middle middle
                if computerHasNotPlayed:
                    if bottomRight['text'] == 'x' and bottomMiddle['text'] == 'x':
                        if played[6] == True:
                            pass
                        else:
                            bottomLeft['text'] = "o"
                            played[6] = True
                            computerHasNotPlayed = False



                # offensive opposite plays
                # horizontal opposites

                if computerHasNotPlayed:
                    if topLeft['text'] == 'o' and topRight['text'] == 'o':
                        if played[1] == True:
                            pass
                        else:
                            topMiddle['text'] = "o"
                            played[1] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if middleLeft['text'] == 'o' and middleRight['text'] == 'o':
                        if played[4] == True:
                            pass
                        else:
                            middleMiddle['text'] = "o"
                            played[4] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if bottomLeft['text'] == 'o' and bottomRight['text'] == 'o':
                        if played[7] == True:
                            pass
                        else:
                            bottomMiddle['text'] = "o"
                            played[7] = True
                            computerHasNotPlayed = False

                # vertical opposites
                if computerHasNotPlayed:
                    if topLeft['text'] == 'o' and bottomLeft['text'] == 'o':
                        if played[3] == True:
                            pass
                        else:
                            middleLeft['text'] = "o"
                            played[3] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if topMiddle['text'] == 'o' and bottomMiddle['text'] == 'o':
                        if played[4] == True:
                            pass
                        else:
                            middleMiddle['text'] = "o"
                            played[4] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if topRight['text'] == 'o' and bottomRight['text'] == 'o':
                        if played[5] == True:
                            pass
                        else:
                            middleRight['text'] = "o"
                            played[5] = True
                            computerHasNotPlayed = False

                # diagonal opposites

                if computerHasNotPlayed:
                    if topLeft['text'] == 'o' and bottomRight['text'] == 'o':
                        if played[4] == True:
                            pass
                        else:
                            middleMiddle['text'] = "o"
                            played[4] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if bottomLeft['text'] == 'o' and topRight['text'] == 'o':
                        if played[4] == True:
                            pass
                        else:
                            middleMiddle['text'] = "o"
                            played[4] = True
                            computerHasNotPlayed = False

                # defensive opposite plays
                # horizontal opposites
                if computerHasNotPlayed:
                    if topLeft['text'] == 'x' and topRight['text'] == 'x':
                        if played[1] == True:
                            pass
                        else:
                            topMiddle['text'] = "o"
                            played[1] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if middleLeft['text'] == 'x' and middleRight['text'] == 'x':
                        if played[4] == True:
                            pass
                        else:
                            middleMiddle['text'] = "o"
                            played[4] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if bottomLeft['text'] == 'x' and bottomRight['text'] == 'x':
                        if played[7] == True:
                            pass
                        else:
                            bottomMiddle['text'] = "o"
                            played[7] = True
                            computerHasNotPlayed = False

                # vertical opposites
                if computerHasNotPlayed:
                    if topLeft['text'] == 'x' and bottomLeft['text'] == 'x':
                        if played[3] == True:
                            pass
                        else:
                            middleLeft['text'] = "o"
                            played[3] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if topMiddle['text'] == 'x' and bottomMiddle['text'] == 'x':
                        if played[4] == True:
                            pass
                        else:
                            middleMiddle['text'] = "o"
                            played[4] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if topRight['text'] == 'x' and bottomRight['text'] == 'x':
                        if played[5] == True:
                            pass
                        else:
                            middleRight['text'] = "o"
                            played[5] = True
                            computerHasNotPlayed = False

                # diagonal opposites

                if computerHasNotPlayed:
                    if topLeft['text'] == 'x' and bottomRight['text'] == 'x':
                        if played[4] == True:
                            if played[7] != True:
                                bottomMiddle['text'] = "o"
                                played[7] = True
                                computerHasNotPlayed = False

                            else:
                                pass
                        else:
                            middleMiddle['text'] = "o"
                            played[4] = True
                            computerHasNotPlayed = False
                if computerHasNotPlayed:
                    if bottomLeft['text'] == 'x' and topRight['text'] == 'x':
                        if played[4] == True:
                            if played[7] != True:
                                bottomMiddle['text'] = "o"
                                played[7] = True
                                computerHasNotPlayed = False

                            else:
                                pass

                        else:
                            middleMiddle['text'] = "o"
                            played[4] = True
                            computerHasNotPlayed = False


                # random play if computer has not played:
                if computerHasNotPlayed:
                    goodnum = []
                    for i in range(len(buttons)):
                        if played[i] == False:
                            goodnum.append(i)

                    if len(goodnum) != 0:
                        chosen = goodnum[randint(0, len(goodnum) - 1)]
                        buttons[chosen]['text'] = 'o'
                        played[chosen] = True
                        computerHasNotPlayed = False
                    else:
                        pass
            else:
                pass
    else:
        pass












    if computerHasNotPlayed == False:
        turn += 1


    # Checks for horizontal three in a row for player o
    if topLeft['text'] == 'o' and topMiddle['text'] == 'o' and topRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        comScore += 1
    elif middleLeft['text'] == 'o' and middleMiddle['text'] == 'o' and middleRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        comScore += 1
    elif bottomLeft['text'] == 'o' and bottomMiddle['text'] == 'o' and bottomRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        comScore += 1



    # Checks for vertical three in a row for player o
    if topLeft['text'] == 'o' and middleLeft['text'] == 'o' and bottomLeft['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        comScore += 1

    elif topMiddle['text'] == 'o' and middleMiddle['text'] == 'o' and bottomMiddle['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        comScore += 1

    elif topRight['text'] == 'o' and middleRight['text'] == 'o' and bottomRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        comScore += 1





    # Checks for diagonal three in a row for player O
    if topLeft['text'] == 'o' and middleMiddle['text'] == 'o' and bottomRight['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        comScore += 1

    elif topRight['text'] == 'o' and middleMiddle['text'] == 'o' and bottomLeft['text'] == 'o':
        tkinter.messagebox.showinfo('You Won!', 'Player O won!')
        isPlaying = False
        comScore += 1

    # Checks for draw


    if isPlaying == False:
        ans = tkinter.messagebox.askquestion('Play again?', 'Do you want to play again?')
        if ans == 'yes':
            aireset()
        else:
            close_window()
            print("Your score was " + str(score) + ". The computer's score was " + str(comScore) + ".")

    playerPlayed = False



def aireset():
    global score, comScore
    global playerPlayed
    global playerX, topLeft, topMiddle, topRight, middleLeft, middleMiddle, middleRight, bottomLeft, bottomMiddle, bottomRight, window, isPlaying, turn, played, computerHasNotPlayed, buttons
    isPlaying = True
    playerX = True
    playerPlayed = False
    strategy = 0
    played = [False, False, False, False, False, False, False, False, False]
    computerHasNotPlayed = True
    turn = 0
    font=('helvetica', 20)

    topLeft = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    topLeft["command"] = lambda:aienter(topLeft)
    topLeft.grid(row="0", column="0")
    topMiddle = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    topMiddle.grid(row="0", column="1")
    topMiddle["command"] = lambda:aienter(topMiddle)
    topRight = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    topRight.grid(row="0", column="3")
    topRight["command"] = lambda:aienter(topRight)
    middleLeft = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    middleLeft["command"] = lambda:aienter(middleLeft)
    middleLeft.grid(row="1", column="0")
    middleMiddle = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    middleMiddle.grid(row="1", column="1")
    middleMiddle["command"] = lambda:aienter(middleMiddle)
    middleRight = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    middleRight.grid(row="1", column="3")
    middleRight["command"] = lambda:aienter(middleRight)
    bottomLeft = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    bottomLeft.grid(row="2", column="0")
    bottomLeft["command"] = lambda:aienter(bottomLeft)
    bottomMiddle = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    bottomMiddle.grid(row="2", column="1")
    bottomMiddle["command"] = lambda:aienter(bottomMiddle)
    bottomRight = Button(window, text="", font=('helvetica', 30), height=5, width = 10)
    bottomRight.grid(row="2", column="3")
    bottomRight["command"] = lambda:aienter(bottomRight)
    buttons = [topLeft, topMiddle, topRight, middleLeft, middleMiddle, middleRight, bottomLeft, bottomMiddle, bottomRight]


font=('helvetica', 20)
window = Tk()
window.geometry("900x900")
isAi = tkinter.messagebox.askquestion('AI or 2 player', 'Do you want to play against the AI? If you click no, you will be playing a two player game.')
if isAi == 'yes':
    font=('helvetica', 20)
    aireset()
else:
    reset()


window.mainloop()