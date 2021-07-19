"""
Container
Frame
"""

from tkinter import *

root = Tk()
root.title("Python GUI - Frame")
root.geometry("320x240")
root.config(bg="#ddddff")
# print(root.keys())

frameUpper = Frame(root, bg="lightgreen", height=60, width=205, pady=40)
frameUpper.pack(fill=BOTH,pady=20)

btnRed = Button(frameUpper, text="Red", fg="red")
btnRed.grid(row=0, column=0)

btnGreen = Button(frameUpper, text="Green", fg="green")
btnGreen.grid(row=1, column=1)

frameLower = Frame(root, bg="lightblue", height=30, width=150)
frameLower.pack(fill=BOTH, expand=True)

# btnPurple = Button(frameLower, text="Purple", fg="purple").pack(side=TOP)
root.mainloop()
