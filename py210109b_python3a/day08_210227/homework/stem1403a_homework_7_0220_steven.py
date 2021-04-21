"""

"""

"""
score
missing docstring (-5)

"""

from tkinter import *

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
root.geometry("{}x{}+200+240".format(640, 800))
root.configure(bg="#ddfffd")

label1 = Label(root, bg="red", fg="green", height=1, width=3, font="Helvetic 40 italic")
label1.pack()

counting(label1)

root.mainloop()