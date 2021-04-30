"""
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


def printInfo():
    print(f"You've input: {entry1.get()} for username")
    print(f"You've input: {entry2.get()} for password")


def login(un, pw):
    if un == username and pw == password:
        title = "Info"
        text = "Login successfully"
        msg.showinfo(title, text)
    else:
        title = "Error"
        text = "Wrong username or password"
        # msg.showinfo(title, text)
        msg.showerror(title, text)

# main program
# root = Tk()
# message = Label(root)

username = "admin"
password = "12345"

root = Tk()
root.title('Python GUI - Button')
root.geometry("320x240+200+200")
root.config(bg='#ddddff')

label1 = Label(root, text="Username")
label1.grid(row=0, column=0, padx=(50, 5))

# create Entry
entry1 = Entry(root)
entry1.grid(row=0, column=1)

label2 = Label(root, text="Password")
label2.grid(row=1, column=0, padx=(50, 5))

entry2 = Entry(root, show="*")
entry2.grid(row=1, column=1)

printbtn = Button(root, text="Print", command=lambda: login(entry1.get(), entry2.get()))
printbtn.grid(row=4, column=1, sticky="w")

root.mainloop()
