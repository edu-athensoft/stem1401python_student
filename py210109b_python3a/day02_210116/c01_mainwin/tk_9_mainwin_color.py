"""
set background color
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - Background color')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

tk.mainloop()