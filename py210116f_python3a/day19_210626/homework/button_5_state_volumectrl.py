"""
Button

Volume controller

Set state for a button
state = {active, disabled, normal}
"""

from tkinter import *


def plus(step=1):
    global value
    value += step
    if value >= MAX:
        button_plus.config(state="disabled")
        button_minus.config(state="active")
    else:
        button_plus.config(state="active")
        button_minus.config(state="active")
    label_value.config(text=str(value))


def minus(step=1):
    global value
    value -= step
    if value <= MIN:
        button_plus.config(state="active")
        button_minus.config(state="disabled")
    else:
        button_plus.config(state="active")
        button_minus.config(state="active")
    label_value.config(text=str(value))


root = Tk()
root.geometry("270x280+600+300")
root.config(bg="goldenrod")
root.title("Python GUI - Volume Control")

# settings
value = 0
MAX = 10
MIN = -10

label_value = Label(root, text=str(value), pady=60, font=("Arial", 50, "bold"), fg="snow", bg="dodgerblue")
label_value.pack(fill=X)

button_plus = Button(root, text="+", state="active", padx=15, font=("Arial", 20), command=lambda: plus(1))
button_plus.pack(anchor=S, side=LEFT, padx=5, pady=5)

button_minus = Button(root, text="-", state="active", padx=15, font=("Arial", 20), command=lambda: minus(1))
button_minus.pack(anchor=S, side=LEFT, padx=5, pady=5)

button_exit = Button(root, text="EXIT", padx=15, font=("Arial", 20), command=root.destroy)
button_exit.pack(anchor=S, side=LEFT, padx=5, pady=5)

root.mainloop()
