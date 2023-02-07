# -*- coding: cp1252 -*-

from Tkinter import *

class Cercle(Canvas):
    def __init__(self,master = None,larg = 400, haut = 400, coul = 'white'):
        Canvas.__init__(self)
        self.configure(width = larg, height = haut,bg = coul)
        self.larg, self.haut, self.coul = larg, haut, coul

        # tracé d'une échelle avec 8 graduations :
        pas = (larg-25)/8.          # intervalles de l'échelle horizontale
        for t in range(0,9):
            stx = 10 + t*pas        # +10 pour partir de l'origine
            #self.create_line(stx, haut/2-4, stx, haut/2+4)
            self.create_line(stx, haut/10, stx, haut*9/10)
            
        pas = haut*2/25            # intervalles de l'échelle horizontale
        for t in range(-5, 6):
            sty = haut/2 -t*pas      # haut/2 pour partir de l'origine
            #self.create_line(8,sty,13, sty)
            self.create_line(10, sty, larg-15, sty)

        # tracé des axes de référence :
        self.create_line(10, haut/2, larg, haut/2, arrow=LAST)    # axe X
        self.create_line(larg/2 - 2, haut,larg/2 - 2, 10,  arrow=LAST)# axe Y

    def dessiner_cercle(self,rn = 100, cx =0, cy = 0):
        n = self.create_oval((self.larg/2 + cx)- rn, (self.haut/2 - cy) - rn,
                             (self.larg/2 + cx)+ rn, (self.haut/2 - cy) + rn)
        return n

if __name__ == '__main__':
    root = Tk()
    Crl = Cercle(root, 600, 400, 'grey')
    Crl.pack()
    print Crl.dessiner_cercle(125,-300,-200)
    root.mainloop()
