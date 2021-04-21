"""
score
not executable (-35)
missing docstring of comment (-5)
not enough white spaces (-1)

"""

import tkinter
import time
print("This program will create a widget of specified size."
      " After, it is going to resize it to 500x350, then ending the program")
root = tkinter.Tk()
# window title
root.title("stem1403_ccj")

image = False
if image:
    root.iconbitmap(image)

print("enter a 16:9 ratio dimension for your widget, ")
w_width = int(input("enter the desired width for your widget: "))
w_height = int(input(" enter the desired height for your widget: "))
while w_width/w_height != 16/9 or w_width > 1600 or w_height > 900:
    print("Please enter a 16:9 ratio dimension for your widget (ex: 1600x900 or 800x450, etc...)"
          "\nMust be equal or smaller than 1600x900")
    w_width = int(input("Please enter the desired width for your widget: "))
    w_height = int(input("Please enter the desired height for your widget: "))
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
top_left_x = int(sw/2 - w_width/2)
top_left_y = int(sh/2 - w_height/2)
root.geometry(f"{w_width}x{w_height}+{top_left_x}+{top_left_y}")
root.configure(background="bleu")
root.wm_attributes("-topmost", True)
root.maxsize(1600, 900)
root.minsize(300, 200)
root.resizable(1, 1)
root.update()
print(root.winfo_width(), "= initial width")
print(root.winfo_height(), "= initial height")
time.sleep(2)
w_width = 500
w_height = 350
top_left_x = int(sw/2 - w_width/2)
top_left_y = int(sh/2 - w_height/2)
root.geometry(f"{w_width}x{w_height}+{top_left_x}+{top_left_y}")
root.update()
