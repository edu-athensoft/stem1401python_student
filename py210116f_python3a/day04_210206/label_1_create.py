"""
create a Label
"""


import tkinter as tk

root = tk.Tk()
root.title('Python GUI - set min size for a window')

winw= 640
winh= 480
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddddff')

# create a Label
label1 = tk.Label(root, text='My Text Label')

# place onto window
label1.pack()

root.mainloop()
