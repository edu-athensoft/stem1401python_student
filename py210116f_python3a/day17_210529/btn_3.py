"""
Button - lambda
"""

from tkinter import *


def myclick():
    print('I was clicked.')


def myclicklambda(num):
    print(f'I was clicked at #{num}')



root = Tk()
root.title('Python GUI - Button')
root.geometry('640x480+300+300')

# Button
btn1 = Button(root, text='1. Click me', command=myclick, font=(None, 16))
btn1.pack()

# Button 2
btn2 = Button(root, text='2. Click me - Lambda', command=lambda : myclicklambda(2), font=(None, 16))
btn2.pack()


# Button 3
btn3 = Button(root, text='3. Click me - Lambda', command=lambda : myclicklambda(3), font=(None, 16))
btn3.pack()

root.mainloop()