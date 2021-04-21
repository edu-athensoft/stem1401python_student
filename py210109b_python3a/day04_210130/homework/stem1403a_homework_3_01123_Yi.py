"""
Homework
"""

import tkinter as tk
import time

root = tk.Tk()
root.title("Python GUI - Center")
# root.iconbitmap("IMG_2408.ico")

win_width = 640
win_height = 480

positionRight = int(root.winfo_screenwidth() / 2 - win_width/2 )
positionDown = int(root.winfo_screenheight() / 2 - win_height/2 )

root.maxsize(900, 600)
root.minsize(100, 70)

root.geometry(f"{win_width}x{win_height}+{positionRight}+{positionDown}")
root.update()
time.sleep(1.5)

root.update()
root.configure(bg='#ddddff')
time.sleep(1.5)

root.update()
root.configure(bg='#ddffdd')
time.sleep(1.5)

root.update()
root.configure(bg='#ffdddd')

root.mainloop()