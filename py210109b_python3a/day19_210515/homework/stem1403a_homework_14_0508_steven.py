"""


"""

import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title('Python')
window.geometry('300x150')

l = tk.Label(window, bg = "lightyellow", width=20,  text='Please choose your roles')
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0):
        print("Mage")
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0):
        print("Warrior")
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1):
        print("Archer")
    elif (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 0):
        print("Mage/Warrior")
    elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 1):
        print("Mage/Archer")
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 1):
        print("Warrior/Archer")
    elif (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 1):
        print("Mage/Warrior/Archer")
    else:
        print("Nothing")




var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

c1 = tk.Checkbutton(window, text='Mage', variable=var1, onvalue=1, offvalue=0)
c1.pack()
c2 = tk.Checkbutton(window, text='Warrior', variable=var2, onvalue=1, offvalue=0)
c2.pack()
c3 = tk.Checkbutton(window, text='Archer', variable=var3, onvalue=1, offvalue=0)
c3.pack()

btn1 = Button(window, text="OK", command=print_selection)
btn1.pack()
window.mainloop()