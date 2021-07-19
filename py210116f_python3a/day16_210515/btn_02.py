"""
Button

create a Button
and write response code
"""

from tkinter import *

def response():
    print("I was clicked.")


win = Tk()
win.title("Tkinter Button")
win.geometry("480x320+300+300")
win.config(bg="#ddddff")

# Button
# command option accepts function only (function name or anonymous function/lambda)
btn1 = Button(win, text="Click me!", font=(None, 20), command=response)
btn1.pack()

# Button
btn2 = Button(win, text="Close", font=(None, 20), command=win.destroy)
btn2.pack()

win.mainloop()