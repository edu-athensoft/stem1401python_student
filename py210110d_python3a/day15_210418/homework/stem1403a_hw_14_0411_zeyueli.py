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

username = "admin"
password = "123456"


def checknamepwd():
    title = "Login log"
    if username == accountE.get() and password == passwordE.get():
        text = 'login successfully!'
        msg.showinfo(title, text)
    else:
        text = 'wrong username or password!'
        msg.showerror(title, text)


root = Tk()
root.title("Python GUI - Entry")
root.geometry("340x200")

accountL = Label(root, text="Account ")
accountL.grid(row=2, padx=(50, 5), sticky="e")

passwordL = Label(root, text="Password ")
passwordL.grid(row=3, padx=(50, 5))

accountE = Entry(root, width=20)
accountE.grid(row=2, column=1, padx=(5, 50))

passwordE = Entry(root, show="*", width=20)
passwordE.grid(row=3, column=1, padx=(5, 50), sticky="e")

enter_button = Button(root, text="Confirm", command=checknamepwd)
enter_button.grid(row=4, columnspan=2)

root.mainloop()
