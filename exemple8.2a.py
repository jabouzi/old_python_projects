from Tkinter import *
from math import *
def ligne(x,y,x1,y1):
    cadre.create_line(x,y,x+100,y,fill='blue')
    cadre.create_line(x,y,x,y+100,fill='blue')
    cadre.create_line(x+100,y+100,x+100,y,fill='blue')
    cadre.create_line(x,y+100,x+100,y+100,fill='blue')
    cadre.create_line(x1,y1,x1+100,y1,fill='blue')
    cadre.create_line(x1,y1,x1,y1+100,fill='blue')
    cadre.create_line(x1+100,y1+100,x1+100,y1,fill='blue')
    cadre.create_line(x1,y1+100,x1+100,y1+100,fill='blue')
    cadre.create_line(x,y,x1,y1,fill='blue')
    cadre.create_line(x,y+100,x1,y1+100,fill='blue')
    cadre.create_line(x+100,y,x1+100,y1,fill='blue')
    cadre.create_line(x+100,y+100,x1+100,y1+100,fill='blue')
    
def souris (event):
    texte.configure(text = "Mouvement en X = " + str(event.x) + \
                    ", Y = " + str(event.y))    

    cadre.delete(ALL)
    ligne(event.x,event.y,event.x + 125,event.y + 125)
    #ligne(0,event.y,405,event.y)
def click(event):
    cadre.delete(ALL)
    ang = 
    ligne(cos(15),event.y,cos(15)+ 125,event.y + 125)

def click2(event):
    cadre.delete(ALL)
    ligne(event.x,sin(24),event.x+ 125,sin(24)+ 125)

fen = Tk()
fen.iconbitmap("skander.ico")
fen.title("Test de Rotation")
cadre = Canvas(fen, width = 400, height = 400, bg = "white")
cadre.bind("<Motion>",souris)
cadre.bind("<Button-1>",click)
cadre.bind("<Button-3>",click2)

cadre.pack()
texte = Label(fen)
texte.pack()

fen.mainloop()
