
class Cercle:
    "Classe de cercle"
    def __init__(self,rayon):
        print "Construction d'un cercle\n"
        self.rayon = rayon
        self.nom = "Cercle"

    def surface(self):
        print "Surface d'un cercle\n"
        return 3.1416 * (self.rayon ** 2)


class Cylindre(Cercle):
    "Classe de cylindre"
    def __init__(self,rayon,hauteur):
        print "Construction d'un cylindre\n"
        Cercle.__init__(self,rayon)
        #self.rayon = rayon
        self.hauteur = hauteur
        self.nom = "Cylindre"

    def volume(self):
        print "Volume d'un cylindre\n"
        return Cercle.surface(self) * self.hauteur


class Cone(Cylindre):
    def __init__(self,rayon,hauteur):
        print "Construction d'un cone\n"
        Cylindre.__init__(self,rayon,hauteur)
        self.nom = "Cone"

    def volume(self):
        print "Volume d'un cone\n"
        return Cylindre.volume(self) / 3
