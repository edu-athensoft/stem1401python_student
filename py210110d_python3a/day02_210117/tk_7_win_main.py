"""
to create a main window
to set a title
to set image icon
to set size
to set initial position
to set background image
"""

import tkinter as tk

root = tk.Tk()

# settings
root.title('Python GUI - Title')
root.iconbitmap('IMG_2408.ico')

# root.geometry("800x450+300+200")
# root.geometry("800x450-300+200")
# root.geometry("800x450-300-200")

root.configure(bg='#ddddff')

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

# print(root.winfo_screenwidth())
# print(root.winfo_screenheight())

ww = 800
wh = 450

# init posx, posy
posx = int(sw/2 - ww/2)
posy = int(sh/2 - wh/2)

root.geometry(f"{ww}x{wh}+{posx}+{posy}")

root.mainloop()


