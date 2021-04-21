"""
Homework
"""

"""
score
perfect

"""

import tkinter as tk

root = tk.Tk()

# windowWidth = root.winfo_reqwidth()
# windowHeight = root.winfo_reqheight()

win_width = 640
win_height = 480

# positionRight = int(root.winfo_screenwidth() / 2 - 400)
# positionDown = int(root.winfo_screenheight() / 2 - 225)

positionRight = int(root.winfo_screenwidth() / 2 - win_width/2)
positionDown = int(root.winfo_screenheight() / 2 - win_height/2)

# root.geometry("{ww}x{wh}+{posx}+{posy}".format(ww=win_width, wh=win_height, posx=positionRight, posy=positionDown))
root.geometry(f"{win_width}x{win_height}+{positionRight}+{positionDown}")

root.mainloop()