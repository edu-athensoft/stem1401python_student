"""
Python 3 Final Exam
Part 2
Ze Yue Li
2020-05-30
"""

from tkinter import *
import random
from tkinter import messagebox as msg


def verify():

    randomNumber = random.randint(10000, 99999)

    verifyWindow = Tk()
    verifyWindow.title("Verification")

    numberLabel = Label(verifyWindow, text=randomNumber)
    numberLabel.pack()

    numberE = Entry(verifyWindow)
    numberE.pack()

    confirm = Button(verifyWindow, text="Confirm", command=lambda: confirmVerification(verifyWindow, numberE.get(), randomNumber))
    confirm.pack()


def confirmVerification(window, num, randomNum):
    if int(num) == randomNum:
        global verified
        verified = True
        window.destroy()
    else:
        msg.showerror("Error", "Number does not match")


def register():
    if verified == True:
        if passwordE.get() == passwordConfirmationE.get():
            msg.showinfo("Success", "Registration Success!")
        else:
            msg.showerror("Error", "Passwords do not match!")
    else:
        msg.showerror("Error", "Please verify you are human")


def reset():
    global verified
    usernameE.delete(0, END)
    passwordE.delete(0, END)
    passwordConfirmationE.delete(0, END)
    verified = False



root = Tk()
root.title("Registration")

verified = False

label = Label(root, text="File Transfer\nAccount registration", font=("Roman", 40))
label.grid(row=0, columnspan=3)

usernameL = Label(root, text="Username:")
usernameL.grid(row=1, columnspan=2)

usernameE = Entry(root)
usernameE.grid(row=1, column=2)

passwordL = Label(root, text="Password:")
passwordL.grid(row=2, columnspan=2)

passwordE = Entry(root, show="*")
passwordE.grid(row=2, column=2)

passwordConfirmationL = Label(root, text="Please confirm your password:")
passwordConfirmationL.grid(row=3, columnspan=2)

passwordConfirmationE = Entry(root, show="*")
passwordConfirmationE.grid(row=3, column=2)

verificationLabel = Label(root, text="Please verify you are a human:")
verificationLabel.grid(row=4, columnspan=2)

verificationButton = Button(root, text="Verify", command=verify)
verificationButton.grid(row=4, column=2)

confirmationButton = Button(root, text="Register", command=register)
confirmationButton.grid(row=6, column=0)

resetButton = Button(root, text="Clear all", command=reset)
resetButton.grid(row=6, column=1)

exitButton = Button(root, text="Exit", command=root.destroy)
exitButton.grid(row=6, column=2)

root.mainloop()
