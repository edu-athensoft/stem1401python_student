"""
[Homework]
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


def showPwd():
    entryobj = passwordE
    entryobj['show'] = ''


def hidePwd():
    entryobj = passwordE
    entryobj['show'] = '*'


def getInfo():
    logininfo = accountE.get()
    passwordinfo = passwordE.get()
    title = 'login information'
    if logininfo == username and passwordinfo == password:
        text = 'login successfully'
        msg.showinfo(title, text)
    else:
        text = 'wrong username or password!'
        msg.showerror(title, text)


username = 'admin'
password = '123456'

accountL = Label(root, text="Account ")
accountL.grid(row=2, padx=(50, 5), sticky='e')
passwordL = Label(root, text="Password ")
passwordL.grid(row=3, padx=(50, 5), sticky='e')
accountE = Entry(root)
accountE.grid(row=2, column=1, padx=(5, 50))
passwordE = Entry(root, show='*')
passwordE.grid(row=3, column=1, padx=(5, 50))
showBtn = Button(root, text='Show password', command=showPwd)
showBtn.grid(row=4, column=1)
showBtn = Button(root, text='Hide password', command=hidePwd)
showBtn.grid(row=5, column=1)
loginbtn = Button(root, text="login", command=getInfo)
loginbtn.grid(row=6, column=1)

root.mainloop()
