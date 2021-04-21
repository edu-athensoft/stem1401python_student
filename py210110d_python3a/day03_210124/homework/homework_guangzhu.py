"""
[Homework] 2021-01-17
1. Create a main window with specified width and height
user may input width and height
2. Please center the window
3. Please add image icon to your window
"""

from tkinter import *

root = Tk()
root.title('Python GUI - Title')
# root.iconbitmap('IMG_2408.ico')
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

posx = int(sw/2 - 800/2)
posy = int(sh/2 - 450/2)

window_height = int(input('Please enter the height of your window:'))
window_width = int(input('Please enter the width of your window:'))

root.geometry(f'{window_width}x{window_height}+{posx}+{posy}')
root.mainloop()