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

digit = 0

step_number = 2
MAX = 10
MIN = -10

def add():
    global digit
    if digit == -10:
        minus_button.config(state="normal")
    digit += step_number
    num.config(text=digit)
    if digit == 10:
        plus_button.config(state="disabled")


def sub():
    global digit
    if digit == 10:
        plus_button.config(state="normal")
    digit -= step_number
    num.config(text=digit)
    if digit == -10:
        minus_button.config(state="disabled")



root = Tk()
root.title("number")
root.geometry("440x380")
root.config(bg="#ddddff")
root.resizable(0, 0)

num = Label(root, bg="gray", text=digit, width=60, height=10, font=("Arial",20))
num.pack()

minus_button = Button(root, text="-", width=20, height=4, relief="raised", command=sub)
minus_button.pack(side=LEFT)

plus_button = Button(root, text="+", width=20, height=4, relief="raised",command=add)
plus_button.pack(side=LEFT)

exit_button = Button(root, text="Exit", width=20, height=4,relief="raised", command=root.destroy)
exit_button.pack(side=RIGHT)

root.mainloop()