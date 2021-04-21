"""
create a Label widget
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - Label')

winw= 640
winh= 480
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

# create a Label
label1 = tk.Label(root, text='My Text Label', width=50, height=3, bg='blue', fg='white')
label1.pack()

# create a Label
label2 = tk.Label(root, text='My Text Label 2',width=30, height=5, bg='red',fg='yellow')
label2.pack()

root.mainloop()