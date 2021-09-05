from tkinter import *

# Tkinter Initialization.
root = Tk()
root.geometry("800x600")
root.title("Rock Paper Scissors Game")

# Buttons to select Rock, Paper, Scissors.
frame = Frame(root, bg="grey")

Button(frame, text="Rock", bg="light blue",
       width=20, height=2).pack(pady=8)
Button(frame, text="Paper", bg="pink", width=20,
       height=2).pack(pady=8)
Button(frame, text="Scissor", bg="light green",
       width=20, height=2).pack(pady=8)

frame.pack(fill=X, pady=20)

root.mainloop()
