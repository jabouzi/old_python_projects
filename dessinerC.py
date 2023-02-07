from cercle import *
from curseur import *

class DessinerCercle(Frame):
    def __init__(self,master = None):
        Frame.__init__(self)
        self.trace= [0]*1
        
        self.crl = Cercle(self, 600, 400, 'light grey')
        self.crl.pack(side = TOP)

        self.gra = Grandeur(self)
        self.gra.pack()
        
        self.master.bind('<Control-Z>',self.montreCercle)
        self.master.title('Dessiner un cercle')
        #self.master.iconbitmap("skander.ico")
        self.pack()

    def montreCercle(self,event):
        for i in range(1):            
            self.crl.delete(self.trace[i])            
            if self.gra.chk.get():
                self.trace[i] = self.crl.dessiner_cercle(                                    
                                    rn = self.gra.r,
                                    cx = self.gra.x,
                                    cy = self.gra.y)
        
if __name__ == '__main__':
     DessinerCercle().mainloop()
      
