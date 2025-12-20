def configure_scroll(event, canvas, scrollbar=None):
    # Update scroll region and canvas width
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas_width = event.width
    canvas_items = canvas.find_all()
    if canvas_items:
        canvas.itemconfig(canvas_items[0], width=canvas_width)
    
    # Check if scrolling is needed and update scrollbar visibility
    if scrollbar:
        _update_scrollbar_state(canvas, scrollbar)
                
def on_canvas_configure(event, canvas, scrollbar=None):
    canvas_width = event.width
    canvas_items = canvas.find_all()
    if canvas_items:
        canvas.itemconfig(canvas_items[0], width=canvas_width)
    
    # Check if scrolling is needed
    if scrollbar:
        _update_scrollbar_state(canvas, scrollbar)

def _update_scrollbar_state(canvas, scrollbar):
    """Show/hide scrollbar based on whether content exceeds canvas size"""
    try:
        # Get the scroll region (content size)
        bbox = canvas.bbox("all")
        if bbox:
            content_height = bbox[3] - bbox[1]  # bottom - top
            canvas_height = canvas.winfo_height()
            
            # Only show scrollbar if content is taller than canvas
            if content_height > canvas_height:
                # Content exceeds canvas, show scrollbar on the right
                # Ensure canvas is packed left, scrollbar right
                if canvas.winfo_manager() == "pack":
                    canvas.pack_configure(side="left", fill="both", expand=True)
                scrollbar.pack(side="right", fill="y")
                canvas.configure(yscrollcommand=scrollbar.set)
            else:
                # Content fits, hide scrollbar
                scrollbar.pack_forget()
                canvas.configure(yscrollcommand=lambda *args: None)
    except:
        pass

def _on_mousewheel(event, canvas):
    # Check if scrolling is needed before scrolling
    try:
        bbox = canvas.bbox("all")
        if bbox:
            content_height = bbox[3] - bbox[1]  # bottom - top
            canvas_height = canvas.winfo_height()
            
            # Only scroll if content is taller than canvas
            if content_height > canvas_height:
                # Reverse direction: multiply by -1 to flip scroll direction
                scroll_amount = int(event.delta)*-1
                canvas.yview_scroll(scroll_amount, "units")
    except:
        pass

