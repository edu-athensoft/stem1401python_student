"""
Entry

# insert by index of position
# pass a parameter
#
# using lambda function

1. Finish entry_05_insert_2_lambda.py
Requirements:
Input a string  (the 1st Entry)
Input position number (the 2nd Entry)
Click on Insert lambda button and get the new string with inserted content at the specified position
Show the modified string on console
Show the modified string on the first Entry
Due date: by the end of next Friday

"""

from tkinter import *

root = Tk()
root.title("Python GUI - Entry")
root.geometry("360x160")


def printInfo():
    print(f"You've input: {entry1.get()}")


def insertInfo():
    entry1.insert(2,"-insert-")
    print(f"You've input: {entry1.get()}")


### explain
def insertInfoLambda(pos):
    print(f"You've input: {entry1.get()}")
    print(f"Position: {pos}")
    print()

    res = entry1.insert(pos,"-insert-")
    print(res)
    # return entry1.insert(pos,"-insert-")


def clearInfo():
    # entry1.delete(0, END)         # remove a whole string
    # delete substring by range
    first = 2
    # last = 6
    last = None
    entry1.delete(first,last)       # remove chars in a range
    entry1.delete(first,None)       # remove one char
    entry2.delete(0, END)


temp_label = Label(root, text="")


def getPos():
    global temp_label

    pos = entry2.get()
    if pos == '':
        pos = 0
        insertInfoLambda(pos)
    else:
        try:
            pos = int(pos)
            insertInfoLambda(pos)
            temp_label.config(text="")
        except ValueError:
            temp_label.config(text="Position must be an integer")
            temp_label.grid(row=6, column=1, columnspan=3)



number = Label(root, text="Input")
number.grid(row=2, column=0, padx=(25, 5), sticky='e')

entry1 = Entry(root)
entry1.grid(row=2, column=1, padx=(5, 25), columnspan=3)

# pos
position = Label(root, text="Position")
position.grid(row=3, column=0, padx=(25, 5), sticky='e')

entry2 = Entry(root)
entry2.grid(row=3, column=1, padx=(5, 25), columnspan=3)

printbtn = Button(root, text="Print", command = printInfo)
printbtn.grid(row=4, column= 1, sticky="w")

insertbtn = Button(root, text="Insert normal", command=insertInfo)
insertbtn.grid(row=4, column= 2, sticky="w")

# posbtn = Button(root, text="Get pos", command=getPos)
# insertbtn.grid(row=4, column= 3, sticky="w")


insertbtn = Button(root, text="Insert lambda", command=getPos)
insertbtn.grid(row=4, column= 3, sticky="w")

clearbtn = Button(root, text="Clear", command=clearInfo)
clearbtn.grid(row=5, column= 2, sticky="we")

quitbtn = Button(root, text="Quit", command=root.destroy)
quitbtn.grid(row=5, column= 3, sticky="we")


root.mainloop()