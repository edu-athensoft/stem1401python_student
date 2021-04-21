"""

"""
from tkinter import *
from tkinter import messagebox as msg


def printInfo():
    print(f"You've input: {entry1.get()} for username")
    print(f"You've input: {entry2.get()} for password")


def good():
    title = "MSG box"
    text = "Login successful"
    msg.showinfo(title, text)


def bad():
    title = "MSG box"
    text = "Wrong username or password"
    msg.showinfo(title, text)


# main program
root = Tk()
root.title('Python GUI - Button')
root.geometry("320x240+200+200")
root.config(bg='#ddddff')

# label
label1 = Label(root, text="Username")
label1.grid(row=0, column=0, padx=(50, 5))

# create Entry
entry1 = Entry(root)
entry1.grid(row=0, column=1)

label2 = Label(root, text="Password")
label2.grid(row=1, column=0, padx=(50, 5))

entry2 = Entry(root, show="*")
entry2.grid(row=1, column=1)

printbtn = Button(root, text="Print", command=printInfo)
printbtn.grid(row=4, column=1, sticky="w")

root.mainloop()
