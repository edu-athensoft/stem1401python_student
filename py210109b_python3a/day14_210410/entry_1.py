"""
Entry
widget

for user input from keyboard
"""

from tkinter import *

root = Tk()
root.title('Python GUI - Entry')
root.geometry("320x240+200+200")
root.config(bg='#ddddff')

# create Entry for username
label1 = Label(root, text="Username")
label1.grid(row=0, column=0,padx=(50,5))

entry1 = Entry(root)
entry1.grid(row=0, column=1)

# create Entry for password
label2 = Label(root, text="Password")
label2.grid(row=1, column=0,padx=(50,5))

entry2 = Entry(root)
entry2.grid(row=1, column=1)

root.mainloop()

