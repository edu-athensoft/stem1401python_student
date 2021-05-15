"""
Container
Toplevel
"""

from tkinter import *
import random


def MessageBox(num):
    # msgType = random.randint(1, 3)
    msgType = num
    labTxt = msg[msgType]
    topframe = Toplevel()
    topframe.geometry("300x180")
    topframe.title("Message Box")
    Label(topframe, text=labTxt, bg="lightgreen").pack(fill=BOTH, expand=True)


# main program
root = Tk()
root.title("Python GUI - Toplevel")
root.geometry("320x160")
root.config(bg="#ddddff")

msg = {1: "Order", 2: "Payment", 3: "Shipping"}

btn = Button(root, text="Order System", command=lambda : MessageBox(1))
btn.pack()

btn2 = Button(root, text="Payment System", command=lambda : MessageBox(2))
btn2.pack()

root.mainloop()
