# -*- coding: cp1252 -*-
from Tkinter import *

fen = Tk()
fen.iconbitmap("Skander3.ico")
fen.title("Premier test")
text = Label(fen, text = 'Premi�re fen�tre',fg = 'red', bd = 10)
text.pack()
bout = Button(fen,text = 'Quitter',command = fen.destroy)
bout.pack()
fen.mainloop()
