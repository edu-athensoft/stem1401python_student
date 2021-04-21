from datetime import datetime
from tkinter import Label

from pythonProject.day_06.day_07.package_day_09.file_dir_14 import root


def strfttime():
    pass


def run_counter(digit):
    counter = 0
    root = strfttime()
    print("Counter")

    def strftime():
        nonlocal counter
        counter += 1
        print(counter)
        digit.config(text=counter)

        if counter >= 15:
            digit.config(text="END")
            return
        else:
            digit.after(1000, strftime)

    strftime()

root.title('Python GUI - Counter')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')



digit_label = Label(root,
                    bg='seagreen',
                    fg='white',
                    height=3,
                    width=10,
                    font="Helvetic 32 bold")
digit_label.pack()



run_counter(digit_label)


root.mainloop()

