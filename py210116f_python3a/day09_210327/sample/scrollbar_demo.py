"""
Scrollbar
https://www.pynote.net/archives/1284
"""

import tkinter as tk

root = tk.Tk()

text = tk.Text(root)
text.pack(side=tk.LEFT)
text.config(width=24)

scrollbar = tk.Scrollbar(root, command=text.yview)
text.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


root.mainloop()