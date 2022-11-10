import random
import os

xdg = 'start' if os.name=='nt' else 'xdg-open'

class Game:
    def __init__(self):
        self.number = -1
        while self.number <1:
            try :
                self.number = int(input('En combien de points voulez vous jouer ?'))
            except:
                print('Mauvaise saisie')
                
        self.j1 = Joueur(input(
            'Quel est le nom du premier joueur (entrer bot pour un bot) : \n'))
        self.j2 = Joueur(input(
            'Quel est le name du premier joueur (entrer bot pour un bot) : \n'))
        print(f"""Bienvenue dans ce jeu de pierre papier ciseau.\n
               Cette partie se fait en {self.number} points gagnants.\n""")

    def manche(self):
        a = self.j1.play()
        b = self.j2.play()
        player_winner = self.winner(a, b)
        if player_winner:
            player_winner.victory()
        else:
            print('pas de gagnant pour cette manche\n')

    def prompt_scoreboard(self):
        self.j1.score()
        self.j2.score()

    def  winner(self, play1, play2):
        play = ['pierre', 'papier', 'ciseau']
        return [None, self.j1, self.j2][play.index(play1)-play.index(play2)]

    def start(self):
        while self.j1.point < self.number and self.j2.point < self.number:    
            self.manche()
            self.prompt_scoreboard()

        if self.j1.point+self.j2.point == self.number:
            os.system(xdg + ' https://www.youtube.com/watch?v=dQw4w9WgXcQ')

class Joueur:
    def __init__(self, name):
        self.name = name
        self.point = 0
    
    def score(self):
        print('Le joueur '+self.name + ' a ' + str(self.point) +  ' points.')

    def victory(self):
        self.point+=1
        print(self.name + ' a remporté cette manche !\n')

    def play(self):
        if self.name == 'bot':
            action = random.choice(['pierre','papier','ciseau'])
            print('Le bot a choisi '+action+'\n')
        else:
            action = input(f'Que voulez vous jouer {self.name} ? (pierre / papier / ciseau) :\n')
            while action not in ['pierre','papier','ciseau']:
                action = input('Entrez une bonne valeur : ')
        return action    

a = Game()
a.start()
