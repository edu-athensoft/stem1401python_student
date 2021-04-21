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

value = 0
step = 1

def plus():
    limit = 10

    global value
    value += step

    btn_value.config(text=value)

    if value >= limit:
        btn_plus.config(state='disabled')

    else:
        btn_minus.config(state='active')


def minus():
    global value
    value -= step
    limit = -10
    btn_value.config(text=value)
    if value <= limit:
        btn_minus.config(state='disabled')
    else:
        btn_plus.config(state='active')


root = Tk()
root.title('Python GUI - Button')
root.geometry("320x240+200+200")
root.config(bg='#ddddff')

btn_value = Label(root, text=value, font="Helvetica 100", bg="#ddddff")
btn_value.pack()


btn_plus = Button(root, text='+', height=3, width=16, command=lambda: plus())
btn_plus.pack(anchor=S, side=LEFT)

btn_minus = Button(root, text='-', height=3, width=16, command=lambda: minus())
btn_minus.pack(anchor=S, side=LEFT)


btn_exit = Button(root, text='Exit', height=3, width=10, command=lambda: root.destroy())
btn_exit.pack(anchor=S, side=RIGHT,)
root.mainloop()