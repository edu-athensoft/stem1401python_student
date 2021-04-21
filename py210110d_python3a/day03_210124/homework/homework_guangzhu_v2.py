"""
[Homework] 2021-01-17
1. Create a main window with specified width and height
user may input width and height
2. Please center the window
3. Please add image icon to your window
"""

"""
score
improper file name (-1)

"""

from tkinter import *
try:
    window_height = None
    window_width = None

    window_height = int(input('Please enter the height of your window:'))
    window_width = int(input('Please enter the width of your window:'))

except Exception as e:
    print('Please input valid number')


root = Tk()
root.title('Python GUI - Title')

try:
    root.iconbitmap('./img/IMG_2408.ico')
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    winwidth = 800
    winheight = 450
    posx = int(sw / 2 - winwidth / 2)
    posy = int(sh / 2 - winheight / 2)

    root.geometry(f'{window_width}x{window_height}+{posx}+{posy}')
    root.mainloop()

except FileNotFoundError as fe:
    print('No such image icon file.')
except Exception as e:
    print(e)


