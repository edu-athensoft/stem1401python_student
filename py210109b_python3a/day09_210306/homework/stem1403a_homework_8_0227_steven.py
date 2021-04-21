"""

"""

"""
score

required key logic missing (-35)
no docstring (-5)

"""

from tkinter import *
from tkinter.ttk import Separator
from datetime import datetime

now = datetime.now()

time = now.strftime("%H:%M:%S:%A")



def counting(digit):
    counter = 0
    def count():
        nonlocal counter
        counter += 1
        digit.config(text=str(counter))

        if counter >= 10:
            digit.config(text="END")
            root.update()
            return
        else:
            digit.after(1000, count)
    count()

root = Tk()
root.title("Python")
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg="#ddfffd")
text1 = "Clock Python Program"
label2 = Label(root, text=text1, pady=20, font="Helvetic 20 bold", justify ="center", bg="yellow")
label2.pack()

sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, padx=5, pady=40)

label1 = Label(root,text=time, bg="red", fg="cyan", height=1, width=3, font="Helvetic 20 italic", justify="center", padx="120", pady="50")
label1.pack()

sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, padx=5, pady=40)

text2 = "Version 2, Steven, 2021-02-27"
label3 = Label(root, text=text2, pady=10, font="Helvetic 10", justify ="center", bg="yellow")
label3.pack()

# counting(label1)

root.mainloop()