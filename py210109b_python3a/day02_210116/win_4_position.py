"""
to set initial position
"""


import tkinter as tk
# from tkinter import *

root = tk.Tk()

root.title('Python GUI - Position')

# set position
# root.geometry('800x450')
# root.geometry('800x450+300+200')
root.geometry('800x450-300+200')
root.geometry('800x450-300-200')

root.mainloop()
