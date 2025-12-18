import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import networkx as nx
from data.TableManager import TableManager
from Stack import Stack

class Window:
    def __init__(self, title, width, height):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        self.baseSectionHeadingFont = "Script MT Bold"
        self.baseSectionHeadingFontSize = 28
        self.baseSectionContentsFont = "Sitka Small"
        self.baseSectionContentsFontSize = 12
        
        self.currentSectionHeadingFont = self.baseSectionHeadingFont
        self.currentSectionHeadingFontSize = self.baseSectionHeadingFontSize
        self.currentSectionContentsFont = self.baseSectionContentsFont
        self.currentSectionContentsFontSize = self.baseSectionContentsFontSize
        
        self.currentSectionDepth = 1
        
        self.currentWidgets = nx.DiGraph() ##directed graph structure of the current widgets
        self.currentRow = 0
        self.currentColumn = 0
        self.tableManager = TableManager()
        self.tableStack = Stack() ##stack of tables to be rolled on

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
        
    
    def run(self):
        self.root.mainloop()
        
    def close(self):
        self.root.destroy()
        
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
            
    def addSection(self, master, title, table=None, currentRow=0, currentColumn=0):
        
        if self.currentSectionDepth > 1:
            if self.currentSectionHeadingFontSize > 10:
                self.currentSectionHeadingFontSize = self.baseSectionHeadingFontSize - (self.currentSectionDepth*5)
            else:
                self.currentSectionHeadingFontSize = 10
            
            if self.currentSectionContentsFontSize > 2:
                self.currentSectionContentsFontSize = self.baseSectionContentsFontSize - (self.currentSectionDepth*5)
            else:
                self.currentSectionContentsFontSize = 2
        else:
            self.currentSectionHeadingFont = self.baseSectionHeadingFont
            self.currentSectionHeadingFontSize = self.baseSectionHeadingFontSize
            self.currentSectionContentsFont = self.baseSectionContentsFont
            self.currentSectionContentsFontSize = self.baseSectionContentsFontSize
        
        ##adds a section to the provided frame
        mainFrame = Frame(master, bg=self.palette["background"])
        padding = self.currentSectionDepth * 10
        mainFrame.pack(fill="both", expand=True, padx=padding)
        
        headerFrame = Frame(mainFrame, bg=self.palette["background"])
        headerFrame.grid(row=0, column=0, sticky="nsew")
        headerLabel = Label(headerFrame, text=title, font=(self.currentSectionHeadingFont, self.currentSectionHeadingFontSize), fg=self.palette["heading"], bg=self.palette["background"]) #Script MT Bold, Goudy Old Style, Sitka Small
        headerLabel.grid(row=1, column=0, sticky="w")
        
        contentsFrame = Frame(mainFrame, bg=self.palette["background"])
        contentsFrame.grid(row=1, column=0, sticky="nsew")
        
        new_title = title.replace(" ", "_")
        
        self.addSectionContents(contentsFrame, title, table)
        
        
        return mainFrame
    
    
    def addSectionContents(self, master, title, table=None, currentRow=0, currentColumn=0):
        
        if title == "Character Name":
            entry = Entry(master, bg=self.palette["color6"], fg=self.palette["color5"], font=("Sitka Small", 12))
            entry.grid(row=1, column=0, sticky="ew")
        
        else:
            values = self.tableManager.getTableOptionsNames(title)
            
            supplementalFrame = Frame(master, bg=self.palette["background"]) ##to hold supplemental tables
            combobox = ttk.Combobox(master, font=("Sitka Small", 12))
            combobox.bind("<<ComboboxSelected>>", lambda event: self.handleComboboxSelection(combobox, title, supplementalFrame))
            combobox.configure(values=values)
            dieButton = Button(master, bg=self.palette["background"], image=self.dice_images["d20"], command=lambda: self.handleDiceRoll(combobox, title, supplementalFrame), borderwidth=0, highlightthickness=0)            
            combobox.grid(row=0, column=0, sticky="ew")
            dieButton.grid(row=0, column=1, sticky="e")
            supplementalFrame.grid(row=1, column=0, columnspan=2, sticky="nsew")

            
    def handleDiceRoll(self, combobox, table, master):
        result = self.tableManager.rollOnTableByName(table)
        combobox.set(result)
        self.handleComboboxSelection(combobox, table, master)
        
    def handleComboboxSelection(self, combobox, title, master):
        value = combobox.get()
        
        option = self.tableManager.getTableOptionByName(value) ##grab the option object associated with the value from the current table
        if option is not None:
            tables = option.getSuppTables()
            if len(tables) > 0:
                self.removeWidgets(master) ##refresh the sections
                for table in tables:
                    self.addSection(master, table.getName(), table=table)
            else:
                self.currentSectionDepth = 0 
        else:
            print(f"No table found for {value}")
        