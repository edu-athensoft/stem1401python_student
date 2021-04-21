"""
Homework 7
"""

"""
score
perfect

"""

from tkinter import *

root = Tk()


def run_counter(digit):
    counter = 0

    print("Counter")

    def counting():
        nonlocal counter
        counter += 1
        print(counter)
        digit.config(text=counter)

        if counter >= 10:
            digit.config(text="END")
            return
        else:
            digit.after(1000, counting)

    counting()

# Geometry
root.title('Python GUI - Counter')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# Label
digit_label = Label(root,
                    bg='seagreen',
                    fg='white',
                    height=3,
                    width=10,
                    font="Helvetic 30 bold")
digit_label.pack()

# Counter
run_counter(digit_label)


root.mainloop()
