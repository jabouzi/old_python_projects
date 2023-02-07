class Domino:
    "Classe de jeux de domino"
    def __init__(self, f1 = 0, f2 = 0):
        self.face1 = f1
        self.face2 = f2

    def afficher_point(self):
        print "Face A : " + str(self.face1) + "Face B : " + str(self.face2)

    def valeur(self):
        return self.face1 + self.face2

    
