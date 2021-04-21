"""
maximize a window

"""

import tkinter as tk
import time

root = tk.Tk()
root.title('Python GUI - maximize a window')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.update()


time.sleep(1)
# maximize
root.state('zoomed')

# restore



# root.update()

def restore():
    print('restoring')
    root.state('normal')
    # root.update()

btn1 = tk.Button(root, text='Restore', command=restore)
btn1.pack()

root.mainloop()