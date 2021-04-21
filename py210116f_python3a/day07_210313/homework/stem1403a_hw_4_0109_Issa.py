import tkinter as tk
import webbrowser


def link(url):
    webbrowser.open_new(url)


root = tk.Tk()
root.title("Myself - Issa")

window_width = 1500
window_height = 675

screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

x = int(screenwidth/2 - window_width/2)
y = int(screenheight/2 - window_height/2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.config(bg="gray")

phrases = ["Hey!",
           "How are you?",
           "My name is Issa.",
           "I am 15.",
           "I love to play basketball.",
           "I go to the College Jean-de-Brébeuf.",
           "I love dogs.",
           "In fact, I will have a samoyed.",
           "Samoyeds are the best dog.",
           "Here's a link of a picture of a samoyed: http://sonderlives.com/wp-content/uploads/2018/08/samoyed11.jpg"]


for phrase in phrases:
    labels = tk.Label(root, bg="white", fg="red", font="Vrinda", text=phrase, padx=20, pady=10)
    labels.pack()

    # here
    TARGET = 'http'
    if TARGET in phrase:
        pos = phrase.index(TARGET)
        print(pos)
        url = phrase[pos:]
        labels.bind("<Button-1>", lambda e: link(url))
    # else:
    #     pos = -1

label_2 = tk.Label(root, bg="white", fg="red", font="Vrinda", text="Here is another link because they are just too cute: https://www.samoyedclubofamerica.org/wp-content/uploads/2014/12/latesummersnow-USED.jpg", padx=20, pady=10)
label_2.pack()
label_2.bind("<Button-2>", lambda e: link("https://www.samoyedclubofamerica.org/wp-content/uploads/2014/12/latesummersnow-USED.jpg"))

root.mainloop()

