import random

class game:

    def __init__(self, j1, j2, manches):

        self.manches = manches
        self.nom_j1 = j1
        self.nom_j2 = j2
        self.points_1 = 0
        self.points_2 = 0

    def coups(self):
        if self.nom_j1 == 'bot':
            self.coup_1 = self.coups_bot()
        else:
            self.coup_1 = self.coups_lambda()

        if self.nom_j2 == 'bot':
            self.coup_2 = self.coups_bot()
        else:
            self.coup_2 = self.coups_lambda()
        
    def coups_lambda(self):

        a = input("Entrer le coup pour le joueur\t")
        return a

    def coups_bot(self):

        availables = ["pierre", "feuille", "ciseau"]
        z = random.choice(availables)
        return z
    
    def regles(self):
        # victoire = 0 -> nul
        # victoire = 1 -> joueur 1 gagne
        # victoire = 2 -> joueur 2 gagne
        #print(f"\nTEST // Le coup du joueur 1 est : {self.coup_1} et celui du joueur 2 est : {self.coup_2}")

        if self.coup_1 == "pierre" and self.coup_2 == "feuille":
            victoire = 2

        elif self.coup_1 == "feuille" and self.coup_2 == "feuille":
            victoire = 0

        elif self.coup_1 == "ciseau" and self.coup_2 == "feuille":
            victoire = 1

        elif self.coup_1 == "pierre" and self.coup_2 == "pierre":
            victoire = 0

        elif self.coup_1 == "feuille" and self.coup_2 == "pierre":
            victoire = 1

        elif self.coup_1 == "ciseau" and self.coup_2 == "pierre":
            victoire = 2

        elif self.coup_1 == "pierre" and self.coup_2 == "ciseau":
            victoire = 1

        elif self.coup_1 == "feuille" and self.coup_2 == "ciseau": 
            victoire = 2

        elif self.coup_1 == "ciseau" and self.coup_2 == "ciseau":
            victoire = 0

        else:
            victoire = 999 # peu importe du chiffre tant qu'il n'est pas égal à 0,1 ou 2.

        return victoire
    
    def gagnant(self, victoire):

        if victoire == 0:
            winner = "personne"
            print(self.points_1, self.points_2)

        elif victoire == 1:
            winner = "joueur 1"
            self.points_1 += 1
            print(self.points_1, self.points_2)

        elif victoire == 2:
            winner = "joueur 2"
            self.points_2 += 1
            print(self.points_1, self.points_2)

        else:
            winner = "\nErreur dans l'entrée de l'action, veuillez recommencer...\n"
        return winner

    def starting(self):

        for i in range(0,self.manches):
            self.coups()
            v = self.regles()
            w = self.gagnant(v)
        print(self.points_1, self.points_2)


partie = game(input("Entrez le nom du joueur 1\t"), input("Entrer le nom du joueur 2\t"), 1000000)

partie.starting()
