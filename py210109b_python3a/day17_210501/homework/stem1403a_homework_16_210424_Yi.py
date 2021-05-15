"""
Homework 16

Date: 2021-04-24
Write a GUI program in Python for a basic calculator
Description
Create a window
Create 10 Button objects for digit 0 - 9
Create 7 Button objects for operators (+, -, *, /, %, ., =)
where % stands for modulus operator rather than percentage sign
where = stands for performing calculation
Create a 'Clear all' Button with the caption of C
Create a 'Backspace' Button with the caption of DEL
Create a display Label to show expression (or equation) at the first line and to show result at the second line.
Due date: by the end of next Friday
"""

from tkinter import *

expression = ""

def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)

def equalpress():
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""

def clearInfo():
    global expression
    expression = ""
    equation.set("")

root = Tk()
root.title("Python GUI - calculator")
# root.geometry("380x190")
equation = StringVar()

entry1 = Entry(root, textvariable=equation)
entry1.grid(columnspan=4, ipadx=125)

btn_1 = Button(root, text='C', font=(None, 15), padx=35, command=clearInfo).grid(row=2, column=0)

btn_2 = Button(root, text='DEL', font=(None, 15), padx=30,).grid(row=2, column=1)

btn_3 = Button(root, text='%', font=(None, 15), padx=35).grid(row=2, column=2)

btn_4 = Button(root, text='/', font=(None, 15), command=lambda: press('/'), padx=35).grid(row=2, column=3)


btn_2_1 = Button(root, text='7', font=(None, 15), command=lambda: press(7), padx=35).grid(row=3, column=0)

btn_2_2 = Button(root, text='8', font=(None, 15), command=lambda: press(8), padx=40).grid(row=3, column=1)

btn_2_3 = Button(root, text='9', font=(None, 15), command=lambda: press(9), padx=35).grid(row=3, column=2)

btn_2_4 = Button(root, text='*', font=(None, 15), command=lambda: press('*'), padx=35).grid(row=3, column=3)


btn_3_1 = Button(root, text='4', font=(None, 15), command=lambda: press(4), padx=35).grid(row=4, column=0)

btn_3_2 = Button(root, text='5', font=(None, 15), command=lambda: press(5), padx=40).grid(row=4, column=1)

btn_3_3 = Button(root, text='6', font=(None, 15), command=lambda: press(6), padx=35).grid(row=4, column=2)

btn_3_4 = Button(root, text='-', font=(None, 15), command=lambda: press('-'), padx=35).grid(row=4, column=3)


btn_4_1 = Button(root, text='1', font=(None, 15), command=lambda: press(1), padx=35).grid(row=5, column=0)

btn_4_2 = Button(root, text='2', font=(None, 15), command=lambda: press(2), padx=40).grid(row=5, column=1)

btn_4_3 = Button(root, text='3', font=(None, 15), command=lambda: press(3), padx=35).grid(row=5, column=2)

btn_4_4 = Button(root, text='+', font=(None, 15), command=lambda: press('+'), padx=35).grid(row=5, column=3)



btn_5_2 = Button(root, text='0', font=(None, 15), command=lambda: press(0), padx=87).grid(row=6, column=0, columnspan=2)

btn_5_3 = Button(root, text='.', font=(None, 15), command=lambda: press('.'), padx=35).grid(row=6, column=2)

btn_5_4 = Button(root, text='=', font=(None, 15), command=equalpress, padx=35).grid(row=6, column=3)

root.mainloop()