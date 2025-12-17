from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
import random

def rollDie(die):
    roll = random.randint(1, int(die))
    print(f"Rolled a {die}: {roll}")

def MainView(window):
    palette = window.palette
    d20 = window.dice_images["d20"]
    d10 = window.dice_images["d10"]
    d12 = window.dice_images["d12"]
    d8 = window.dice_images["d8"]
    d6 = window.dice_images["d6"]
    d4 = window.dice_images["d4"]
    d100 = window.dice_images["d100"]
    
    
    
    window.addSection(window.root, "Section Test")
    
    x = 5
    y = 0
    
    mainFrame = Frame(window.root, bg=palette["background"])
    mainFrame.grid(row=x, column=y, sticky="nsew")
    
    ##character Name section
    characterNameFrame = Frame(mainFrame, bg=palette["background"])
    characterNameFrame.grid(row=x, column=y, sticky="nsew")
    x+=1
    ##Add section contents
    characterHeaderFrame = Frame(characterNameFrame, bg=palette["background"])
    characterHeaderFrame.grid(row=0, column=0, sticky="nsew")
    characterNameLabel = Label(characterHeaderFrame, text="Character Name", font=("Script MT Bold", 28), fg=palette["heading"], bg=palette["background"]) #Script MT Bold, Goudy Old Style, Sitka Small
    characterNameLabel.grid(row=0, column=0, sticky="w")
    
    characterNameContentsFrame = Frame(characterNameFrame, bg=palette["background"])
    characterNameContentsFrame.grid(row=1, column=0, sticky="nsew")
    characterNameEntry = Entry(characterNameContentsFrame, bg=palette["color6"], fg=palette["color5"], font=("Sitka Small", 12))
    characterNameEntry.grid(row=0, column=0, sticky="ew")
    
    
    ## Racial traits section
    racialTraitsFrame = Frame(mainFrame, bg=palette["background"])
    racialTraitsFrame.grid(row=x, column=y, sticky="nsew")
    x+=1
    ##Add section contents
    raceLabel = Label(racialTraitsFrame, text="Racial Traits", font=("Script MT Bold", 28), fg=palette["heading"], bg=palette["background"]) #Script MT Bold, Goudy Old Style, Sitka Small
    raceLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    raceEntry = Entry(racialTraitsFrame, bg=palette["color6"], fg=palette["color5"], font=("Sitka Small", 12))
    raceEntry.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
    raceDieButton = Button(racialTraitsFrame, bg=palette["background"], image=d20, command=lambda: rollDie("20"), borderwidth=0, highlightthickness=0)
    raceDieButton.grid(row=1, column=1, sticky="e", padx=10, pady=10)
    
    return mainFrame
