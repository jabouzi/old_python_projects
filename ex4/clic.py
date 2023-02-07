############################################################################
#    Copyright (C) 2006 by Skander   #
#    skander@(none)   #
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

from Tkinter import *
from math import *

def cercle(x, y):
	cadre.create_oval(x - 5, y - 5, x + 5, y + 5, fill = 'dark red')
		
def evaluer(event):
	chaine.configure(text = "Resultat = " + str(eval(entree.get())))

def poiteur(event):
	chaine.configure(text ="Clic detecte en X =" + str(event.x) + ", Y =" + str(event.y))
	cadre.delete(ALL)
	cercle(event.x, event.y)
	
fen = Tk()
entree = Entry(fen)
cadre = Canvas(fen, width = 200, height = 150, bg = "light yellow")
chaine = Label(fen)
#resultat = Label(fen)
entree.bind("<Key>", evaluer)
cadre.bind("<Button-1>", poiteur)
entree.pack()
cadre.pack()
chaine.pack()
#resultat.pack()

fen.mainloop()
