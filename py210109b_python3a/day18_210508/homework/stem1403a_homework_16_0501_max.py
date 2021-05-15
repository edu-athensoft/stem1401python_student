"""
Homework 16

Create a window
Create 10 Button objects for digit 0 - 9
Create 7 Button objects for operators (+, -, *, /, %, ., =)
where % stands for modulus operator rather than percentage sign
where = stands for performing calculation
Create a 'Clear all' Button with the caption of C
Create a 'Backspace' Button with the caption of DEL
Create a display Label to show expression (or equation) at the first line and to show result at the second line.
"""

from tkinter import *
from math import *
from tkinter import messagebox as msg

# 1. never wrap everything with a try block
# 2. do not define functions within try block


try:
    def calculation():
        global calculate, answer

        try:
            answer.set(eval(display_number.get()))
        except SyntaxError:
            display_number.set("A syntax error has occurred")
        finally:
            calculate = True


    def set_value(value):
        global calculate

        if calculate:
            if value in operators + ['%', '.']:
                display_number.set(answer.get())
                answer.set('')
            else:
                display_number.set('')
                answer.set('')
            calculate = False

        display_number.set(display_number.get() + value)


    def backspace():
        x = list(display_number.get())

        if not calculate:
            try:
                del x[-1]
            except IndexError:
                pass
            display_number.set(''.join(x))


    root = Tk()
    root.title("Python GUI - Entry")
    root.geometry("265x173")

    calculate = False

    display_number = StringVar()
    answer = StringVar()

    # numbers
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(numbers)):
        Button(root, text=str(numbers[i]), width=8, height=1, command=lambda val=numbers[i]: set_value(val)).grid(
            row=ceil(5 - (i / 3)),
            column=i % 3)

    zero = Button(root, text='0', width=17, height=1, command=lambda val='0': set_value(val)).grid(row=6, column=0,
                                                                                                   columnspan=2,
                                                                                                   ipadx=1)
    # operators
    operators = ['/', '*', '-', '+']
    for i in range(len(operators)):
        Button(root, text=str(operators[i]), width=8, height=1, command=lambda val=operators[i]: set_value(val)).grid(
            row=i + 2,
            column=4)

    modulo = Button(root, text='%', width=8, height=1, command=lambda val='%': set_value(val)).grid(row=2, column=2)
    decimal = Button(root, text='.', width=8, height=1, command=lambda val='.': set_value(val)).grid(row=6, column=2)
    equal = Button(root, text='=', width=8, height=1, bg='#ffffdd', command=lambda: calculation()).grid(row=6, column=4)

    # extra
    back = Button(root, text='DEL', width=8, height=1, command=lambda: backspace()).grid(row=2, column=1)
    clear = Button(root, text='C', width=8, height=1, command=lambda: display_number.set('')).grid(row=2, column=0)
    display = Label(root, width=37, height=1, textvariable=display_number, anchor='ne').grid(row=0, column=0,
                                                                                             columnspan=5, rowspan=1)
    ans = Label(root, width=37, height=1, textvariable=answer, anchor='se').grid(row=1, column=0,
                                                                                 columnspan=5, rowspan=1)

    root.mainloop()

except Exception:
    msg.showerror("Error", "An unexpected error has occurred")
