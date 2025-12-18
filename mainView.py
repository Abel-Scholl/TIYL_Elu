from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
import random

def rollDie(die):
    roll = random.randint(1, int(die))
    print(f"Rolled a {die}: {roll}")

def MainView(window, character):
    palette = window.palette

    mainFrame = Frame(window.root, bg=palette["background"])
    mainFrame.grid(row=0, column=0, sticky="nsew")
    
    leftFrame = Frame(mainFrame, bg=palette["background"])
    leftFrame.grid(row=0, column=0, sticky="nsew")
    rightFrame = Frame(mainFrame, bg=palette["background"])
    rightFrame.grid(row=0, column=1, sticky="nsew")
    
    while not window.tableStack.isEmpty():
        section = window.tableStack.pop()
        print(section)
        window.addSection(leftFrame, section)
    
    
    return mainFrame
