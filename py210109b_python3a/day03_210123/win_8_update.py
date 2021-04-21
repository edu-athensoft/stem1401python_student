"""
refreshing a window state
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - refreshing a window state')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
print(root.winfo_width(),root.winfo_height())

root.update()
print(root.winfo_width(),root.winfo_height())

root.mainloop()