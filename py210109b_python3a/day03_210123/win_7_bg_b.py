"""
set background color

color value

time.sleep(number_of_sec)
"""

import tkinter as tk
import time

root = tk.Tk()
root.title('Python GUI - background color')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.update()
time.sleep(1.5)

root.update()
root.configure(bg='#ddddff')
time.sleep(1.5)

root.update()
root.configure(bg='#ddffdd')
time.sleep(1.5)

root.update()
root.configure(bg='#ffdddd')


root.mainloop()