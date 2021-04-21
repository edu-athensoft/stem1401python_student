"""
Homework 8
"""

"""
score
improper function name (-5)
failed to apply Separator Widget (-5)

"""

from tkinter import *
from datetime import *

root = Tk()


### improper function name
def date(digit):

    def counting():
        curr_time = datetime.now()
        formatted_time = curr_time.strftime('%H:%M:%S.%f')
        # modified by Athens
        formatted_time = formatted_time[:-3]
        digit.config(text=f"{formatted_time}")
        digit.after(1, counting)

    counting()


# Geometry
root.title('Python GUI - Counter')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='white')

# Label
title = Label(root,
              bg='white',
              font="Helvetic 30 bold",
              text="System Time")

footer = Label(root,
               bg='white',
               font="Helvetic 24 bold",
               text="Version 1, Max Yang, March 6th 2021")

separator = Label(root,
                  bg='white',
                  text="─────────────────────",
                  font="Helvetic 30 bold")

separator2 = Label(root,
                   bg='white',
                   text="─────────────────────",
                   font="Helvetic 30 bold")

digit_label = Label(root,
                    bg='seagreen',
                    fg='white',
                    padx=100,
                    pady=100,
                    font="Helvetic 30 bold")
title.pack()
separator.pack()
digit_label.pack()
separator2.pack()
footer.pack()

# Counter
date(digit_label)

root.mainloop()
