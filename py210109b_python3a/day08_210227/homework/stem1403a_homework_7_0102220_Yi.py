"""
Tjinter
Label counter

config()
after()

"""

"""
score
typo in docstring (-1)

"""

from tkinter import *

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
root.configure(bg='#ddddff')

# Label object
digit_label = Label(root,
                bg= "seagreen", fg = 'white',
                height = 3, width = 10,
                font = "Helvetic 30 bold")

digit_label.pack(side = "right")

# counting
run_counter(digit_label)

root.mainloop()

