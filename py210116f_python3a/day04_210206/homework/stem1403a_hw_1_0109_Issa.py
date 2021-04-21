"""
Date: 2021-01-30
1. Design a main window for a GUI application
Requirements:
 Use your own logo icon, you may create or download an icon in format of ico
 Set dimension of window at the ratio of 16:9
 Set a proper title for your main window
 Center your main window
 Set max size for the window
 Get initial size of the window and print them out
 Get current size of the window and print them out
"""

import tkinter as tk
import time

root = tk.Tk()

root.title("Red Car")

root.iconbitmap("./BMW6.ico")



window_width = 800
window_height = 450

screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

x = int(screenwidth/2 - window_width/2)
y = int(screenheight/2 - window_height/2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.maxsize(1200, 675)

# added by Athens
print(f"Initial size is: {root.winfo_width()}: {root.winfo_height()}")
root.update()

time.sleep(5)
print(f"Current size, after 5 seconds, is: {root.winfo_width()}: {root.winfo_height()}")

root.mainloop()
