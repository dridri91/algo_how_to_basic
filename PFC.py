print("Joueur 1... ")
coup_1 = input("Entrez votre coup :\t")
print("\nJoueur 2...")
coup_2 = input("Entrez votre coup :\t")
victoire = 0

def regles(coup_1,coup_2):
                 # victoire = 0 -> nul
                 # victoire = 1 -> joueur 1 gagne
                 # victoire = 2 -> joueur 2 gagne
    if coup_1 == "pierre" and coup_2 == "feuille":
        victoire = 2

    elif coup_1 == "feuille" and coup_2 == "feuille":
        victoire = 0

    elif coup_1 == "ciseau" and coup_2 == "feuille":
        victoire = 1

    elif coup_1 == "pierre" and coup_2 == "pierre":
        victoire = 0

    elif coup_1 == "feuille" and coup_2 == "pierre":
        victoire = 1

    elif coup_1 == "ciseau" and coup_2 == "pierre":
        victoire = 2

    elif coup_1 == "pierre" and coup_2 == "ciseau":
        victoire = 1

    elif coup_1 == "feuille" and coup_2 == "ciseau": 
        victoire = 2

    elif coup_1 == "ciseau" and coup_2 == "ciseau":
        victoire = 0
    

    return victoire

victoire = regles(coup_1,coup_2)

def gagnant(victoire):
    if victoire == 0:
        winner = "personne"
        return winner

    elif victoire == 1:
        winner = "joueur 1"
        return winner
    
    elif victoire == 2:
        winner = "joueur 2"
        return winner

result_gagnant = gagnant(victoire)

if result_gagnant == "personne":
    print(f"{result_gagnant} ne gagne")
elif result_gagnant == "joueur 1":
    print(f"Le gagnant est donc le {result_gagnant}\n")
else:
    print(f"Le gagnant est donc le {result_gagnant}\n")




    
