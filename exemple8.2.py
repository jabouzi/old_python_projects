# -*- coding: cp1252 -*-
from Tkinter import *

def ligne(x1,y1,x2,y2):
    cadre.create_line(x1,y1,x2,y2,fill='black')
     
    
def souris (event):
    cadre.focus_set()
    cadre.delete(ALL)    
    texte.configure(text = "Mouvement en X = " + str(event.x) + \
                    ", Y = " + str(event.y))     
    ligne(event.x,0,event.x,405)
    ligne(0,event.y,405,event.y)
    txt = " X = "+ str(event.x) + ", Y = " + str(event.y)
    cadre.create_text(200,200,text = txt,justify = CENTER)

def fleche(event):
    cadre.focus_set()
    cadre.delete(ALL)
    txt = "pressed : " + repr(event.keysym)
    texte.configure(text = "Touche = " + str(event.keysym))
    #print "pressed", repr(event.keysym)
    #if event.keysym == "Down":        
    cadre.create_text(200,200,text = txt ,justify = CENTER)
        
fen = Tk()
cadre = Canvas(fen, width = 400, height = 400, bg = "grey")
cadre.bind("<Motion>",souris)
cadre.bind("<KeyPress>",fleche)
cadre.pack()
cadre.focus_set()
texte = Label(fen)
texte.pack()

fen.mainloop()
