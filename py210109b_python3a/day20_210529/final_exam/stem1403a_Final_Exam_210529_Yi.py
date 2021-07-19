"""
Homework]
Date: 2021-05-08
Rewrite checkbutton program
Print out all options you checked
"""

from tkinter import *
from tkinter import messagebox as msg
import random

def myste_validation():
    s = str(random.randrange(1,10))
    s1 = str(random.randrange(1,10))
    s2 = str(random.randrange(1,10))
    s3 = str(random.randrange(1,10))
    s4 = str(random.randrange(1,10))
    s5 = str(random.randrange(1, 10))
    p = s + s1 + s2 + s3 + s4 + s5
    return p

def registration(valicode, passw, rpassw):
    if valicode == validation_code:
        print(f"Username: {entry1.get()}")
        if passw == rpassw:
            print(f"Password: {entry2.get()}")
            print(f"Review password: {entry3.get()}")
            print(f"Validation password: {entry4.get()}")
            msg.showinfo("Login", "Login successful!")
        else:
            print(f"Password: {entry2.get()}")
            print("Review password is not correct")
            print(f"Validation password: {entry4.get()}")
            msg.showerror("Login", "Wrong Review password. Please try again.")
    else:
        print(f"Username: {entry1.get()}")
        print(f"Password: {entry2.get()}")
        print(f"Review password: {entry3.get()}")
        print(f"not correct")
        msg.showerror("Login", "Wrong Validation code. Please try again.")


def clearInfo():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)

root = Tk()
root.title("Python GUI - Entry")
root.geometry("640x480")

validation_code = myste_validation()

digit_label1 = Label(root,text="The registration form",
                padx='10', pady='20',
                font = "Helvetic 20 bold")
digit_label1.grid(row=1, column=1, columnspan=8, padx=(180,5))

accountL = Label(root, text="Username :")
accountL.grid(row=3, column=1, padx=(20,5), sticky='e')

entry1 = Entry(root)
entry1.grid(row=3, column=2, padx=(5, 50), columnspan=4)

accountL1 = Label(root, text="Password :")
accountL1.grid(row=4, column=1,padx=(20,5), sticky='e')

entry2 = Entry(root)
entry2.grid(row=4, column=2, padx=(5, 50),columnspan=4)

accountL2 = Label(root, text="Review Password :")
accountL2.grid(row=5, column=1,padx=(150,5), sticky='e')

entry3 = Entry(root)
entry3.grid(row=5, column=2, padx=(5, 50),columnspan=4)

accountL3 = Label(root, text="validation code :")
accountL3.grid(row=6, column=1,padx=(0,5), sticky='e')

entry4 = Entry(root)
entry4.grid(row=6, column=2, padx=(5, 50),columnspan=4)

label1 = Label(root,text="Code = {}".format(validation_code),fg = 'black', font = "30")
label1.grid(row=6, column=3,columnspan=3)

register = Button(root, text="Print", command=lambda: registration(entry4.get(), entry3.get(), entry2.get()))
register.grid(row=7, column= 2, sticky="we")

clearbtn = Button(root, text="Clear", command=clearInfo)
clearbtn.grid(row=7, column= 3, sticky="we")

quitbtn = Button(root, text="Quit", command=root.destroy)
quitbtn.grid(row=7, column= 4, sticky="we")

root.mainloop()