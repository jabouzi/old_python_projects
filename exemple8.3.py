from Tkinter import *
from math import *

def carree(x,y,x1,y1):
    
    #cadre.create_line(x,y,x1+100,y1,fill='blue')
    #cadre.create_line(x,y,x,y+100,fill='blue')
    #cadre.create_line(x+100,y+100,x+100,y,fill='blue')
    cadre.create_line(x,y, x1, y1,width = 10)
    #cadre.create_line(x1,y1,x1+10,y1,fill='blue')
    #cadre.create_line(x1,y1,x1,y1+10,fill='blue')
    #cadre.create_line(x1+10,y1+10,x1+10,y1,fill='blue')
    #cadre.create_line(x1,y1+10,x1+10,y1+10,fill='blue')
    #cadre.create_line(x,y,x1,y1,fill='blue')
    #cadre.create_line(x,y+10,x1,y1+10,fill='blue')
    #cadre.create_line(x+10,y,x1+10,y1,fill='blue')
    #cadre.create_line(x+10,y+10,x1+10,y1+10,fill='blue')

def cercle(x,y):
    cadre.create_oval(x, y, x + 30, y + 30,width = 2, fill = 'red')
    
def rotation():
    global x,y,x1,y1,x2,y2,x3,y3,angle
    cadre.delete(ALL)
    carree(x,y,x1,y1)
    #cercle(x,y)
    tempx = x1
    tempy = y1
    
    #x = tempx*cos(angle) - tempy*sin(angle)
    #y = tempx*sin(angle) + tempy*cos(angle)
    x1 = x + 100*cos(float(angle)*2*pi/360)
    y1 = y - 100*sin(float(angle)*2*pi/360)
    
    fen.after(100,rotation)
    

    
x = 200
y = 200
x1 = x + 100
y1 = y + 100
x2, y2= 10, 10
x3, y3= x2 + 30, y2 + 30
angle = 1
    #carree(x,y,x1,y1)
    
fen = Tk()
fen.iconbitmap("skander.ico")
fen.title(" -- Test de Rotation")
cadre = Canvas(fen, width = 400, height = 400, bg = "white")
rotation()
#rotation()
#rotation()
#carree()
#cadre.bind("<Motion>",souris)
cadre.pack()
texte = Label(fen)
texte.pack()

fen.mainloop()
    
