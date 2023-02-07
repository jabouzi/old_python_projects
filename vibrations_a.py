#! /usr/bin/env python
# -*- coding: Latin-1 -*-

from oscillo import *
from curseurs import *

class ShowVibra(Frame):
    "D�monstration de mouvements vibratoires harmoniques"
    def __init__(self, master =None):
        Frame.__init__(self, master)        # constr. classe parente
        self.couleur=['white','white','white']
        self.trace=[0]*1            # liste des trac�s
        #self.controle=[0]*3         # liste des panneaux de contr�le

        # Instanciation du canevas avec axes X et Y :
        self.gra = OscilloGraphe(self, larg =600, haut=400)
        self.gra.configure(bg ='grey', bd=4, relief=GROOVE)
        self.gra.pack(side =TOP, pady=5)

        # Instanciation de 3 panneaux de contr�le (curseurs) :
        #for i in range(3):
        self.controle = ChoixVibra(self,'black')
        self.controle.pack()

        # D�signation de l'�v�nement qui d�clenche l'affichage des trac�s :
        self.master.bind('<Control-Z>', self.montreCourbes)

        # Mise en place :
        self.master.title('Mouvements vibratoires harmoniques')
        self.pack()

    def montreCourbes(self,event):
        "(r�)affichage des 3 graphiques �longation/temps"
        #for i in range(3):
            # D'abord, effacer le trac� pr�c�dent (�ventuel) :
        self.gra.delete(self.trace[0])
            # Ensuite, dessiner le nouveau trac� :
        if self.controle.chk.get():
            self.trace[0] = self.gra.traceCourbe(
                                    coul=self.couleur[1],
                                    freq=self.controle.freq,
                                    phase=self.controle.phase,
                                    ampl=self.controle.ampl)
            print self.trace

#### Code pour tester la classe : ###

if __name__ == '__main__':
    ShowVibra().mainloop()
