"""
Radiobutton
"""


from tkinter import *


def printOption():
    print("printOption")
    value = var.get()
    print(value)
    # label['text']=value

    # slice
    # value = value[value.find('-')+1:]

    # replace
    # value = value.replace('value-','')

    # split
    value = value.split('-')[-1]

    txt.set(value)


root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry("320x240+300+200")


txt = StringVar()
label = Label(root, text="Please choose a role", bg="lightyellow", width=30, font=('Helvetica',16),
              textvariable=txt)
label.pack()

# list all available options for the widget

print(label.keys())


var = StringVar()

# IntVar()
# DoubleVar()
# BooleanVar()

var.set(None)

# option 1
radiobtn1 = Radiobutton(root, text="Mage", value="value-Mage", font=('Helvetica',16),
                        variable=var,
                        command=printOption)
radiobtn1.pack()

# option 2
radiobtn2 = Radiobutton(root, text="Warrior", value="value-Warrior", font=('Helvetica',16),
                        variable=var,
                        command=printOption)
radiobtn2.pack()


# option 3
radiobtn3 = Radiobutton(root, text="Archer", value="value-Archer", font=('Helvetica',16),
                        variable=var,
                        command=printOption)
radiobtn3.pack()


root.mainloop()


