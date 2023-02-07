from Tkinter import *
from turtle import *

reset()
a = 0
while a < 1:
	a = a + 1
	forward(150)
	left(150)

fen1 = Tk()
tex1 = Label(fen1, text='Bonjour',fg='red')
tex1.pack()
bou1 = Button(fen1, text ='Quitter', command = fen1.destroy)
bou1.pack()
fen1.mainloop()

fen2 = Tk()
tex2 = Label(fen2, text='Skander Jabouzi', fg='black')
#tex2.pack()
fen2.mainloop()
