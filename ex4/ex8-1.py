from Tkinter import *
from random import randrange

def drawline():
	global x1, y1, x2, y2, coul
	can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
	
	x2, x1 = x2 + 5, x1 + 5
	
	
def changecolor():
	global coul
	pal = ['cyan','maroon','green']
	c = randrange(3)
	coul = pal[c]
	
	
#def main():
x1, y1, x2, y2 = 0, 200, 0, 0
coul = 'dark green'
	
fen1 = Tk()
can1 = Canvas(fen1,bg='dark grey',height=200, width=200)
can1.pack(side=LEFT)
	
bou1 = Button(fen1, text='Quitter',command = fen1.quit)
bou1.pack(side=TOP)
bou2 = Button(fen1, text='Tracer',command = drawline)
bou2.pack()
bou3 = Button(fen1, text='Autre couleur',command = changecolor)
bou3.pack()
	
fen1.mainloop()
fen1.destroy()
	
	
#main()

