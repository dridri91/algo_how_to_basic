class game: 
    def __init__(self,j1,j2,nbmanche):
        
        
            self.points_1 = 0
            self.points_2 = 0
            self.j1 = j1
            self.j2 = j2
            self.nbmanche = nbmanche
       
    
    
    def partie(self):       
        self.choice1= input("choisit entre: pierre , feuille , ciseaux  : ")
        self.choice2 = input("choisit entre: pierre , feuille , ciseaux : ")
    
    

    def regle(self):
        if self.choice1 == "pierre" and self.choice2 == "ciseaux":
            self.points_1 +=1

        elif self.choice1 == "feuille" and self.choice2 == "pierre":
            self.points_1 += +1

        elif self.choice1 == "ciseaux" and self.choice2 == "feuille":
            self.points_1 += +1

        elif self.choice2 == "pierre" and self.choice1 == "ciseaux":
            self.points_2 += +1

        elif self.choice2 == "feuille" and self.choice1 == "pierre":
            self.points_2 += +1

        elif self.choice2 == "ciseaux" and self.choice1 == "feuille":
            self.points_2 += +1
        

        


    def victoire(self):
        
        if self.points_1 > self.points_2:
            print("joueur1 gagne ! ")
            print(self.points_1, "points !")

        elif self.points_1 == self.points_2:
            print("égalité !")
            print(0, "point")


        else:
            print("joueur2 gagne !")
            print(self.points_2, "points !")

            

Partie1 = game("adrien","Paul",3)
for nbmanche in range(1,Partie1.nbmanche + 1):
    Partie1.partie()
    Partie1.regle()
Partie1.victoire()





