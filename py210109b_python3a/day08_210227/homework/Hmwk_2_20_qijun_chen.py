
'''
1. Write a GUI program of Label counter for implementing version 3.
Requirements:
(Function)
When the number reaches 10, then it comes to stop and displays the text of 'END'.
If a user clicks to close the main window, the program terminates.
(UI)
Using the layout manager of pack() for the UI.
A recommended UI design is given below.
Due date: by the end of next Friday
'''

from tkinter import *

def counting(digit):
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

root = Tk()
root.title("Python")
root.geometry("{}x{}+200+240".format(640, 800))
root.configure(bg="#ddfffd")

label1 = Label(root, bg="red", fg="green", height=1, width=3, font="Helvetic 40 italic")
label1.pack()

counting(label1)

root.mainloop()