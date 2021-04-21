"""
Button
command
lambda function
pass parameter
"""


from tkinter import *


def helloCallBack():
    label1 = Label(root, text="This is a label widget.")
    label1.pack()
    # print('I was clicked.')


# main program
root = Tk()
root.title('Python GUI - Button and Lambda')
root.geometry('300x200+300+200')

# create a button object using lambda
btn1 = Button(root, text="Confirm using lambda", command=lambda:helloCallBack())
btn1.pack()

# create a button object
btn2 = Button(root, text='OK', command=helloCallBack)
btn2.pack()

root.mainloop()
