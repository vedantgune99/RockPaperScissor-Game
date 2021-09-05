from tkinter import *


def onClickRock():
    move = rock['text']


def onClickPaper():
    move = paper['text']


def onClickScissor():
    move = scissor['text']


# Tkinter Initialization.
root = Tk()
root.geometry("800x600")
root.title("Rock Paper Scissors Game")

# Buttons to select Rock, Paper, Scissors.
frame = Frame(root, bg="grey")

rock = Button(frame, text="Rock", bg="light blue",
              width=20, height=2, command=onClickRock)
rock.pack(pady=8)

paper = Button(frame, text="Paper", bg="pink", width=20,
               height=2, command=onClickPaper)
paper.pack(pady=8)

scissor = Button(frame, text="Scissor", bg="light green",
                 width=20, height=2, command=onClickScissor)
scissor.pack(pady=8)

frame.pack(fill=X, pady=20)

Label(root, text=" Game Stats ", font="consolas 20").pack(padx=20)
Frame(root, bg="red", relief=SUNKEN).pack(fill=BOTH, pady=10)

result = Frame(root, bg="light gray", padx=2, pady=2)
Label(result, text="Your Choice : ", font="consolas 15 bold").pack()
Label(result, text="CPU Choice : ", font="consolas 15 bold").pack()
Label(result, text="Game Status : ", font="consolas 15 bold").pack()
result.pack(fill=BOTH)


root.mainloop()
