import tkinter as tk
# Function to change the label text
def change_label_text():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Label and Button Example")

# Create a label widget
label = tk.Label(root, text="Tkinter Exercises (Label Text)")
label.pack(padx=20, pady=20)

# Create a button widget
button = tk.Button(root, text="Click Me", command=change_label_text)
button.pack()

# Start the Tkinter main loop
root.mainloop()