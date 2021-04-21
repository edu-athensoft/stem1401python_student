#Homework 16 jan
#Qi Jun

"""
score

improper file name (-1)
not enough white space (-1)
delayed (-8)

"""

import tkinter as tk
root = tk.Tk()
root.title("Python GUI - Title")
x = int(root.winfo_screenwidth()/2 - 800/2)
y = int(root.winfo_screenheight()/2 - 450/2)
root.geometry("800x450+{}+{}".format(x, y))
root.mainloop()