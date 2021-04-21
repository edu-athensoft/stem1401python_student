"""
create a label
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - subtopic')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

# create a label
label1 = tk.Label(root, text='My Text Label 1')
label1.pack()

# create a label
label2 = tk.Label(root, text='My Text Label 2')
label2.pack()


root.mainloop()