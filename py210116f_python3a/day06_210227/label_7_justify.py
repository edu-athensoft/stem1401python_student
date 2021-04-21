"""
Label - justify
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - label')
root.geometry(f'{640}x{480}+{200}+{200}')
root.config(bg='#ddff77')

# text label
mytext = 'My Text Label font'

label1 = tk.Label(root, text=mytext,
                  width=30, height=3,
                  bg='red', fg='#ffffff',
                  font='Helvetica 20',
                  justify='left',wraplength=180)
label1.pack()

# text label
label2 = tk.Label(root, text=mytext,
                  width=30, height=3,
                  bg='blue', fg='#ffffff',
                  font='Helvetica 20',
                  justify='right',wraplength=180)
label2.pack()


# text label
label3 = tk.Label(root, text=mytext,
                  width=30, height=3,
                  bg='red', fg='#ffffff',
                  font='Helvetica 20',
                  justify='center',wraplength=180)
label3.pack()

root.mainloop()

