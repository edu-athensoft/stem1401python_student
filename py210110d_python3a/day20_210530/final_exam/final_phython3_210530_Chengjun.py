"""
1. Writing a GUI program in Python tkinter for the registration process of a network application.

Basic requirements:
a. User can input a username
b. User can input a password
c. User can input a password for the second time to ensure user's password was input correctly
d. User can input a validation code (usually an integer) generated randomly by the System, and that code (or number) should display on the window. If the user inputs the wrong code (or number), registration will fail and a messagebox should popup on the screen to warn the user.
e. A text title for this application should be set properly on the interface. Note: It is not the title of the main window.
f. A Button is required to perform registration once User finishes all inputs. Proper messages or information is required to display in both cases of 'success' and 'failed'.
g. A second Button is required to perform reset (or clear all inputs on the window)
h. Another Button is required to perform closing window and exit

Hints:
Any layout manager is free to use.
To make a clean and concise layout for your GUI application.
Make a wireframe (or draft design) for your GUI
Assuming your application (program) is designed for a real scenario, therefore think about what previous experience you had in other online registration processes.
"""
from tkinter import *
from tkinter import messagebox as msg, Label
import random

root = Tk()
root.title("Entry")
root.geometry("600x200")


def pwd():
    title = "Login log"
    if password.get() == password2.get() and (x == int(Random.get())):
        text = "Glad for your join"
        msg.showinfo(title, text)
    else:
        text = "please recheck the passwords or the verification code"
        msg.showerror(title, text)


def clear():
    account.delete(0, 'end')
    password.delete(0, 'end')
    password2.delete(0, 'end')
    Random.delete(0, 'end')


def windows(enter):
    window = Toplevel(root)
    window.title(enter)
    window.geometry("160x80")
    window.mainloop()


x = random.randint(999, 10000)


name = Label(root, text="SHOPPER SUPREME-----REGISTERED PAGE", bg="Yellow")
name.grid(row=2, columnspan=1, padx=(0, 0), sticky="we")

accountL = Label(root, text="Account ")
accountL.grid(row=3, columnspan=1, padx=(0, 10), sticky="w")

Pwd = Label(root, text="Password ")
Pwd.grid(row=4, columnspan=1, padx=(0, 10), sticky="w")

Pwd2 = Label(root, text="verification of the password ")
Pwd2.grid(row=5, columnspan=1, padx=(0, 10), sticky="w")

random_n = Label(root, text="verification code:")
random_n.grid(row=6, columnspan=1, padx=(0, 10), sticky="w")


text_random = Label(root, text=x)
text_random.grid(row=6, columnspan=2, padx=(100, 10), sticky="w")


Random = Entry(root, width=10)
Random.grid(row=6, columnspan=3, padx=(300, 450), sticky="we")


account = Entry(root, width=20)
account.grid(row=3, columnspan=2, padx=(300, 400), sticky="we")

password = Entry(root, width=20)
password.grid(row=4, columnspan=2, padx=(300, 400), sticky="we")

password2 = Entry(root, width=20)
password2.grid(row=5, columnspan=2, padx=(300, 400), sticky="we")

enter_button = Button(root, text='join', command=pwd)
enter_button.grid(row=8, columnspan=1, padx=(0, 100))

clear_button = Button(root, text="Delete", command=clear)
clear_button.grid(row=8, columnspan=2, padx=(200, 400))

close_button = Button(root, text='exit', command=root.destroy)
close_button.grid(row=8, columnspan=4, padx=(400, 500))

help_button = Button(root, command=lambda enter="Help": windows(enter), text="Help", relief='raised', height=1,
                     width=5, padx=5, pady=5, font='Times 12 bold')
help_button.grid(row=9, columnspan=4, padx=(250, 300), sticky="w")

root.mainloop()
