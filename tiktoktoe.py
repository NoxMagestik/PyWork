# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:32:04 2018

@author: Daniyal
"""
from logic import *
from tkinter import *


window = Tk()
window.geometry("900x900")
topLeft = Button(window, text="", height = 15, width = 33)
topLeft["command"] = lambda:enter(topLeft)
topLeft.grid(row="0", column="0")
topMiddle = Button(window, text="", height = 15, width = 33)
topMiddle.grid(row="0", column="1")
topMiddle["command"] = lambda:enter(topMiddle)
topRight = Button(window, text="", height = 15, width = 33)
topRight.grid(row="0", column="3")
topRight["command"] = lambda:enter(topRight)
middleLeft = Button(window, text="", height = 15, width = 33)
middleLeft["command"] = lambda:enter(middleLeft)
middleLeft.grid(row="1", column="0")
middleMiddle = Button(window, text="", height = 15, width = 33)
middleMiddle.grid(row="1", column="1")
middleMiddle["command"] = lambda:enter(middleMiddle)
middleRight = Button(window, text="", height = 15, width = 33)
middleRight.grid(row="1", column="3")
middleRight["command"] = lambda:enter(middleRight)
bottomLeft = Button(window, text="", height = 15, width = 33)
bottomLeft.grid(row="2", column="0")
bottomLeft["command"] = lambda:enter(bottomLeft)
bottomMiddle = Button(window, text="", height = 15, width = 33)
bottomMiddle.grid(row="2", column="1")
bottomMiddle["command"] = lambda:enter(bottomMiddle)
bottomRight = Button(window, text="", height = 15, width = 33)
bottomRight.grid(row="2", column="3")
bottomRight["command"] = lambda:enter(bottomRight)


window.mainloop()