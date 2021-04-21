"""
Homework 4
"""

"""
score
perfect

"""

import tkinter as tk

root = tk.Tk()

root.title('Python GUI - Homework 4')
root.iconbitmap('img/IMG_2408.ico')


def center(screen_length, screen_width, window_length, window_width):
    x = screen_length/2
    y = screen_width/2

    half_length = window_length/2
    half_width = window_width/2

    root.geometry(f"{window_length}x{window_width}"
                  f"+{int(x-half_length)}+{int(y-half_width)}")


center(1920, 1080, 800, 450)
root.maxsize(1000, 1000)
root.minsize(100, 100)
root.configure(bg='#aabbcc')

label1 = tk.Label(root, text='bla bla bla',
                  font='Helvetica',
                  width=10, height=5,
                  bg='red',
                  fg='blue',
                  anchor='n',
                  wraplength=40)

label1.pack()

root.mainloop()
