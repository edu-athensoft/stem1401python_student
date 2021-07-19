"""
Entry

"""

from tkinter import *
from tkinter import messagebox as msg


def Infoentry1():
    global entry1
    print(f"Login account: {entry1.get()}")


def Infoentry2():
    global entry2
    print(f"Login password: {entry2.get()}")


root = Tk()
root.title("Python GUI - Login Form")
root.geometry("450x300")
root.configure(bg="black")

account = "issapro18"
password = 123

print(f"Account: {account}")
print(f"Password: {password}")

title = Label(root, text="Login Form", bg="black", fg="white", font="verdana 24")
title.pack(anchor=CENTER)

blank_space_0 = Label(root, bg="black")
blank_space_0.pack()

accountL = Label(root, text="Account:", bg="black", fg="white")
accountL.pack()

entry1 = Entry(root)
entry1.pack()

blank_space = Label(root, bg="black")
blank_space.pack()

passowrdL = Label(root, text="Password:", bg="black", fg="white")
passowrdL.pack()

entry2 = Entry(root, show="*")
entry2.pack()

blank_space_2 = Label(root, bg="black")
blank_space_2.pack()

login = Button(root, text='Login', command=lambda:[Infoentry1(), Infoentry2()])
login.pack()


if entry1.get() == account and entry2.get() == password:
    msg.showinfo("Form Result", "Login successfully.")
else:
    msg.showinfo("Form Result", "Error while login.")

blank_space_3 = Label(root, bg="black")
blank_space_3.pack()

quit_btn = Button(root, text="Quit", command=root.destroy)
quit_btn.pack()


root.mainloop()
