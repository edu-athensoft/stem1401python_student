"""
1. Writing a GUI program in Python tkinter for the registration process of a network application.

Basic requirements:
a. User can input a username
b. User can input a password
c. User can input a password for the second time to ensure user's password was input correctly
d. User can input a validation code (usually an integer) generated randomly by the System, and that code (or number)
should display on the window. If the user inputs the wrong code (or number), registration will fail and a messagebox
should popup on the screen to warn the user.
e. A text title for this application should be set properly on the interface. Note: It is not the title of the main
window.
f. A Button is required to perform registration once User finishes all inputs. Proper messages or information is
required to display in both cases of 'success' and 'failed'.
g. A second Button is required to perform reset (or clear all inputs on the window)
h. Another Button is required to perform closing window and exit

Hints:
Any layout manager is free to use.
To make a clean and concise layout for your GUI application.
Make a wireframe (or draft design) for your GUI
Assuming your application (program) is designed for a real scenario, therefore think about what previous experience you
had in other online registration processes.
"""

from tkinter import *
from tkinter import messagebox as msg
from random import *


def conf():
    global txt

    try:
        val = int(valid_input.get())
        if un_input.get() != '' and pw_input.get() == pw2_input.get() and val == num:
            txt.set("Login successful!")
            result.config(fg='green')

        elif un_input.get() == '':
            txt.set("Please enter a username.")
            result.config(fg='red')

        elif pw_input.get() != pw2_input.get():
            txt.set("Passwords do not match.")
            result.config(fg='red')

        elif val != num:
            msg.showerror("Wrong Validation Code", "Please enter the correct validation code.")



    except ValueError:
        msg.showerror("Wrong Validation Code", "Please enter the correct validation code.")



def clear():
    username.set("")
    password.set("")
    password2.set("")
    val_code.set("")
    txt.set("")





root = Tk()
root.geometry('320x160')
root.title("Login Form")

username = StringVar()
password = StringVar()
password2 = StringVar()
val_code = StringVar()

frame = LabelFrame(root, text="Sign In", font='Helvetica 10', labelanchor='n')

un = Label(frame, text='Username: ')
un.grid(row=0, column=0, sticky=E)

un_input = Entry(frame, textvariable=username, font='Helvetica 10')
un_input.grid(row=0, column=1)


pw = Label(frame, text='Password: ')
pw.grid(row=1, column=0, sticky=E)

pw_input = Entry(frame, textvariable=password, font='Helvetica 10')
pw_input.grid(row=1, column=1)


pw2 = Label(frame, text='Re-enter password: ')
pw2.grid(row=2, column=0, sticky=E)

pw2_input = Entry(frame, textvariable=password2, font='Helvetica 10')
pw2_input.grid(row=2, column=1)


num = randint(0, 99999)
code = StringVar()
code.set(f"Validation Code ({num}): ")

valid = Label(frame, textvariable=code)
valid.grid(row=3, column=0, sticky=E)

valid_input = Entry(frame, textvariable=val_code, font="Helvetica 10")
valid_input.grid(row=3, column=1)


txt = StringVar()
result = Label(frame, textvariable=txt, font='Helvetica 9')
result.grid(row=4, column=0, columnspan=2, sticky=NW)

frame.pack()

confirm = Button(root, text='Confirm', font='Helvetica 12', command=conf, width=11)
confirm.pack(side=LEFT)

clear = Button(root, text="Clear", font='Helvetica 12', command=clear, width=11)
clear.pack(side=LEFT)

quit = Button(root, text="Quit", font='Helvetica 12', command=root.destroy, width=11)
quit.pack(side=LEFT)

root.mainloop()