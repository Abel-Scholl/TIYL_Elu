import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import networkx as nx

class Window:
    def __init__(self, title, width, height):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.currentWidgets = nx.DiGraph() ##directed graph structure of the current widgets
        self.currentRow = 0
        self.currentColumn = 0


        self.palette = {
            "background": "#757992", ##blue
            "heading": "#EE881A", ##orange/gold
            "color3": "#A41917", ##red
            "color4": "#819564", ##tan/green
            "color5": "#030F15", ##black
            "color6": "#F1DBB5" ##cream
        }
        
        dice_image = Image.open("./assets/dice.png")
        dice_image = dice_image.resize((dice_image.width // 4, dice_image.height // 4))
        self.dice_images = {
            "d100": dice_image.crop((0, 0, 30, 40)),
            "d20": dice_image.crop((115, 0, 160, 40)),
            "d12": dice_image.crop((70, 0, 110, 40)),
            "d10": dice_image.crop((30, 0, 70, 40)),
            "d8": dice_image.crop((108, 40, 148, 85)),
            "d6": dice_image.crop((60, 40, 100, 85)),
            "d4": dice_image.crop((8, 40, 50, 85))
        }

        for key, value in self.dice_images.items():
            self.dice_images[key] = ImageTk.PhotoImage(value)
        
        self.currentWidgets.add_nodes_from([    
            ("root", {"widget": self.root, "type": "window"})
        ])
        
    
    def setWidth(self, width):
        self.screen_width = width
        self.root.geometry(f'{self.screen_width}x{self.screen_height}')
    
    def getWidth(self):
            return self.screen_width
    
    def setHeight(self, height):
        self.screen_height = height
        self.root.geometry(f'{self.screen_width}x{self.screen_height}')
    
    def getHeight(self):
        return self.screen_height
    
    def __getAllWidgets(self):
    ## references all widgets in a frame and returns them in a list
        _list = self.root.winfo_children() ##list of the bound master's widgets from bottom to top
        if _list:
            for widget in _list:
                if widget.winfo_children():
                    _list.extend(self.root.winfo_children()) ## if the widget has embedded widgets, acknowledge them too.
        return _list
    
    def removeWidgets(self, master=None):
        ##removes all widgets contained within a specified frame
        ##without removing the frame itself
        ##if no frame is specified, the main window is cleared
        ##and the GUI will close.
        if master != None:
            delete = master.winfo_children()
            for i in delete:
                i.destroy()
        else:
            self.root.destroy()
            
    def addSection(self, master, title, currentRow=0, currentColumn=0):
        ##adds a section to the provided frame
        mainFrame = Frame(master, bg=self.palette["background"])
        mainFrame.grid(row=currentRow, column=currentColumn, sticky="nsew")
        
        headerFrame = Frame(mainFrame, bg=self.palette["background"])
        headerFrame.grid(row=0, column=0, sticky="nsew")
        headerLabel = Label(headerFrame, text=title, font=("Script MT Bold", 28), fg=self.palette["heading"], bg=self.palette["background"]) #Script MT Bold, Goudy Old Style, Sitka Small
        headerLabel.grid(row=1, column=0, sticky="w")
        
        contentsFrame = Frame(mainFrame, bg=self.palette["background"])
        contentsFrame.grid(row=1, column=0, sticky="nsew")
        
        self.currentWidgets.add_nodes_from([
            (f"{title}Frame", {"widget": mainFrame, "type": "frame", "currentRow": 1, "currentColumn": 0}),
            (f"{title}HeaderFrame", {"widget": headerFrame, "type": "frame", "currentRow": 1, "currentColumn": 0}),
            (f"{title}ContentsFrame", {"widget": contentsFrame, "type": "frame", "currentRow": 2, "currentColumn": 0}),
        ])
        
        self.currentWidgets.add_edges_from([
            ("root", f"{title}Frame"),
            (f"{title}Frame", f"{title}HeaderFrame"),
            (f"{title}Frame", f"{title}ContentsFrame"),
        ])
        
        ##update the current row and column of the master frame
        
        return mainFrame
    
    def run(self):
        self.root.mainloop()
        
    def close(self):
        self.root.destroy()
    
        