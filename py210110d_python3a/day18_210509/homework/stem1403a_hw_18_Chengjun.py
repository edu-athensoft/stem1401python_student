"""
[Homework]
4:16
Date : 2021-05-02
Rewrite and try out Checkbutton
Understanding the sample code above
Due date: By the end of next Sat.
"""

from tkinter import *


def printOption():
    print(roles[var.get()])


root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry("320x140")
roles = {10: 'Mage', 20: 'Warrior', 30: 'Archer'}

var = IntVar()
var.set(20)

label = Label(root, text="Choose your role", bg="lightyellow", width=30)
label.pack()

for num, rolename in roles.items():
    Radiobutton(root, text=rolename, variable=var, value=num).pack()

Button(root, text="OK", width=10, command=printOption).pack()

root.mainloop()
