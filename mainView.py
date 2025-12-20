from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
import pymupdf 

def MainView(window):
    palette = window.palette

    mainFrame = Frame(window.root, bg=palette["background"])
    mainFrame.grid(row=0, column=0, sticky="nsew")
    
    # Left side with scrollbar
    leftCanvas = Canvas(mainFrame, bg=palette["background"], highlightthickness=0)
    leftScrollbar = Scrollbar(mainFrame, orient="vertical", command=leftCanvas.yview)
    leftFrame = Frame(leftCanvas, bg=palette["background"])
    
    leftCanvas.pack(side="left", fill="both", expand=True)
    leftScrollbar.pack(side="left", fill="y")
    
    leftCanvas.create_window((0, 0), window=leftFrame, anchor="nw")
    leftCanvas.configure(yscrollcommand=leftScrollbar.set)
    
    def configure_left_scroll(event):
        # Update scroll region and canvas width
        leftCanvas.configure(scrollregion=leftCanvas.bbox("all"))
        canvas_width = event.width
        canvas_items = leftCanvas.find_all()
        if canvas_items:
            leftCanvas.itemconfig(canvas_items[0], width=canvas_width)
    
    leftFrame.bind("<Configure>", configure_left_scroll)
    
    def on_left_canvas_configure(event):
        canvas_width = event.width
        canvas_items = leftCanvas.find_all()
        if canvas_items:
            leftCanvas.itemconfig(canvas_items[0], width=canvas_width)
    
    leftCanvas.bind("<Configure>", on_left_canvas_configure)
    
    # Right side with scrollbar
    rightCanvas = Canvas(mainFrame, bg=palette["background"], highlightthickness=0)
    rightScrollbar = Scrollbar(mainFrame, orient="vertical", command=rightCanvas.yview)
    rightFrame = Frame(rightCanvas, bg=palette["background"])
    
    rightScrollbar.pack(side="right", fill="y")
    rightCanvas.pack(side="right", fill="both", expand=True)
    
    rightCanvas.create_window((0, 0), window=rightFrame, anchor="nw")
    rightCanvas.configure(yscrollcommand=rightScrollbar.set)
    
    def configure_right_scroll(event):
        # Update scroll region and canvas width
        rightCanvas.configure(scrollregion=rightCanvas.bbox("all"))
        canvas_width = event.width
        canvas_items = rightCanvas.find_all()
        if canvas_items:
            rightCanvas.itemconfig(canvas_items[0], width=canvas_width)
    
    rightFrame.bind("<Configure>", configure_right_scroll)
    
    def on_right_canvas_configure(event):
        canvas_width = event.width
        canvas_items = rightCanvas.find_all()
        if canvas_items:
            rightCanvas.itemconfig(canvas_items[0], width=canvas_width)
    
    rightCanvas.bind("<Configure>", on_right_canvas_configure)
    
    # Enable mousewheel scrolling (reversed direction)
    def _on_mousewheel_left(event):
        # Reverse direction: multiply by -1 to flip scroll direction
        scroll_amount = int(event.delta)
        leftCanvas.yview_scroll(scroll_amount, "units")
    
    def _on_mousewheel_right(event):
        # Reverse direction: multiply by -1 to flip scroll direction
        scroll_amount = int(event.delta)*-1
        rightCanvas.yview_scroll(scroll_amount, "units")
    
    leftCanvas.bind("<MouseWheel>", _on_mousewheel_left)
    rightCanvas.bind("<MouseWheel>", _on_mousewheel_right)
    
    # Also bind to the frames inside the canvas
    leftFrame.bind("<MouseWheel>", _on_mousewheel_left)
    rightFrame.bind("<MouseWheel>", _on_mousewheel_right)
    
    while not window.tableStack.isEmpty():
        section = window.tableStack.pop()
        print(section)
        window.addSection(leftFrame, section)
    
    
    
        
    Base = ["Character Name", "Level", "Race", "Background", "Class"]
    Origins = ["Parents", "Birthplace", "Siblings", "Family", "Absent Parent", "Childhood Home", "Childhood Memories"]
    Bonds = [] ##This is where people close to you will go. If you have family/siblings, the tables to roll on for them will show up here.
    PersonalDecisions = ["Background", "Class"]
    LifeEvents = ["Life Events"]
    Supplemental = []
    
    sections = [Origins, PersonalDecisions, LifeEvents, Supplemental]
        
    # Style the notebook tabs
    style = ttk.Style()
    style.configure("TNotebook.Tab", 
                    background=palette["color3"],
                    foreground=palette["color6"],
                    padding=[10, 5])
    style.map("TNotebook.Tab",
              background=[("selected", palette["background"])],
              foreground=[("selected", palette["color6"])])
    
    notebook = ttk.Notebook(rightFrame)
    tabs = ["Base", "Origins", "Relationships", "Personal Decisions", "Life Events", "Supplemental"]
    for tab in tabs:
        frame = ttk.Frame(notebook, bg=palette["color3"])
        label = ttk.Label(frame, text = tab)
        label.pack(pady = 50, padx = 20)
        frame.pack(fill= "both", expand=True)
        notebook.insert("end", frame, text = tab)
        notebook.add(frame, text = tab)
    
    notebook.pack(fill="both", expand=True, padx=5, pady=5)
    
    
    doc = pymupdf.open("./assets/CharacterSheet1.pdf")
    page = doc.load_page(0)
    pix = page.get_pixmap()
    # set the mode depending on alpha
    mode = "RGBA" if pix.alpha else "RGB"
    img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
    tkimg = ImageTk.PhotoImage(img)
    
    pdf_label = Label(rightFrame, image=tkimg)
    #pdf_label.pack()
    
    
    traits = window.character.getAll()
    i=0
    for trait, value in traits.items():
        label = Label(rightFrame, text=f"{trait}: {value}", font=("Sitka Small", 12), bg=palette["background"], fg=palette["color6"])
        label.grid(row=i, column=0, sticky="w")
        i+=1
    
    
    
    
    return mainFrame
