
from Window import Window
from Character import Character
from data.TableManager import TableManager
from Stack import Stack
from mainView import MainView

def main():
    window = Window("TIYL_Elu", 800, 600)
    character = Character()
    stack = Stack()
    MainView(window, character, stack)
    
    window.run()

if __name__ == "__main__":
    main()
    
    
    
    
    
#    canvas = Canvas(mainFrame)
#    scrollbar = Scrollbar(mainFrame, orient="vertical", command=canvas.yview)

#    content_frame = ttk.Frame(canvas)
#    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
#    fonts=list(font.families())
#    for f_name in fonts:
#        #print(f_name)
#        Label(content_frame, text=f_name, font=(f_name, 18)).grid(row=x, column=y, sticky="nsew")
#        x+=1
    
#    content_frame.columnconfigure(0, weight=1)
#    content_frame.rowconfigure(0, weight=1)
    
#    canvas.create_window((0, 0), window=content_frame, anchor="nw")
#    canvas.grid(row=x, column=y, sticky="nsew")
#    scrollbar.grid(row=x, column=y+1, sticky="ns")
    
#    def _on_mousewheel(event):
#        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

#    canvas.bind_all("<MouseWheel>", _on_mousewheel)