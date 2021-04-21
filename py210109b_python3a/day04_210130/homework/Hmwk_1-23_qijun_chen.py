"""
[Homework] 2021-01-23
Create your own window
requirements:
1. make it at center point on your screen
2. specify dimension at 16:9
3. set a background color
4. make it topmost
5. make it non-resizable
6. print out the window's height and width at console
Due date: by the end of next Friday
"""


import tkinter as tk
import time

root = tk.Tk()
root.title("Python GUI - Center")
# root.iconbitmap("IMG_2408.ico")

width = 640
height = 480

rightpos = int(root.winfo_screenwidth() / 2 - width/2 )
downpos = int(root.winfo_screenheight() / 2 - height/2 )

root.maxsize(900, 600)
root.minsize(100, 70)

root.geometry(f"{width}x{height}+{rightpos}+{downpos}")
root.update()
time.sleep(1)

root.update()
root.configure()
time.sleep(1)

root.update()
root.configure()
time.sleep(1)

root.update()
root.configure()