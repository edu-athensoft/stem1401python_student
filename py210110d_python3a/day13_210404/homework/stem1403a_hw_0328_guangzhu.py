"""
[Homework]
Date: 2021-03-28
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
Due date: by the end of next Sat.
"""
from tkinter import *

root = Tk()
root.title('button homework')
root.geometry('640x480+200+200')
root.config(bg='#ddddff')

input_button = input("Please enter the numbers (separated with a space):")
list_button = []

# r is ?
r = 0
list_button.append(input_button.split(' '))
for index in list_button[0]:
    btn_number = Button(root, text=index, relief='groove', width=20, height=2, anchor=S)
    btn_number.grid(row=r)
    r += 1

# exit button
exit_button = Button(root,text='exit', command=root.destroy, width=20, height=2)
exit_button.grid(column=3, row=2)

root.mainloop()
