"""
Button
state

normal
active
disabled
"""

from tkinter import *

def helloCallBack():
    pass

# main program
root = Tk()
root.title('Python GUI - Button and Lambda')
root.geometry('300x200+300+200')

# button state
btn1 = Button(root, text='Normal', command=lambda: helloCallBack(), state='normal')
btn1.pack()

btn2 = Button(root, text='Active', command=lambda: helloCallBack(), state='active')
btn2.pack()

btn3 = Button(root, text='Disabled', command=lambda: helloCallBack(), state='disabled')
btn3.pack()


root.mainloop()
