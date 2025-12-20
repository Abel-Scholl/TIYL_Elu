import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import networkx as nx
from data.TableManager import TableManager
from Character import Character
from Stack import Stack
from config import palette, sections
from ScrollEvents import configure_scroll, on_canvas_configure, _on_mousewheel

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
        
        self.currentWidgets = {}
        self.currentRow = 0
        self.currentColumn = 0
        self.tableManager = TableManager()
        self.character = Character()
        self.tableStack = Stack()

        self.palette = palette
        self.style = ttk.Style()
        self.style_notebook()
        
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
        
        self.initializeMainFrames()
        
    def initializeNotebookWindows(self):
        leftFrame = self.currentWidgets["leftFrame"]
        notebook = ttk.Notebook(leftFrame)
        self.currentWidgets.update({"notebook": notebook})
        
        tabs = sections.keys()
        for tab in tabs:
            # Create a container frame for the tab that will hold canvas and scrollbar
            tabContainer = Frame(notebook, bg=self.palette["background"])
            
            # Create canvas and scrollbar inside the container
            canvas = Canvas(tabContainer, bg=self.palette["background"], highlightthickness=0)
            scrollbar = Scrollbar(tabContainer, orient="vertical", command=canvas.yview)
            frame = Frame(canvas, bg = self.palette["background"])
            
            # Pack canvas first (scrollbar will be shown/hidden dynamically on the right)
            canvas.pack(side="left", fill="both", expand=True)
            
            # Configure canvas with the scrollable frame
            canvas.create_window((0, 0), window=frame, anchor="nw")
            # Initially disable scrollbar (will be enabled if content exceeds canvas)
            canvas.configure(yscrollcommand=lambda *args: None)
            
            # Bind scroll events (pass scrollbar so it can be shown/hidden)
            frame.bind("<Configure>", lambda event, c=canvas, s=scrollbar: configure_scroll(event, c, s))
            canvas.bind("<Configure>", lambda event, c=canvas, s=scrollbar: on_canvas_configure(event, c, s))
            canvas.bind("<MouseWheel>", lambda event, c=canvas: _on_mousewheel(event, c))
            frame.bind("<MouseWheel>", lambda event, c=canvas: _on_mousewheel(event, c))
            
            widgets = {
                f"{tab}Canvas": canvas,
                f"{tab}Scrollbar": scrollbar,
                f"{tab}Frame": frame,
                f"{tab}Container": tabContainer
            }
            self.currentWidgets.update(widgets)
            
            # Add the container to the notebook (not the canvas directly)
            notebook.add(tabContainer, text = tab)
            
            while not self.tableStack.isEmpty():
                section = self.tableStack.pop()
                print(section)
                self.addSection(frame, section)
            
        notebook.pack(fill="both", expand=True, padx=5, pady=5)
    
    def initializeMainFrames(self):
        widgets = {}
        
        mainFrame = Frame(self.root, bg=self.palette["background"])
        mainFrame.grid(row=0, column=0, sticky="nsew")
        
        leftFrame = Frame(mainFrame, bg=self.palette["color4"])
        leftFrame.pack(side="left", fill="both", expand=True)

        
        # Right side with scrollbar
        rightCanvas = Canvas(mainFrame, bg=self.palette["color4"], highlightthickness=0)
        rightScrollbar = Scrollbar(mainFrame, orient="vertical", command=rightCanvas.yview)
        rightFrame = Frame(rightCanvas, bg=self.palette["color4"])
        
        # Pack canvas first (scrollbar will be packed on the right when needed)
        rightCanvas.pack(side="left", fill="both", expand=True)
        
        rightCanvas.create_window((0, 0), window=rightFrame, anchor="nw")
        # Initially disable scrollbar (will be enabled if content exceeds canvas)
        rightCanvas.configure(yscrollcommand=lambda *args: None)
        
        rightFrame.bind("<Configure>", lambda event: configure_scroll(event, rightCanvas, rightScrollbar))
        rightCanvas.bind("<Configure>", lambda event: on_canvas_configure(event, rightCanvas, rightScrollbar))
        
        ##bind the mousewheel to the right canvas and the right frame
        rightCanvas.bind("<MouseWheel>", lambda event: _on_mousewheel(event, rightCanvas))
        rightFrame.bind("<MouseWheel>", lambda event: _on_mousewheel(event, rightCanvas))
        
        ##add the widgets to the current widgets dictionary
        widgets = {
            "mainFrame": mainFrame,
            "leftFrame": leftFrame,
            "rightCanvas": rightCanvas,
            "rightFrame": rightFrame,
            "rightScrollbar": rightScrollbar
        }
        self.currentWidgets.update(widgets)
        
        self.initializeNotebookWindows()
        
        
        self.refreshCharacterSheet()
    
    
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
            
    def refreshCharacterSheet(self):
        master = self.currentWidgets["rightFrame"]
        self.removeWidgets(master)
        traits = self.character.getAll()
        i=0
        for trait, value in traits.items():
            label = Label(master, text=f"{trait}: {value}", font=("Sitka Small", 16), bg=self.palette["color4"], fg=self.palette["color5"])
            label.grid(row=i, column=0, sticky="w")
            self.currentWidgets.update({f"{trait}": label})
            i+=1
    
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
            
            self.character.set(option.getParentTable(), value)
            self.refreshCharacterSheet()
            self.removeWidgets(master) ##refresh the sections
            master.grid_remove() ## Hide the frame entirely so it takes up no space
            
            tables = option.getSuppTables()
            if len(tables) > 0:
                master.grid() ## Show the frame again since we have content
                for table in tables:
                    self.addSection(master, table.getName(), table=table)
            else:
                print(f"No table found for {value}")


    def style_notebook(self):
        # Use a theme that supports custom tab backgrounds (works better on Windows)
        # Try 'clam' or 'alt' theme which support background colors
        try:
            self.style.theme_use('clam')
        except:
            try:
                self.style.theme_use('alt')
            except:
                pass  # Use default theme if others aren't available

        # Style the tab bar (the area behind the tabs)
        self.style.configure("TNotebook",
                    background=palette["color4"],
                    borderwidth=0,
                    bordercolor=palette["color5"])

        # Style the individual tabs
        self.style.configure("TNotebook.Tab", 
                    background=palette["color3"],
                    foreground=palette["color7"],
                    padding=[10, 5],
                    borderwidth=2,
                    bordercolor=palette["color5"],
                    relief="solid",
                    lightcolor=palette["color5"],
                    darkcolor=palette["color5"])

        self.style.map("TNotebook.Tab",
                background=[("selected", palette["background"]), ("!selected", palette["color3"])],
                foreground=[("selected", palette["color6"]), ("!selected", palette["color7"])],
                bordercolor=[("selected", palette["color5"]), ("!selected", palette["color5"])],
                lightcolor=[("selected", palette["color5"]), ("!selected", palette["color5"])],
                darkcolor=[("selected", palette["color5"]), ("!selected", palette["color5"])],
                borderwidth=[("selected", 2), ("!selected", 2)],
                expand=[("selected", [1, 1, 1, 0])]) #[top, right, bottom, left]
        