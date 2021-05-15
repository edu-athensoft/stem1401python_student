"""
Homework 17

"""
from tkinter import *


def printOption(value):
    print(value)


def all_options():
    global options
    options.set('')
    if btn1.get():
        options.set(options.get() + 'Mage ')
    if btn2.get():
        options.set(options.get() + 'Warrior ')
    if btn3.get():
        options.set(options.get() + 'Archer ')


root = Tk()
root.title("Python GUI - Checkbutton")
root.geometry("320x120+300+200")
btn1 = IntVar()
btn2 = IntVar()
btn3 = IntVar()
options = StringVar()
options.set('Please choose your roles')

roles = Label(root, bg="lightyellow", width=30, font='Helvetica 16', textvariable=options).pack()

checkbtn1 = Checkbutton(root, text='Mage', variable=btn1, onvalue=1, offvalue=0).pack()
checkbtn2 = Checkbutton(root, text='Warrior', variable=btn2, onvalue=1, offvalue=0).pack()
checkbtn3 = Checkbutton(root, text='Archer', variable=btn3, onvalue=1, offvalue=0).pack()

confirm = Button(root, text='Confirm', command=lambda: all_options()).pack()

root.mainloop()
