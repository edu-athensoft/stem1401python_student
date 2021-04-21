"""
copied source code from slack on Feb 6th, 2021

obvious error, not tested

"""

import tkinter as tk
import time
root = tk.Tk()
root.title("Blarg")
root.iconbitmap("IMG_2408.ico")
windowwidth = 2800
windowheight = 1080
positRight = int(root.winfo_screenwidth() / 2 - win_width/2 )
positDown = int(root.winfo_screenheight() / 2 - win_height/2 )
root.maxsize(2800, 1400)
root.minsize(1080, 540)
root.geometry(f"{windowwidth}x{windowheight}+{positRight}+{positDown}")
root.update()
time.sleep(1.5)