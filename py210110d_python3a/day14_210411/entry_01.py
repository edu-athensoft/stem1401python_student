"""
Entry
padx(left, right)

"""

from tkinter import *

root = Tk()
root.title("Python GUI - Entry")
root.geometry("340x200")

accountL = Label(root, text="Account ")
accountL.grid(row=2,padx=(50,5), sticky='e')

passwordL = Label(root, text="Password ")
passwordL.grid(row=3,padx=(50,5), sticky='e')

accountE = Entry(root, width=20, font=(24))
accountE.grid(row=2, column=1, padx=(5, 50))

passwordE = Entry(root, show='?', width=20, font=(24))
passwordE.grid(row=3, column=1, padx=(5, 50))

root.mainloop()
