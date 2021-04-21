"""
Homework 3
"""

"""
score
perfect

"""

import tkinter as tk

root = tk.Tk()

root.title('Python GUI - Center')


def center(screen_length, screen_width, window_length, window_width, color):
    if screen_length / screen_width == 16 / 9:

        x = screen_length / 2
        y = screen_width / 2

        half_length = window_length / 2
        half_width = window_width / 2

        root.geometry(f"{window_length}x{window_width}"
                      f"+{int(x - half_length)}+{int(y - half_width)}")

        root.configure(bg=color)

        root.attributes('-topmost', True)

        root.resizable(False, False)

        print(f"window length: {window_length}, window width: {window_width}")

    else:
        raise ValueError("Please specify an aspect ratio of 16:9")


center(1920, 1080, 800, 450, "#cffcff")

root.mainloop()
