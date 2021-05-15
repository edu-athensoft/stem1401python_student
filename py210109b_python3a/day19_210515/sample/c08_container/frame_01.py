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
frameUpper.pack(fill=BOTH)

btnRed = Button(frameUpper, text="Red", fg="red").pack(side=LEFT)
btnGreen = Button(frameUpper, text="Green", fg="green").pack(side=LEFT)

frameLower = Frame(root, bg="lightblue", height=30, width=150)
frameLower.pack(fill=BOTH, expand=True)

# btnPurple = Button(frameLower, text="Purple", fg="purple").pack(side=TOP)
root.mainloop()
