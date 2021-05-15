"""
Checkbutton

get()
dictionary
variable, BooleanVar()
"""

from tkinter import *


def printInfo():
    selection = ""
    for i in checkboxes:
        if checkboxes[i].get() == True:
            selection += roles[i] + ","
    print(selection)


# main program
root = Tk()
root.title("Python GUI - Checkbutton")
root.geometry("320x240")

# label
label = Label(root, text="Please choose your roles", bg="lightyellow", width=30, font=('Helvetica',16))
label.pack()

# data, dictionary
roles = {0: 'Mage', 1: 'Warrior', 2: 'Archer'}
checkboxes = {}

for i in range(len(roles)):
    checkboxes[i] = BooleanVar()
    Checkbutton(root, text=roles[i], variable=checkboxes[i], font=('Helvetica',16)).pack()

# for i in range(3):
#     checkboxes[i] = BooleanVar()
#     Checkbutton(root, text=roles[i], variable=checkboxes[i], font=('Helvetica', 16)).pack()

# checkboxes[0] = BooleanVar()
# Checkbutton(root, text=roles[0], variable=checkboxes[0], font=('Helvetica', 16)).pack()
# # text = Mage
#
# checkboxes[1] = BooleanVar()
# Checkbutton(root, text=roles[1], variable=checkboxes[1], font=('Helvetica', 16)).pack()
#
# checkboxes[2] = BooleanVar()
# Checkbutton(root, text=roles[2], variable=checkboxes[2], font=('Helvetica', 16)).pack()



Button(root, text="OK", width=10, command=printInfo, font=('Helvetica',16)).pack()

root.mainloop()
