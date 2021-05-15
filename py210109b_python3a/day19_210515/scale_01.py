"""
Scale

basic usage of Scale

get value via Scale object

['activebackground', 'background', 'bigincrement', 'bd', 'bg',
'borderwidth', 'command', 'cursor', 'digits', 'fg',
'font', 'foreground', 'from', 'highlightbackground', 'highlightcolor',
'highlightthickness', 'label', 'length', 'orient', 'relief',
'repeatdelay', 'repeatinterval', 'resolution', 'showvalue', 'sliderlength',
'sliderrelief', 'state', 'takefocus', 'tickinterval', 'to', 'troughcolor', 'variable', 'width']

"""

from tkinter import *


def printValue():
    # print("print value 1",scale1.get())
    print("print value 1",var1.get())


def printValue2():
    print("print value 2",scale2.get())


# main program
root = Tk()
root.title("Python GUI - Scale")
root.geometry("640x480")

# label
label = Label(root, text="A simple demo of Scale", bg="lightyellow", width=30)
label.pack()

var1 = IntVar()
scale1 = Scale(root, from_=0, to=100, variable=var1)
scale1.pack()

Button(root, text="Print value of Scale #1", width=20, command=printValue).pack()


var2 = IntVar()
scale2 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
scale2.pack()

Button(root, text="Print value of Scale #2", width=20, command=printValue2).pack()

# check and get all available options of Scale object
print(scale1.keys())

root.mainloop()
