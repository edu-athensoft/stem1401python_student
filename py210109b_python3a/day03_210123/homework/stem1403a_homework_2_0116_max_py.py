"""
Homework 2
"""

"""
score
perfect

"""

import tkinter as tk

screen_length = 1920
screen_width = 1080
window_length = 800
window_width = 450

root = tk.Tk()

root.title('Python GUI - Center')
### root.iconbitmap('img/IMG_2408.ico')


def center():
    x = screen_length/2
    y = screen_width/2

    half_length = window_length/2
    half_width = window_width/2

    root.geometry(f"{window_length}x{window_width}"
                  f"+{int(x-half_length)}+{int(y-half_width)}")


center()

root.mainloop()
