"""
Homework 11
Date: 2021-03-27
Input N numbers from your keyboard
Put them into a list  (i.e. [1,3,5])
Create a window
Then place(add) N buttons to the window
anchor=S
side=LEFT, side=RIGHT
Button text is the current number you get
Create an 'Exit' button
which allows you to press it to close the window
Hint:
Lambda
pass parameter
only one callback function
Due date: by the end of next Friday
"""

from tkinter import *

numbers = [25, 30, 98, 3150, 93, 260, 205, 57, 10]


def response():
    label1 = Label(root, text='I was clicked')
    label1.pack()


root = Tk()
root.title('Python GUI - Button')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')

for i in range(len(numbers)):
    btn = Button(root, text=numbers[i], font='Helvetica 10', command=lambda: response())
    btn.pack(anchor=S, side=LEFT, ipadx=5, ipady=5)

exit_btn = Button(root, text="Exit", font='Helvetica 10', command=lambda: root.destroy())
exit_btn.pack(anchor=N, side=RIGHT, ipadx=5, ipady=5)

root.mainloop()
