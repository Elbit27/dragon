from tkinter import Tk, PanedWindow, Label

def on_sash_drag(event):
    print("Sash dragged!")

root = Tk()
root.title("PanedWindow Example")

# Create a PanedWindow with two panes
paned_window = PanedWindow(root, orient="horizontal")
paned_window.pack(fill="both", expand=True)

# Create labels for the panes
pane1 = Label(paned_window, text="Pane 1", background="lightblue")
pane2 = Label(paned_window, text="Pane 2", background="lightgreen")

# Add panes to the PanedWindow
paned_window.add(pane1)
paned_window.add(pane2)

# Bind the on_sash_drag function to the sash drag event
paned_window.bind("<B1-Motion>", on_sash_drag)

root.mainloop()
