"""
close a window

root.destroy()
root.quit()

"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - close window')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

print("closing...")

btn1 = tk.Button(root, text='Close', command=root.destroy)
btn1.pack()

root.mainloop()