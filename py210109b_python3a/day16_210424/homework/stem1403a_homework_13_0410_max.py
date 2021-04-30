"""
Homework 13

Date: 2021-04-10
Design and write program for a login form
Requirements:
A GUI interface
Preset the username is 'admin' and the password is '123456'
User may input username
User may input password, and the password should show mask char ('*') instead
If the user's input matches the presetting, then the program shows a text message (info) box with the words 'login successfully!'
otherwise, the program shows a text message (error) box with the words 'wrong username or password!'
Due date: by the end of next Friday
"""

from tkinter import *
from tkinter import messagebox as msg

root = Tk()
root.title("Python GUI - Entry")
root.geometry("300x160")


def login(un, pw):
    if un == username and pw == password:
        msg.showinfo("Login", "Login successful!")
    else:
        msg.showerror("Login", "Wrong username or password. Please try again.")


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
