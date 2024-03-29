"""
[Homework]
Date: 2021-03-21
Create a window with two buttons
Click one for showing a text content using a label
Click the other one to exit
Due date: by the end of next Friday
"""

# tkinter module
from tkinter import *


def show_msg():
    # mymsg = msg
    text_box.configure(text=msg)
    # text_box.config(text=msg)


# exit program function
def close_widget():
    # do other jobs
    root.destroy()


# widget specifications
root = Tk()
root.title("Kevin L. Homework")

# show content function
msg = "You have pressed the left button"

# label without text
text_box = Label(bg="gray87", width=len(msg) + 5, height=5, relief="groove")
text_box.grid(row=0, columnspan=2, padx=60, pady=15)

# button for showing msg
Button(text="Open Message", command=show_msg, relief="groove", width=15, height=3).grid(row=1, column=0, pady=20)

# button for destroying widget
Button(text="Close program", command=close_widget, relief="groove",  width=15, height=3).grid(row=1, column=1, pady=20)

# mainloop
root.mainloop()
