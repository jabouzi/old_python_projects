from cercle import *
from curseur import *

class DessinerCercle(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.cercle = [0]
        self.crl = Cercle(self, 600, 400, 'light grey')
        self.crl.pack(side = TOP)

        self.gra = Grandeur(self)
        self.gra.pack()
        
        self.master.bind('<Button-1>',self.montreCercle)
        self.pack()

    def montreCercle(self,event):
        self.crl.delete(ALL)
        if self.gra.chk.get():
            self.cercle[0] = self.crl.dessiner_cercle(self.gra.r,
                                                  self.gra.x,
                                                  self.gra.y)
        print self.cercle[0]
if __name__ == '__main__':
     DessinerCercle().mainloop()
      
