"""
close a window

root.destroy()

root.quit()

"""

import tkinter as tk
import time

root = tk.Tk()
root.title('Python GUI - refreshing a window state')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

print("closing...")
# time.sleep(3)

btn1 = tk.Button(root, text='Close', command=root.destroy)
btn1.pack()

root.mainloop()