"""
[Homework] 2021-01-17
1. Create a main window with specified width and height
user may input width and height
2. Please center the window
3. Please add image icon to your window
"""

"""
score
improper file name (-1)

"""

import tkinter as tk

root = tk.Tk()

# settings
root.title('Python GUI - Homework')
# root.iconbitmap("IMG_2408.ico")

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

# init posx, posy, sizex, sizey

posx = int(sw / 2 - 800 / 2)
posy = int(sh / 2 - 450 / 2)

sizex = int(input("Enter the width of the window"))
sizey = int(input("Enter the height of the window"))

root.geometry("{}x{}+{}+{}".format(sizex, sizey, posx, posy))

root.mainloop()