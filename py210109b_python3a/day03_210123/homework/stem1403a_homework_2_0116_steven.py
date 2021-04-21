"""
center our window
"""

"""
score
perfect

"""

import tkinter as tk
root = tk.Tk()

root.title("Python GUI - Title")

# root.iconbitmap('')

x = int(root.winfo_screenwidth()/2 - 800/2)
y = int(root.winfo_screenheight()/2 - 450/2)
root.geometry("{}x{}+{}+{}".format(800,450,x,y))

root.mainloop()
