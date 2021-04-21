"""
set image icon for a window

image icon format:   .ico

square  8x8, 16x16, 32x32, 64x64

.jpg
.png
.gif
.bmp
.tiff

step 1. get an image
step 2. convert it to .ico
step 3. install icon image to work folder
step 4. set icon

"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - setting image icon')

# setting size
root.geometry('640x480+300+200')

# setting icon
root.iconbitmap('./img/IMG_2408.ico')
root.iconbitmap('img/IMG_2408.ico')


root.mainloop()


