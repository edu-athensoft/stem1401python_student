"""
create a Label
"""


import tkinter as tk

root = tk.Tk()
root.title('Python GUI - Text Label')

winw= 640
winh= 480
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddddff')

# create a Label
label1 = tk.Label(root, text='My Text Label 1')
label1.pack()

# create a Label
label2 = tk.Label(root, text='My Text Label 2')
label2.pack()

# create a Label
label3 = tk.Label(root, text='My Text Label 3')
label3.pack()


root.mainloop()
