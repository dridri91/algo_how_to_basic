import random

class Partie:
    def __init__(self):
        self.nombre = 3
        self.j1 = Joueur(input('Quel est le nom du premier joueur (entrer bot pour un bot) : \n'))
        self.j2 = Joueur(input('Quel est le nom du premier joueur (entrer bot pour un bot) : \n'))
        print(f'Bienvenue dans ce jeu de pierre papier ciseau.\nCette partie se fait en {self.nombre} points gagnants.\n')
        

    def manche(self):
        a = self.j1.jouer()
        b = self.j2.jouer()
        gagnant = self.winner(a,b)
        if gagnant == "egalite":
            print('pas de gagnant pour cette manche\n')
        else:
            gagnant.victoire()

    def afficher_score(self):
        self.j1.score()
        self.j2.score()

    def  winner(self, play1, play2):
        possiblilities = ['pierre', 'papier', 'ciseau']
    
        #return ['egalite',self.joueur1,self.joueur2][possiblilities.index(play1)-possiblilities.index(play2)%3]
        return ['egalite',self.j1,self.j2][possiblilities.index(play1)-possiblilities.index(play2)%3]

    def lancement(self):
        while self.j1.point < 3 and self.j2.point < 3:    
            self.manche()
            self.afficher_score()


    

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.point = 0
    
    def score(self):
        print('Le joueur '+self.nom + ' a ' + str(self.point) +  ' points.')

    def victoire(self):
        self.point+=1
        print(self.nom + ' a remporté cette manche !\n')

    def jouer(self):
        if self.nom == 'bot':
            action = random.choice(['pierre','papier','ciseau'])
            print('Le bot a choisi '+action+'\n')
        else:
            action = input(f'Que voulez vous jouer {self.nom} ? (pierre / papier / ciseau) :\n')
        return action    





a = Partie()

a.lancement()
