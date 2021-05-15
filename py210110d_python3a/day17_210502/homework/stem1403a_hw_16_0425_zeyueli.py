"""
[Homework]
Date: 2021-04-25
Study others' code
write a summary.  """    """  .py
Zeyue code (logic)
2. Rewrite the last 3 sample code for textvariable
get()
set()
callback function
4:18
Optimize your code,  submit
"""

from tkinter import *


# functions
def execute_button(button):
    global expression
    if button != "C" and button != "DEL":
        expression += button
    elif button == "C":
        expression = ""
    else:
        expression = expression[:-1]
    display_label["text"] = f"{expression}"


def calculate():
    global result
    global expression
    try:
        result = eval(expression)
        expression += "="
        display_label["text"] = f"{expression}\n{result}"
        expression = str(result)
    except Exception as e:
        result = "An error has occurred during the calculation"
        display_label["text"] = f"{result}"
    result = ""


# main program
root = Tk()
root.title("Python GUI - Project - Calculator")

expression = ""
result = ""

# main label
display_label = Label(root, text=f"{expression}", relief="raised", width=100, height=2, anchor=E)
display_label.grid(row=0, columnspan=4, sticky=S)

# row and column
MAXROW = 5

row = 1
column = 0

# button creation
buttons = ["C", "7", "4", "1", "DEL", "8", "5", "2", "%", "9", "6", "3", "/", "*", "-", "+"]

for button in buttons:
    button1 = Button(root, text=button, font=(None, 10), relief="raised", command=lambda a=button: execute_button(a))
    if button == "C":
        button1["fg"] = "blue"
    button1.grid(row=row, column=column, sticky=E + W)
    row += 1

    if row >= MAXROW:
        column += 1
        row = 1

# bottom row buttons
zero_button = Button(root, text="0", font=(None, 10), relief="raised", command=lambda: execute_button("0"))
zero_button.grid(row=6, columnspan=2, sticky=E+W)

dot_button = Button(root, text=".", font=(None, 10), relief="raised", command=lambda: execute_button("."))
dot_button.grid(row=6, column=2, sticky=E+W)

enter_button = Button(root, text="=", bg="yellow", font=(None, 10), relief="raised", command=calculate)
enter_button.grid(row=6, column=3, sticky=E+W)

root.mainloop()
