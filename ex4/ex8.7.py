
from Tkinter import *
from random import randrange

def drawoval():
	global x1, y1, x2, y2, coul
	#can1.create_oval(x1,y1,x2,y2,width=4,fill='white')
	can1.create_oval(100,120,250,270,width=2,outline='red')
	can1.create_oval(220,120,370,270,width=2,outline='yellow')
	can1.create_oval(340,120,490,270,width=2,outline='green')	
	can1.create_oval(150,195,300,345,width=2,outline='blue')
	can1.create_oval(275,195,425,345,width=2,outline='black')
	#y2, y1 = y2 + 15, y1 - 15	
	
def effacer():
	can1.delete(ALL)
	
#def main():
x1, y1, x2, y2 = 0, 10, 600, 400
coul = 'dark green'
	
fen1 = Tk()
can1 = Canvas(fen1,bg='white',height=400, width=600)
can1.pack(side=TOP, padx = 5, pady = 5)
	
bou1 = Button(fen1, text='Quitter',command = fen1.quit)
bou1.pack(side=RIGHT)
bou2 = Button(fen1, text='J.O', command = drawoval)
bou2.pack(side=LEFT)
bou3 = Button(fen1, text='Effacer', command = effacer)
bou3.pack()
	
fen1.mainloop()
#fen1.destroy()
	
	
#main()

