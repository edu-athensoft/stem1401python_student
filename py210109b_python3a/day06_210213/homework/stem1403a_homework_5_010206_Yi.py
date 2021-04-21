"""
Homework 5
"""

"""
score
perfect

"""

import tkinter as tk
import time

root = tk.Tk()
root.title("Python GUI - Center")
# root.iconbitmap("IMG_2408.ico")

win_width = 640
win_height = 480

positionRight = int(root.winfo_screenwidth() / 2 - win_width/2 )
positionDown = int(root.winfo_screenheight() / 2 - win_height/2 )

root.maxsize(900, 600)
root.minsize(100, 70)

mytext = 'MyText Label 4'
label2 = tk.Label(root, text=mytext,
                  width=30, height=7,
                  bg='blue', fg='#ffffff',
                  anchor=tk.N)
label2.pack()

root.geometry(f"{win_width}x{win_height}+{positionRight}+{positionDown}")

mytext = 'My Text Label bitmap'
label1 = tk.Label(root,bg='green',text='my Label 1',
                  compound='right',bitmap = 'error',
                  font= 'Helvetica 20 italic underline',
                  padx = 20, pady= 10)
label2 = tk.Label(root,bg='red',text='my Label 2',
                  compound='bottom',bitmap = 'info',
                  font= 'Helvetica 24 italic overstrike',
                  padx = 20, pady= 10)
label3 = tk.Label(root,bg='white',text='my Label 3',
                  compound='center',bitmap = 'questhead',
                  font= '"Segoe UI" 20 italic underline overstrike',
                  padx = 20, pady= 10)
label4 = tk.Label(root,bg='white',text='my Label 4',
                  compound='left',bitmap = 'question',
                  padx = 20, pady= 10)
label5 = tk.Label(root,bg='white',text='my Label 5',
                  compound='top',bitmap = 'warning',
                  padx = 20, pady= 10)

# display labels
for i in range(1, 6):
    obj = 'label' + str(i)
    eval(obj).pack()


root.mainloop()