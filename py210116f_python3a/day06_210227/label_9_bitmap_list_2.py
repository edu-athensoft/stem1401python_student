"""
bitmap list of label

"error"			"info"
"questhead"	    "question"
"warning"		"hourglass"
"gray75"		"gray50"
"gray25"		"gray12"


"""

import tkinter as tk
# from tkinter import *

root = tk.Tk()
root.title('Python GUI - label')

winw= 640
winh= 480
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddff77')

# create a label
mytext = 'My Text Label bitmap'

"""
label1 = tk.Label(root,bg='white',bitmap = 'error',padx = 20, pady= 10)
label2 = tk.Label(root,bg='white',bitmap = 'info',padx = 20, pady= 10)
label3 = tk.Label(root,bg='white',bitmap = 'questhead',padx = 20, pady= 10)
label4 = tk.Label(root,bg='white',bitmap = 'question',padx = 20, pady= 10)
label5 = tk.Label(root,bg='white',bitmap = 'warning',padx = 20, pady= 10)
label6 = tk.Label(root,bg='white',bitmap = 'gray75',padx = 20, pady= 10)
label7 = tk.Label(root,bg='white',bitmap = 'hourglass',padx = 20, pady= 10)
label8 = tk.Label(root,bg='white',bitmap = 'gray50',padx = 20, pady= 10)
label9 = tk.Label(root,bg='white',bitmap = 'gray25',padx = 20, pady= 10)
label10 = tk.Label(root,bg='white',bitmap = 'gray12',padx = 20, pady= 10)
"""

bitmap_names = ["error","info","questhead","question","warning","hourglass","gray75","gray50","gray25","gray12"]

for bitmap_name in bitmap_names:
    # mylabel = tk.Label(root,bg='white',bitmap = bitmap_name, padx = 20, pady= 10)
    # mylabel.pack()

    tk.Label(root, bg='white', bitmap=bitmap_name, padx=20, pady=10).pack()


"""
# display labels
for i in range(1, 11):
    obj = 'label' + str(i)
    eval(obj).pack()


res = eval('1+2*3')
print(res)
"""
root.mainloop()



