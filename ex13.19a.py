from Tkinter import *

class Grandeur(Frame):
    def __init__(self, master = None, coul = 'red'):
        Frame.__init__(self)
        self.x, self.y, self.r, self.coul = 0,0,0, coul
        Scale(self, length = 500, orient = HORIZONTAL, sliderlength = 20,
              label = 'Valeur x du centre :', from_ = 0, to = 200, tickinterval = 10,
              showvalue = 0, command = self.setX).pack(side = TOP)
        Scale(self, length = 500, orient = HORIZONTAL, sliderlength = 20,
              label = 'Valeur Y du centre :', from_ = 0, to = 200, tickinterval = 10,
              showvalue = 0, command = self.setY).pack(side = BOTTOM)
        Scale(self, length = 500, orient = HORIZONTAL, sliderlength = 20,
              label = 'Valeur du rayon :', from_ = 0, to = 200, tickinterval = 10,
              showvalue = 0, command = self.setR).pack(side = BOTTOM)

    def setX(self, x):
        self.x = int(x)

    def setY(self, y):
        self.y = int(y)

    def setR(self, r):
        self.r = int(r)



if __name__ == '__main__':
    root = Tk()
    gr = Grandeur(root, 'blue')
    gr.pack()
    #gr.configure(text = ' x = '+ str(gr.x) + ' y = ' + str(gr.y)
                # + ' rayon = '+ str(gr.r))
    root.mainloop()

    
