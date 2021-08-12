"""
Final exam part II - Issa

1. Writing a GUI program in Python tkinter for the registration process of a network application.
Basic requirements:
a. User can input a username --> done
b. User can input a password --> done
c. User can input a password for the second time to ensure user's password was input correctly --> done
d. User can input a validation code (usually an integer) generated randomly by the System, and that code (or number) should display on the window. If the user inputs the wrong code (or number), registration will fail and a messagebox should popup on the screen to warn the user. --> done
e. A text title for this application should be set properly on the interface. Note: It is not the title of the main window. --> done
f. A Button is required to perform registration once User finishes all inputs. Proper messages or information is required to display in both cases of 'success' and 'failed'. --> done
g. A second Button is required to perform reset (or clear all inputs on the window) --> done
h. Another Button is required to perform closing window and exit --> done
Hints:
Any layout manager is free to use.
To make a clean and concise layout for your GUI application.
Make a wireframe (or draft design) for your GUI
Assuming your application (program) is designed for a real scenario, therefore think about what previous experience you had in other online registration processes.

"""

from tkinter import *
from tkinter import messagebox as msg
import random


def login():
    if entry2.get() == entry3.get() and code == entry4.get():
        msg.showinfo("Form Result", "Login successfully.")
    else:
        msg.showerror("Form Result", "Wrong password, username or validation code. Please try again.")


def clearInfo():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)

root = Tk()
root.title("Form")
root.geometry("500x500")
root.configure(bg="black")
root.iconbitmap("./img/login.ico")

code = str(random.randint(1000, 9999))

# title
title = Label(root, text="Account Registration", bg="black", fg="white", font="verdana 24")
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
passwordL = Label(root, text="Password:", bg="black", fg="white")
passwordL.pack()

entry2 = Entry(root, show="*")
entry2.pack()

blank_space_2 = Label(root, bg="black")
blank_space_2.pack()

# entry of password 2
password2L = Label(root, text="Confirm password:", bg="black", fg="white")
password2L.pack()

entry3 = Entry(root, show="*")
entry3.pack()

blank_space_3 = Label(root, bg="black")
blank_space_3.pack()

# validation code
validation_code = Label(root, text=f"Your validation code: {code}", bg="black", fg="white", font="verdana 12")
validation_code.pack(anchor=CENTER)

confirm_code = Label(root, text="Confirm validation code:", bg="black", fg="white")
confirm_code.pack()

# entry of validation code
entry4 = Entry(root)
entry4.pack()

blank_space_4 = Label(root, bg="black")
blank_space_4.pack()

# button of login
login_btn = Button(root, text='Login', command=login, bg="white", fg="black")
login_btn.pack()

blank_space_5 = Label(root, bg="black")
blank_space_5.pack()

# button of clear
clear_btn = Button(root, text="Clear", bg="white", fg="black", command=clearInfo)
clear_btn.pack()

blank_space_5 = Label(root, bg="black")
blank_space_5.pack()


# button of exit
quit_btn = Button(root, text="Exit", bg="white", fg="black", command=root.destroy)
quit_btn.pack()

root.mainloop()
