from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
import random

def rollDie(die):
    roll = random.randint(1, int(die))
    print(f"Rolled a {die}: {roll}")

def MainView(window, character, stack):
    palette = window.palette
    d100 = window.dice_images["d100"]
    d20 = window.dice_images["d20"]
    d10 = window.dice_images["d10"]
    d12 = window.dice_images["d12"]
    d8 = window.dice_images["d8"]
    d6 = window.dice_images["d6"]
    d4 = window.dice_images["d4"]      


    mainFrame = Frame(window.root, bg=palette["background"])
    mainFrame.grid(row=0, column=0, sticky="nsew")
    
    leftFrame = Frame(mainFrame, bg=palette["background"])
    leftFrame.grid(row=0, column=0, sticky="nsew")
    rightFrame = Frame(mainFrame, bg=palette["background"])
    rightFrame.grid(row=0, column=1, sticky="nsew")
    
    while not stack.isEmpty():
        section = stack.pop()
        print(section)
        window.addSection(leftFrame, section)
    
    
    return mainFrame
