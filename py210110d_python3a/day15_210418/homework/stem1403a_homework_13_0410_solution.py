"""
Homework 13
"""

from tkinter import *
from tkinter import messagebox as msgbox

root = Tk()
root.title("Python GUI - Entry")
root.geometry("300x160")

message = Label(root)


def login(un, pw):
    if un == username and pw == password:
        message.config(text="Login successful")
        msgtitle = "Message"
        txt = "Login successfully!"
        # msgbox.showinfo(msgtitle,txt)
    else:
        message.config(text="Wrong username or password")
        msgtitle = "Error"
        txt = "Wrong username or password!"
        # msgbox.showerror(msgtitle,txt)
        # msgbox.showinfo(msgtitle,txt)

    msgbox.showeinfo(msgtitle,txt)
    message.grid(row=3, column=0, columnspan=2, sticky='n')


username = "admin"
password = "123456"

accountL = Label(root, text="Username: ")
accountL.grid(row=0, column=0, padx=(50, 0))

accountE = Entry(root)
accountE.grid(row=0, column=1)

passwordL = Label(root, text="Password: ")
passwordL.grid(row=1, column=0, padx=(50, 0))

passwordE = Entry(root, show='*')
passwordE.grid(row=1, column=1)

loginbtn = Button(root, text="Login", command=lambda: login(accountE.get(), passwordE.get()))
loginbtn.grid(row=2, column=1, sticky='w')

root.mainloop()
