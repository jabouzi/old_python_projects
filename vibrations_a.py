#! /usr/bin/env python
# -*- coding: Latin-1 -*-

from oscillo import *
from curseurs import *

class ShowVibra(Frame):
    "Démonstration de mouvements vibratoires harmoniques"
    def __init__(self, master =None):
        Frame.__init__(self, master)        # constr. classe parente
        self.couleur=['white','white','white']
        self.trace=[0]*1            # liste des tracés
        #self.controle=[0]*3         # liste des panneaux de contrôle

        # Instanciation du canevas avec axes X et Y :
        self.gra = OscilloGraphe(self, larg =600, haut=400)
        self.gra.configure(bg ='grey', bd=4, relief=GROOVE)
        self.gra.pack(side =TOP, pady=5)

        # Instanciation de 3 panneaux de contrôle (curseurs) :
        #for i in range(3):
        self.controle = ChoixVibra(self,'black')
        self.controle.pack()

        # Désignation de l'événement qui déclenche l'affichage des tracés :
        self.master.bind('<Control-Z>', self.montreCourbes)

        # Mise en place :
        self.master.title('Mouvements vibratoires harmoniques')
        self.pack()

    def montreCourbes(self,event):
        "(ré)affichage des 3 graphiques élongation/temps"
        #for i in range(3):
            # D'abord, effacer le tracé précédent (éventuel) :
        self.gra.delete(self.trace[0])
            # Ensuite, dessiner le nouveau tracé :
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
