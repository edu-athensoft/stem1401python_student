"""
real button
action:
    press
    release
    bump

click
    quick click
    long click
    (single) click
    double click

event
    click action generates an event (object)
    listening the event source
    response


hyper-link
    link and bring you to a new web address
    can refer to a resource on line (pdf, xml, txt, jpg, ...)
    click and get the benefit of a service or function provided by other on-line presence

click

"""

from tkinter import *

root = Tk()
root.title('Python GUI - Button')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')

btn1 = Button(root, text='Click me')
btn1.pack()


root.mainloop()