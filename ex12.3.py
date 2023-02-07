class Voiture:
    "Classe de voiture"

    def __init__(self, m = "ford", c = "rouge", p = "personne", v = 0):
        self.marque = m
        self.couleur  = c
        self.pilote = p
        self.vitesse  = v


    def choix_de_conducteur(self, p):
        self.pilote = p


    def accelerer(self,taux, duree):
        if self.pilote == "personne":
            print "Cette voiture n'a pas de conducteur !"
        else:
            self.vitesse = taux * duree


    def afficher_tout(self):
        print " marque " +  self.marque + " couleur " + self.couleur + \
              " pilotée par " + self.pilote + ", vitesse = %s m/s " %(self.vitesse)
        
