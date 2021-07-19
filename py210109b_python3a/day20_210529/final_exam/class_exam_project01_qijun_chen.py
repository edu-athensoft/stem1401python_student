from tkinter import *


def printInfo():
    print(f"password approved: {password.get()}")

root = Tk()
root.title("Python GUI - Entry")
root.geometry("600x430")

wifi = Label(root,text="Enter the network password",)
wifi.pack()

password_solution = "1"


password = Label(root, text="Password :")
password.pack()

account = Entry(root)
account.pack()


Btn = Button(root, text='Enter', command=printInfo)
Btn.pack()
root.mainloop()
