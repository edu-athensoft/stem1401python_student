"""
Button

create a Button
create a Button to close the entire window
"""

from tkinter import *

root = Tk()
root.title("Tkinter Button")
root.geometry("480x320+300+300")
root.config(bg="#ddddff")

# Button
btn1 = Button(root, text="Click me!", font=(None, 20))
btn1.pack()

# Button
btn2 = Button(root, text="Close", font=(None, 20), command=root.destroy)
btn2.pack()

root.mainloop()
