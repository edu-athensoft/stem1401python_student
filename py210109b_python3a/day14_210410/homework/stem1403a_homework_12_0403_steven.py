"""
Homework 12
Description
Max value and Min value
1. User can press '+' button to increase the number by one per click
2. User can press '-' button to decrease the number by one per click
3. The number shows in a Label
constraints:
the MAX value = 10,
the MIN value = -10,
default number = 0
default step number = 1,  step number is adjustable
Due date: by the end of next Friday
"""

from tkinter import *

MAX = 10
MIN = -10
plus = 2
value = 0

def add():
    global value
    value += plus
    if value >= MAX:
        btn1.config(state='disabled')
        btn2.config(state='active')

    else:
        btn1.config(state='active')
        btn2.config(state='disabled')
    label1.config(text=str(value))


def sub():
    global value
    value -= plus
    if value <= MIN:
        btn1.config(state='active')
        btn2.config(state='disabled')

    else:
        btn1.config(state='disabled')
        btn2.config(state='active')
    label1.config(text=str(value))


root = Tk()
root.geometry("706x480+300+300")
root.title("Python Buttons")
root.config(bg="#dddfff")

label1 = Label(root, text=int(0), font ="Helvetica 20 bold", bg="yellow", width=20, height=5)
label1.grid(row=0, column = 1)

btn1 = Button(root, text="+", font ="Helvetica 20 bold", bg="cyan", command = add, width=10, height=1)
btn1.grid(row=1, column = 0)

btn2 = Button(root, text="-", font ="Helvetica 20 bold", bg="cyan", command = sub, width=10, height=1)
btn2.grid(row=1, column = 1)

btn3 = Button(root, text="Exit", font ="Helvetica 20 bold", bg="cyan", command = root.destroy, width=10, height=1)
btn3.grid(row=1, column = 2)



root.mainloop()