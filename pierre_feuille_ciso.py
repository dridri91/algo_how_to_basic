
class Partie:
    def __init__(self,j1, j2, nombre):
        self.joueur1 = j1
        self.joueur2 = j2
        self.nombre = nombre
        self.point_1 = 0
        self.point_2 = 0

    def  winner(self, play1, play2):
        possiblilities = ['pierre', 'papier', 'ciseau']
        return ['egalite',self.joueur1,self.joueur2][possiblilities.index(play1)-possiblilities.index(play2)%3]



    def game(self):
        
        for i in range(self.nombre):
            joueur_actif = self.joueur2 if i%2 else self.joueur1
            print(f"c'est a {joueur_actif} de jouer")


a = Partie('mathis', 'guilian',3)

print(a.winner('pierre','ciseau'))

