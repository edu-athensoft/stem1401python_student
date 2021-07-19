"""
Entry

"""

from tkinter import *
from tkinter import messagebox as msg


def infoentry1():
    global entry1
    print(f"Login account: {entry1.get()}")


def infoentry2():
    global entry2
    print(f"Login password: {entry2.get()}")


def login():
    # print("test login()")
    infoentry1()
    infoentry2()
    if entry1.get() == account and entry2.get() == password:
        msg.showinfo("Form Result", "Login successfully.")
    else:
        msg.showerror("Form Result", "Error! Invalid username or password.")


# main program
root = Tk()
root.title("Python GUI - Login Form")
root.geometry("450x300")
root.configure(bg="black")

# presetting
account = "issapro18"
# password = 123
password = '123'

print(f"Account: {account}")
print(f"Password: {password}")

# title
title = Label(root, text="Login Form", bg="black", fg="white", font="verdana 24")
title.pack(anchor=CENTER)

blank_space_0 = Label(root, bg="black")
blank_space_0.pack()

# entry of account
accountL = Label(root, text="Account:", bg="black", fg="white")
accountL.pack()

entry1 = Entry(root)
entry1.pack()

blank_space = Label(root, bg="black")
blank_space.pack()

# entry of password
passowrdL = Label(root, text="Password:", bg="black", fg="white")
passowrdL.pack()

entry2 = Entry(root, show="*")
entry2.pack()

blank_space_2 = Label(root, bg="black")
blank_space_2.pack()

# button of login
login = Button(root, text='Login', command=login)
login.pack()

blank_space_3 = Label(root, bg="black")
blank_space_3.pack()

# button of quit
quit_btn = Button(root, text="Quit", command=root.destroy)
quit_btn.pack()


root.mainloop()
