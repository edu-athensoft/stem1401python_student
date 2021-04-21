"""
[Homework]
Date: 2021-01-24
Write a Python GUI program to create your own window
Common requirements:
1. set a title
2. set an image icon
Extra requirements:
1. specify dimension at 16:9
2. make it at center point on your screen
3. set a background color
4. make it topmost
5. set max size and min size
6. make it resizable
7. print out the initial height and width of your window at console
8. resizing your window
9. print out the current height and width of your window at console
"""

"""
score
not executable (-35)

"""

import tkinter as tk

root = tk.Tk()

# 1.
root.title("Python GUI - Homework")

# 2.
### root.iconbitmap("IMG_2408.ico")

# extra requirements
# 1. and 2.
width = int(input("Please input the width of the window (Note that width:height must be equal to 16:9)"))
height = int(input("Please input the height of the window (Note that width:height must be equal to 16:9)"))
root.geometry("{}x{}+{}+{}".format(width, height, root.winfo_screenwidth()/2 - width/2, root.winfo_screenheight()/2 - height/2))

# 3.
root.config(bg="gold")

# 4.
root.attributes('-topmost', True)

# 5.
root.maxsize()
root.minsize(300, 200)

# 6.
root.resizable(True, True)

root.update()

# 7.
print("Height = {}, Width = {}".format(root.winfo_height(), root.winfo_width()))

# 8.
root.geometry("{}x{}+{}+{}".format(600, 400, root.winfo_screenwidth()/2 - 600/2, root.winfo_screenheight()/2 - 400/2))

root.update()

# 9.
print("Height = {}, Width = {}".format(root.winfo_height(), root.winfo_width()))

root.mainloop()