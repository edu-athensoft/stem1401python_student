"""
Homework 8
"""

"""
score

required key logic missing (-35)

"""

from tkinter import *
from tkinter.ttk import Separator

def run_counter(digit):
    # define a Local var in the outer function
    counter = 0

    def counting():
        # using nonlocal var here
        nonlocal counter

        counter += 1

        digit.config(text=str(counter))

        if counter >= 10:
            digit.config(text="END")
        else:
            digit.after(1000, counting)

    counting()

# main
root = Tk()

root.title("python GUI - Label counter")
root.geometry("{}x{}+200+240".format(640, 480))
# root.configure(bg='#ddddff')

digit_label1 = Label(root,text="Bien venu a mon GUI",
                # bg= "seagreen", fg = 'white',
                padx='10', pady='20',
                font = "Helvetic 30 bold")
digit_label1.pack()

sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, padx=5, pady=40)

# Label object
digit_label2 = Label(root,
                # bg= "seagreen",
                fg = 'black',
                height = 3, width = 10,
                font = "Helvetic 30 bold")

digit_label2.pack()

sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, padx=5, pady=40)

digit_label3 = Label(root,text="v.0.1",
                bg= "seagreen", fg = 'white',
                font = "Helvetic 30 bold")

digit_label3.pack()

# counting
run_counter(digit_label2)

root.mainloop()

