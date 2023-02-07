# -*- coding: cp1252 -*-
from Tkinter import *
val = ['0','1','2','3','4','5','6','7','8','A','B','C','D','E','F']
val2 = [0x0,0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8]
#v = StringVar()
def updateLabel(x):
    lab.configure(text='Valeure actuelle = ' + x)

root = Tk()
Scale(root, takefocus = 0, length = 300, orient = VERTICAL, label = 'Réglage :',
      troughcolor = 'dark grey', sliderlength = 20,
      showvalue = 0, from_ = 0x0, to = 0xF, tickinterval = 0x1,
      command = updateLabel).pack()
lab = Label(root)
lab.pack()
#Scale.get()focus_set()
root.mainloop()
