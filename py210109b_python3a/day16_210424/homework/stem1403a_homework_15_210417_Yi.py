"""
homework 15

Date: 2021-04-17

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

def insertInfoLambda():
    print(f"You've input: {entry1.get()}")
    # return lambda pos=getPos(): entry1.insert(pos,"-insert-")
    pos = getPos()
    entry1.insert(pos, "-insert-")
    print(f"You've new input: {entry1.get()}")

def printInfo():
    print(f"You've input: {entry1.get()}")

def insertInfo():
    entry1.insert(2,"-insert-")
    print(f"You've input: {entry1.get()}")

# def insertInfoLambda():
#     pos = getPos()
#     print(f"You've input: {entry1.get()}")
#     return lambda: entry1.insert(pos,"-insert-")

def clearInfo():
    entry1.delete(0, END)
    entry2.delete(0, END)

def getPos():
    pos = entry2.get()
    print(pos)
    return pos

root = Tk()
root.title("Python GUI - Entry")
root.geometry("380x180")

accountL = Label(root, text="Input :")
accountL.grid(row=2,padx=(80,5), sticky='e')

entry1 = Entry(root)
entry1.grid(row=2, column=1, padx=(5, 50), columnspan=3)

accountL1 = Label(root, text="Position :")
accountL1.grid(row=3,padx=(80,5), sticky='e')

entry2 = Entry(root)
entry2.grid(row=3, column=1, padx=(5, 50),columnspan=3)

printbtn = Button(root, text="Print", command = printInfo)
printbtn.grid(row=4, column= 1, sticky="w")

insertbtn = Button(root, text="Insert normal", command=insertInfo)
insertbtn.grid(row=4, column= 2, sticky="w")

# posbtn = Button(root, text="Get pos", command=getPos)
# insertbtn.grid(row=4, column= 3, sticky="w")
# if pos=='':
#     pos=0
# else:
#     pos = int(pos)

insertbtn = Button(root, text="Insert lambda", command=insertInfoLambda)
insertbtn.grid(row=4, column= 3, sticky="w")

clearbtn = Button(root, text="Clear", command=clearInfo)
clearbtn.grid(row=5, column= 2, sticky="we")

quitbtn = Button(root, text="Quit", command=root.destroy)
quitbtn.grid(row=5, column= 3, sticky="we")

root.mainloop()