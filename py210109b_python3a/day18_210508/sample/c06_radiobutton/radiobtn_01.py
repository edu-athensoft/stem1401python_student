"""
Radiobutton

default option selected

"""

from tkinter import *

def printOption():
    label.config(text="I am a " + var.get() + ".")


root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry("320x240")

var = StringVar()
# var.set("Warrior")    # set a default selected option
var.set(None)       # select nothing

label = Label(root, text="Please choose a role", bg="lightyellow", width=30, font=('Helvetica',16))
label.pack()

radiobtn1 = Radiobutton(root, text="Mage", variable=var, value="Mage", command=printOption, font=('Helvetica',16))
radiobtn1.pack()

radiobtn2 = Radiobutton(root, text="Warrior", variable=var, value="Warrior", command=printOption, font=('Helvetica',16))
radiobtn2.pack()

radiobtn3 = Radiobutton(root, text="Archer", variable=var, value="Archer", command=printOption, font=('Helvetica',16))
radiobtn3.pack()

root.mainloop()
