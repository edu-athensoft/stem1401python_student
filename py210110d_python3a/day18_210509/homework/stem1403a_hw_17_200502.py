"""
[Homework]
Date : 2021-05-02
Rewrite and try out Checkbutton
Understanding the sample code above
Due date: By the end of next Sat.
"""

from tkinter import *


def printRoles():
    role = ""
    for i in checkboxes:
        if checkboxes[i].get() == True:
            role += roles[i] + "\n"
    print(role)


# main program
root = Tk()
root.title("Python GUI - Homework")

label = Label(root, text="Please choose your roles:")
label.pack()

roles = {0: "Mage", 1: "Warrior", 2: "Archer"}
checkboxes = {}

for i in range(len(roles)):
    checkboxes[i] = BooleanVar()
    Checkbutton(root, text=roles[i], variable=checkboxes[i]).pack()
Button(root, text="Print selected roles", command=printRoles).pack()

root.mainloop()
