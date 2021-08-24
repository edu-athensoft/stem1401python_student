"""
menu

basic menu and menu option
"""

from tkinter import *
from tkinter import messagebox


def test_menu1():
    messagebox.showinfo("Test", "Menu 1 is clicked")


def test_menu2():
    messagebox.showinfo("Test", "Menu 2 is clicked")


main = Tk()
main.title("Athensoft Python Course | Menu")
main.geometry("640x480+300+300")

# define menu and menu items
menubar = Menu(main)
menubar.add_command(label="MENU_1", command=test_menu1)
menubar.add_command(label="MENU_2", command=test_menu2)
menubar.add_command(label="Exit", command=main.destroy)

menubar2 = Menu(main)
menubar2.add_command(label="2MENU_1", command=test_menu1)
menubar2.add_command(label="2MENU_2", command=test_menu2)
menubar2.add_command(label="2Exit", command=main.destroy)


# set menu
main.config(menu=menubar2)

main.mainloop()