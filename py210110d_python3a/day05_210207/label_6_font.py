"""
label font
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - Label font')

winw= 640
winh= 480
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

# create a Label
label1 = tk.Label(root, text='My Text Label', width=50, height=3, bg='blue', fg='white',
                  font="Helvetica 20 bold")
label1.pack()

# create a Label
label2 = tk.Label(root, text='My Text Label 2',width=30, height=5, bg='red',fg='yellow',
                  font="Times 16 italic underline")
label2.pack()

# create a Label
label3 = tk.Label(root, text='My Text Label 2',width=30, height=5, bg='blue',fg='yellow',
                  font='"Arial Narrow" 16')
label3.pack()

root.mainloop()