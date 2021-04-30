"""
Homework 14
Emprunter: Max Yang

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
from tkinter.ttk import Separator

def login(un, pw):
    if un == username and pw == password:
        print(f"You've Account: {accountE.get()}"),
        print(f"You've Password: {passwordE.get()}")
        print("Login successful")

    else:
        print(f"You've Account: {accountE.get()}"),
        print(f"You've Password: {passwordE.get()}")
        print("Wrong username or password")

def printInfo():
    print(f"You've Account: {accountE.get()}"),
    print(f"You've Password: {passwordE.get()}")

root = Tk()
root.title("Python GUI - Entry")
root.geometry("600x430")

message = Label(root)

username = "admin"
password = "123456"

# Head
digit_label1 = Label(root,text="Login Form",
                padx='10', pady='20',
                font = "Helvetic 30 bold")
digit_label1.pack()

# Separ
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, padx=5, pady=40)

# Body
accountL = Label(root, text="Account :")
accountL.pack()

passwordL = Label(root, text="Password :")
passwordL.pack()

accountE = Entry(root)
accountE.pack()

passwordE = Entry(root, show='*')
passwordE.pack()

showBtn = Button(root, text='Get Account', command=lambda: login(accountE.get(), passwordE.get()))
showBtn.pack()

# Separ
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, padx=5, pady=40)

# Foot
digit_label3 = Label(root,text="Copyright 2021 Athensoft Inc.",
                     fg = 'black', font = "30")

digit_label3.pack()

root.mainloop()