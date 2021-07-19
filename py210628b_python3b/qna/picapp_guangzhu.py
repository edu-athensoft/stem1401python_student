"""
Question description:
cannot open image

Question posted by Guangzhu Cui

Date: 2021-06-28
"""

from tkinter import *
root = Tk()
root.title("Klee banner wish")
root.geometry('1374x680')

# banner
banner_image = PhotoImage(file='./banner_img/klee_banner.png')
background_banner = Label(root, image=banner_image)
background_banner.place(x=0, y=0, relwidth=1, relheight=1)

# wish bar x1
wish_x1_image = PhotoImage(file='./banner_img/x1_wish_img.png')
wish_x1_button = Button(root, image=wish_x1_image, width=270, height=62, anchor=S)
wish_x1_button.place(x=50, y=500)

# wish bar x10
wish_x10_image = PhotoImage(file='./banner_img/x10_wish_img.png')
wish_x10_button = Button(root, image=wish_x10_image, width=270, height=62, anchor=S)
wish_x10_button.place(x=50, y=565)

root.mainloop()