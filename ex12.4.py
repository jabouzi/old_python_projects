class Satellite:
    "Classe de simulation de satellite artificiels"

    def __init__(self,n = "Sat", m = 100, v = 0):
        self.nom = n
        self.masse = m
        self.vitesse = v

    def impultion(self,force, duree):
        self.vitesse = self.vitesse + (force * duree) / self.masse

    def afficher_vitesse(self):
        print "La vitesse du satellite %s = %s m/s" %(self.nom, self.vitesse)

    def energie(self):
        return (self.masse * (self.vitesse ** 2)) / 2
    
