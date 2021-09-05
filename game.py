from tkinter import *
from random import choice

ChoiceList = ["rock", "paper", "scissor"]

# Function to determine Win/Lose.


def gameState(move, cpu_move):
    if (move == "rock" and cpu_move == "paper"):
        state = "CPU Won"
        user_choice['text'] = "Your Choice : " + move
        cpu_choice['text'] = "CPU Choice : " + cpu_move
        status['text'] = "Game State : " + state

    elif (move == "rock" and cpu_move == "scissor"):
        state = "User Won"
        user_choice['text'] = "Your Choice : " + move
        cpu_choice['text'] = "CPU Choice : " + cpu_move
        status['text'] = "Game State : " + state

    elif (move == "paper" and cpu_move == "rock"):
        state = "User Won"
        user_choice['text'] = "Your Choice : " + move
        cpu_choice['text'] = "CPU Choice : " + cpu_move
        status['text'] = "Game State : " + state

    elif (move == "paper" and cpu_move == "scissor"):
        state = "CPU Won"
        user_choice['text'] = "Your Choice : " + move
        cpu_choice['text'] = "CPU Choice : " + cpu_move
        status['text'] = "Game State : " + state

    elif (move == "scissor" and cpu_move == "paper"):
        state = "User Won"
        user_choice['text'] = "Your Choice : " + move
        cpu_choice['text'] = "CPU Choice : " + cpu_move
        status['text'] = "Game State : " + state

    elif (move == "scissor" and cpu_move == "rock"):
        state = "CPU Won"
        user_choice['text'] = "Your Choice : " + move
        cpu_choice['text'] = "CPU Choice : " + cpu_move
        status['text'] = "Game State : " + state

    else:
        state = "Match Draw"
        user_choice['text'] = "Your Choice : " + move
        cpu_choice['text'] = "CPU Choice : " + cpu_move
        status['text'] = "Game State : " + state


# Clicked on Rock.
def onClickRock():
    move = rock['text'].lower()
    cpu_move = choice(ChoiceList)
    gameState(move, cpu_move)


# Clicked on Paper.
def onClickPaper():
    move = paper['text'].lower()
    cpu_move = choice(ChoiceList)
    gameState(move, cpu_move)


# Clicked on Scissor.
def onClickScissor():
    move = scissor['text'].lower()
    cpu_move = choice(ChoiceList)
    gameState(move, cpu_move)


# Tkinter Initialization.
root = Tk()
root.geometry("350x500")
root.minsize(320, 450)
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

# Horizontal Red Line...
Label(root, text=" Game Stats ", font="consolas 20").pack(padx=20)
Frame(root, bg="red", relief=SUNKEN).pack(fill=BOTH, pady=10)

result = Frame(root, bg="light gray", padx=2, pady=2)
user_choice = Label(result, font="consolas 15 bold")
user_choice.pack()
cpu_choice = Label(result, font="consolas 15 bold")
cpu_choice.pack()
status = Label(result, font="consolas 15 bold")
status.pack()
result.pack(fill=BOTH)


root.mainloop()
