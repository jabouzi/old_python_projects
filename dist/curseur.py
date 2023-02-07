from Tkinter import *

class Grandeur(Frame):
    def __init__(self, maitre = None, coul = 'red'):
        Frame.__init__(self)
        self.x, self.y, self.r, self.coul = 0,0,0, coul
        self.chk = IntVar()
        Checkbutton(self,text = 'Afficher!',variable = self.chk,
                    command = self.set_).pack(side = TOP)
        Scale(self, length = 800, orient = HORIZONTAL, sliderlength = 20,
              label = 'Valeur x du centre :', from_ = -300, to = 300, tickinterval = 20,
              showvalue = 0, command = self.setX).pack(side = TOP)
        Scale(self, length = 800, orient = HORIZONTAL, sliderlength = 20,
              label = 'Valeur y du centre :', from_ = -300, to = 300, tickinterval = 20,
              showvalue = 0, command = self.setY).pack()
        Scale(self, length = 800, orient = HORIZONTAL, sliderlength = 20,
              label = 'Valeur du rayon :', from_ = 0, to = 300, tickinterval = 10,
              showvalue = 0, command = self.setR).pack(side = BOTTOM)

    def set_(self):
        self.event_generate('<Control-Z>')
    def setX(self, x):
        self.x = int(x)
        self.event_generate('<Control-Z>')
    def setY(self, y):
        self.y = int(y)
        self.event_generate('<Control-Z>')
    def setR(self, r):
        self.r = int(r)
        self.event_generate('<Control-Z>')
        
    #print self.chk.get()

if __name__ == '__main__':
    def afficherTout(event=None):
        lab.configure(text = '%s - %s - %s - %s' %
                         (gr.chk.get(), gr.x, gr.y, gr.r))
    root = Tk()
    gr = Grandeur(root, 'blue')
    gr.pack()
    lab = Label(root, text ='test')
    lab.pack()
    #gr.configure(text = ' x = '+ str(gr.x) + ' y = ' + str(gr.y)
                 #+ ' rayon = '+ str(gr.r))
    root.bind('<Control-Z>', afficherTout)
    root.mainloop()

    
