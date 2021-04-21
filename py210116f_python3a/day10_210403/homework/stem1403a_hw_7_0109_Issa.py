"""
[Homework]
Date: 2021-03-13
1. Design and write code for a counter
From 1 to infinite without stop
time interval = 1 second
Due date: by the end of next Friday
"""

from tkinter import *

number = 0

while number >= 0:
    number = number + 1
    print(number)


def change_text():
    Label.config(text=str(number))

root = Tk()

root.title("Python GUI - Counter")

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg="#ddddff")

# create a label widget

for number in number:
    Label(root, text=str(number), padx=30, pady=15,
               font="Helvetica 20",
               bg="#72efaa", fg="grey10").pack()

Label.after(1000*number, change_text)


root.mainloop()

