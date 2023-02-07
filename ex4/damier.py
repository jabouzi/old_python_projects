############################################################################
#    Copyright (C) 05 avril 2006 by Skander   #
#    jabouzi@gmail.com   #
#                                                                          #
#    This program is free software; you can redistribute it and#or modify  #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation; either version 2 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    This program is distributed in the hope that it will be useful,       #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program; if not, write to the                         #
#    Free Software Foundation, Inc.,                                       #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
############################################################################
#!/usr/bin/env python
# _*_ coding:Utf-8 _*_

from Tkinter import *
from random import randrange

def cercle(x, y):
	can.create_oval(x - 50 / 2, y - 50 / 2, x + 50 / 2, y + 50 / 2, fill = 'red')
	
def pion():
	pn = randrange(100)
	cercle(50*(pn%10)+25,50*(pn/10)+25)

def effacer():
	can.delete(ALL)

def carre(x1, y1, x2, y2):
	can.create_rectangle(x1, y1, x2, y2, fill = 'navy')
	
def damier():
	can.delete(ALL)
	ligne = 0
	case = 0
	x = 0
	y = 0
	while ligne < 10:
		while case < 10:
			carre(x, y, x + 50, y + 50)
			case += 1
			x += 100 
			#y += 50
		ligne += 1
		case = 0
		y += 50
		if (ligne % 2) == 1:
			x = 50	
		else :
			x = 0			
		
fen = Tk()
can = Canvas(fen, width = 500, height = 500, bg = 'white')
can.pack(side = TOP)
b1 = Button(fen, text = 'Damier', command = damier)
b1.pack(side = LEFT)
b2 = Button(fen, text = 'Effacer', command = effacer)
b2.pack(side = RIGHT)
b3 = Button(fen, text = 'Pion', command = pion)
b3.pack(side = LEFT)



fen.mainloop()
			