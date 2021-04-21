"""
score
missing docstring of comment (-5)

"""

from tkinter import *
import time
root = Tk()
#common requirements
#1
root.title('python gui - homework')

#2
### root.iconbitmap('IMG_2408.ico')

#extra requirements
#1
print('The proportion must be width:height = 16:9')
window_width = int(input('Please enter the width of your window:'))
window_height = int(input('Please enter the height of your window:'))
#2
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
pos_x = int(round(screen_width/2 - window_width/2))
pos_y = int(round(screen_height/2 - window_height/2))
root.geometry('{}x{}+{}+{}'.format(window_width,window_height,pos_x,pos_y))
#3
root.config(bg='LightPink1')
#4
root.attributes("-topmost", True)
#5
root.maxsize(1600, 900)
root.minsize(300, 200)
#6
root.resizable(True,1)
root.update()
#7
print('The initial window width is:',root.winfo_width(), 'The initial window height is:',root.winfo_height())
#8

root.geometry(f'{500}x{350}+{int(round(screen_width/2-500/2))}+{int(round(screen_height/2-350/2))}')
time.sleep(3)
root.update()
#9
print('The new window width is:',root.winfo_width(),'The initial window height is:',root.winfo_height())
#run program
root.mainloop()
