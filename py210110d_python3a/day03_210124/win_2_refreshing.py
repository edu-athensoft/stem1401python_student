"""
refreshing

root.update()
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - subtopic')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

w = root.winfo_width()
h = root.winfo_height()
print(f'w={w}, h={h}')

# refreshing
root.update()

w = root.winfo_width()
h = root.winfo_height()
print(f'w={w}, h={h}')

root.mainloop()