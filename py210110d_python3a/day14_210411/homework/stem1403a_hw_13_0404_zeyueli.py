"""
[Challenge]  Project. Volume Controller
c04_button/button_03_b.py
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
"""

from tkinter import *


def add(multiplier):
    global number
    number += step_number*multiplier
    if number >= MAX:
        number = MAX
        plus_btn.config(state="disabled")
    else:
        plus_btn.config(state="normal")
    if number <= MIN:
        number = MIN
        minus_btn.config(state="disabled")
    else:
        minus_btn.config(state="normal")
    num_label.config(text=number)


root = Tk()
root.title("Python GUI - Volume Controller")
root.geometry("540x480")
root.config(bg="#ddddff")

MAX = 10
MIN = -10
number = 0
step_number = 1

num_label = Label(root, bg="gray", text=number, width=100, height=10, font=("Arial", 30))
num_label.pack()

minus_btn = Button(root, text="-", width=20, height=3, command=lambda: add(-1))
minus_btn.pack(side=LEFT)

plus_btn = Button(root, text="+", width=20, height=3, command=lambda: add(1))
plus_btn.pack(side=LEFT)

exit_btn = Button(root, text="Exit", width=40, height=3, command=root.destroy)
exit_btn.pack(side=LEFT, fill=X)

root.mainloop()
