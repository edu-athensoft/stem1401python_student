"""
Homework]
Date: 2021-05-08
Rewrite checkbutton program
Print out all options you checked
"""

from tkinter import *

def printInfo():
    print(f"You've Account: {cb_1.get()}")

root = Tk()
root.title("Python GUI - Checkbuttom")
root.geometry("520x180")


label1 = Label(root, text="Please shoose your roles", bg="yellow", width=30, font=("Arial", 16))
label1.pack()

cb_1 = Checkbutton(root, text="Mage", font=("Arial", 16))
cb_1.pack()

cb_2 = Checkbutton(root, text="Warrior", font=("Arial", 16))
cb_2.pack()

cb_3 = Checkbutton(root, text="Archer", font=("Arial", 16))
cb_3.pack()

btn_1 = Button(root, text="OK", width=10, command=printInfo, font=("Arial", 16))
btn_1.pack()

root.mainloop()