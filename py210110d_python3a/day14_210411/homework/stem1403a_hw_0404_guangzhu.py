"""
[Challenge]  Project. Volume Controller
c04_button/button_03_b.py
Description
Max value and Min value
1. User can press '+' button to increase the number by one per click
2. User can press '-' button to decrease the number by one per click
3. The number shows in a Label
constraints:
the MAX value = 10,
the MIN value = -10,
default number = 0
default step number = 1,  step number is adjustable
"""

from tkinter import *

max = 10
min = -10
step_number = int(input('Please enter the step number you want(an integer):'))
print('The max number on the label is 10 and the minimum is -10')


def add():
    global digit
    digit += step_number
    if digit == max or digit >= max:
        add_button.config(state='disabled')
        decrease_button.config(state='normal')
        digit = max
    elif max > digit >= min:
        add_button.config(state='normal')
        decrease_button.config(state='normal')
    else:
        add_button.config(state='normal')
    digit_label.config(text=digit)


def decrease():
    global digit
    digit -= step_number
    if digit == min or digit <= min:
        decrease_button.config(state='disabled')
        add_button.config(state='normal')
        digit = min
    elif min < digit <= max:
        decrease_button.config(state='normal')
        add_button.config(state='normal')
    else:
        decrease_button.config(state='normal')
    digit_label.config(text=digit)


root = Tk()
root.title('button homework')
root.config(bg='#ddddff')

digit = 0

digit_label = Label(text=digit, font="Helvetica 25", width=21, height=5, bg="gray85")
digit_label.pack(fill=X)

exit_button = Button(width=14, height=2, font='Helvatica 15 bold', text="Exit", relief="raised", bg='red', command=root.destroy)
exit_button.pack(side=RIGHT)

add_button = Button(width=10, height=2, font='Helvatica 15 bold', text="+", relief="raised", command=add)
add_button.pack(side=LEFT)

decrease_button = Button(width=10, height=2, font='Helvatica 15 bold', text="-", relief="raised", command=decrease)
decrease_button.pack()


root.mainloop()
