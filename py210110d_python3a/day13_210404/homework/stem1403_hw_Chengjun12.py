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
white_check_mark
eyes
raised_hands
"""
from tkinter import *

def print_number(number):
    print(numbers[number])

root = Tk()
root.title("HW_CHENGJUN")
root.geometry("800x450+200+200")
root.config(bg="#ddddff")

numbers = []

num = int(input("enter a number, a button with the number will be created : "))

numbers.append(num)

Button(text="Exit", command=root.destroy).pack(pady=20, padx=15, anchor=S, side=RIGHT)
for i in range(len(numbers)):
    Button(text=numbers[i], command=lambda num=i: print_number(num)).pack(pady=20, padx=15, anchor=S, side=RIGHT)

root.mainloop()