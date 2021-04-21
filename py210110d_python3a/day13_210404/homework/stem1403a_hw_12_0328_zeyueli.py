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


def print_num(number):
    print(f"Button {number} was pressed")


number_list = []

num_of_nums = input("Please enter the number of buttons you want or the numbers on the buttons separated by a space: ")
if " " in num_of_nums:
    number_list = num_of_nums.split(" ")
else:
    for i in range(int(num_of_nums)):
        number_list.append(input("Enter the next number: "))

MAX_ROWS = 17  # MUST BE ADJUSTED TO FIT SCREEN SIZE

r = 0
c = 0

root = Tk()
root.title('Python GUI - Homework')
root.geometry('640x480')
root.config(bg='#ddddff')

for i in number_list:
    btn = Button(root, text=i, anchor=S, command=lambda num=i: print_num(num))
    btn.grid(row=r, column=c, sticky=E + W)

    r += 1
    if r > MAX_ROWS:
        r = 0
        c += 1

close = Button(root, text='Exit', command=root.destroy)
close.grid(row=r, column=c, sticky=E + W)

root.mainloop()
