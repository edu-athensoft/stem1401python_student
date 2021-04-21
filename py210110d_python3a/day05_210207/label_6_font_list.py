"""
label font
"""

import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title('Python GUI - Label font')

winw= 640
winh= 480
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

res = font.families()
print(type(res))

for f in res:
    print(f)

root.mainloop()

"""
Rockwell
Rage Italic
Perpetua Titling MT
Perpetua
Palace Script MT
OCR A Extended
Maiandra GD
Lucida Sans Typewriter
Lucida Sans
Imprint MT Shadow
Goudy Stout
Goudy Old Style
Gloucester MT Extra Condensed
Gill Sans Ultra Bold Condensed
Gill Sans Ultra Bold
Gill Sans MT Condensed
Gill Sans MT
Gill Sans MT Ext Condensed Bold
Gigi
Franklin Gothic Medium Cond
Franklin Gothic Heavy
Franklin Gothic Demi Cond
Franklin Gothic Demi
Franklin Gothic Book
Forte
Felix Titling
Eras Medium ITC
Eras Light ITC
Eras Demi ITC
Eras Bold ITC
Engravers MT
Elephant
Edwardian Script ITC
Curlz MT
Copperplate Gothic Light
Copperplate Gothic Bold
Century Schoolbook
Castellar
Calisto MT
Bookman Old Style
Bodoni MT Condensed
Bodoni MT Black
"""