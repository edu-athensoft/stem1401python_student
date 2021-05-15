from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("800x500+200+200")
root.config(bg="gray85")
root.resizable(1, 1)
font = ("Helvetica", 16)
expression: str = ""
expression_answer = ""
display_Label = Label(text=expression, width=63, height=3, bg="gray85", relief="raised", padx=5, anchor=E, font=font)
display_Label.grid(columnspan=4, padx=10, pady=10, sticky=E)


def user_input_digit(num):
    global expression
    num = num - 1
    expression = expression + f"{num}"
    display_Label.config(text=expression)


def clear():
    global expression
    expression = ""
    display_Label.config(text="")


def delete():
    global expression
    expression = expression[:-1]
    display_Label.config(text=expression)


def modulus():
    global expression
    if expression[-1:].isnumeric and expression != "":
        expression = expression + "%"
    display_Label.config(text=expression)


def division():
    global expression
    if expression[-1:].isnumeric and expression != "":
        expression = expression + "/"
    display_Label.config(text=expression)


def multiplication():
    global expression
    if expression[-1:].isnumeric and expression != "":
        expression = expression + "*"
    display_Label.config(text=expression)


def subtraction():
    global expression
    if expression[-1:].isnumeric:
        expression = expression + "-"
    display_Label.config(text=expression)


def addition():
    global expression
    if expression[-1:].isnumeric and expression != "":
        expression = expression + "+"
    display_Label.config(text=expression)


def comma():
    global expression
    if expression[-1:].isnumeric() and expression != "":
        expression = expression + "."
    display_Label.config(text=expression)


def equal():
    global expression, expression_answer
    answer = eval(expression)
    expression_answer = expression + "\n" + str(answer)
    display_Label.config(text=expression_answer)


row = 2
digits = ['7', '4', '1', '8', '5', '2', '9', '6', '3', '0']

clear_button = Button(root, text='C', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12', fg='blue',
                      command=clear)
clear_button.grid(row=1)

delete_B = Button(text="DEL", font=font, width=15, height=2, command=delete)
delete_B.grid(row=1, column=1)

modulus_button = Button(root, text='%', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12',
                        command=modulus)
modulus_button.grid(row=1, column=2)

division_button = Button(root, text='/', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12',
                         command=division)
division_button.grid(row=1, column=3)

multiplication_button = Button(root, text='*', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12',
                               command=multiplication)
multiplication_button.grid(row=2, column=3)
subtraction_button = Button(root, text='-', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12',
                            command=subtraction)
subtraction_button.grid(row=3, column=3)
addition_button = Button(root, text='+', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12',
                         command=addition)
addition_button.grid(row=4, column=3)
answer_button = Button(root, text='=', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12',
                       bg='light goldenrod yellow', command=equal)
answer_button.grid(row=5, column=3)

expression = ""
answer = ""

button_list = []
for i in range(10):
    button = Button(text=i, command=lambda num=i + 1: user_input_digit(num), width=15, height=2, font=font)
    button_list.append(button)

button_list[7].grid(row=2, column=0, pady=5, padx=5)
button_list[8].grid(row=2, column=1, pady=5, padx=5)
button_list[9].grid(row=2, column=2, pady=5, padx=5)
button_list[4].grid(row=3, column=0, pady=5, padx=5)
button_list[5].grid(row=3, column=1, pady=5, padx=5)
button_list[6].grid(row=3, column=2, pady=5, padx=5)
button_list[1].grid(row=4, column=0, pady=5, padx=5)
button_list[2].grid(row=4, column=1, pady=5, padx=5)
button_list[3].grid(row=4, column=2, pady=5, padx=5)
button_list[0].config(width=30)
button_list[0].grid(row=5, columnspan=3, pady=5, padx=(5, 0))

root.mainloop()
