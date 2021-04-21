"""
Homework 13

Date: 2021-04-03
[Challenge]  Volume Controller
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
Due date: by the end of next Friday
"""

from tkinter import *

def plus():
    global value
    value += 1
    if value > 10:
        btn_1.config(state='disabled')
        btn_2.config(state='active')


    else:
        btn_1.config(state='active')
        btn_2.config(state='disabled')
        num_screen.config(text=str(value))

def sub():
    global value
    value += -1
    if value < -10:
        btn_1.config(state='active')
        btn_2.config(state='disabled')

    else:
        btn_1.config(state='disabled')
        btn_2.config(state='active')
    num_screen.config(text=str(value))

root = Tk()
root.title('Python GUI - Button')
root.geometry('320x240+300+300')
root.config(bg='#ddddff')

value = 0

num_screen = Label(root, text=str(value), font="Helvetica 100", padx=20, pady=10)
num_screen.pack()

btn_1 = Button(root, text="+", padx=10, command=lambda:plus())
btn_1.pack(anchor=S, side=LEFT)

btn_2 = Button(root, text="-", padx=10, command=lambda:sub())
btn_2.pack(anchor=S, side=LEFT)

btn_close = Button(root, text="Close", padx=10, command=root.destroy)
btn_close.pack(anchor=S, side=RIGHT)

root.mainloop()