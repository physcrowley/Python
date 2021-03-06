""" Ce fichier développe un exemple où un objet est utilisé de façon
similaire à ce qu'on pourrait voir en développant un jeu ou une application.
"""

from random import randint

# on utilise ces valeurs souvent alors c'est mieux de définir une variable
# afin de seulement avoir à le changer une fois, ici, et éviter d'oublier
# de le changer en quelque part dans notre programme
WIDTH = 80
HEIGHT = 60

class Runner:
    def __init__(self):
        self.x = randint(0, WIDTH) # position horizontale
        self.y = randint(0, HEIGHT) # position verticale
        self.vx = randint(-WIDTH//10, WIDTH//10) # vitesse horizontale > + est vers la droite
        self.vy = randint(-HEIGHT//10, HEIGHT//10) # vitesse verticale > + est vers le bas
        self.name = "Runner" + str(self.x) + "-" + str(self.y)
    
    def running(self):
        self.x += self.vx
        self.y += self.vy

        # rebondir aux limites
        if self.x >= WIDTH or self.x <= 0 : 
            self.vx = -self.vx
        if self.y >= HEIGHT or self.y <= 0 : 
            self.vy = -self.vy



# notre script de jeu pour tester nos affaires
if __name__ == "__main__":
    
    # ========PRÉPARATION==========

    #liste pour garder nos objets Runner
    runners = []
    for i in range(6):
        runners.append(Runner())
        print(runners[i].name)
    

    # =========JEU============

    version_choice = "0" # version
    while version_choice not in ("1", "2"):
        print("Which version do you want to play? 1- values | 2- diagrams")
        version_choice = input()
        if version_choice not in ("1", "2"):
            print(">> you must choose 1 or 2")
    
    print("====We're playing version " + version_choice + "!!!!====")
    
    
    playing = True
    while playing:
        print("Keep running? Y/N")
        choice = input().lower()

        if choice == "n":
            print("End of game")
            # break  # quitter directement la boucle
            playing = False # modifier la valeur de la condition pour la boucle while
            
        elif choice != "y":
            print(">> you must choose Y or N")
            continue # continue > saute la boucle actuelle, mais part un nouveau cycle
        
        else:
            for r in runners:
                    r.running() # on court!

                    if version_choice == "1": # version 1 > afficher la position en chiffres
                        print(r.name, r.x, r.y)
                    
                    else: # version 2 > visuellement représenter la position horizontale
                        if r.vx == 0 : car = "*" # immobile
                        elif r.vx > 0 : car = ">" # bouge vers la droite
                        else: car = "<" # bouge vers la gauche
                        
                        # Dessiner un mur "|" et placer x fois le nombre d'espaces
                        # avant le caractère qui indique la position.
                        # Avant de placer le mur droit, on doit ajouter des espaces pour
                        # atteindre la pleine largeur, soit un nombre d'espaces égale à
                        # WIDTH moins la position.
                        print("|" + r.x * " " + car + (WIDTH - r.x) * " " + "|")
                    
            
