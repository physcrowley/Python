###################################
# Les exemples dans ce fichier sont
# définis comme des fonctions qui
# sont appelés seulement à la
# toute fin dans la partie "script"
#
# Changer le nom de la fonction 
# appelée dans le script pour voir
# un exemple différent.
#
# Cette structure de programme
# ressemble plus aux programmes
# typiques en Python
###################################

# Les boucles sont pour répéter des commandes selon une condition.

# on peut s'avoir d'avance le nombre de répétition -> on va utiliser une boucle FOR

# si on ne sait pas combien de fois on doit faire la répétion, on utilise une boucle WHILE


#EXEMPLE 1 - while
# while <condition qui doit être vrai>:
#  <code à répéter, incluant une façon de rendre la condition fausse>

def exemple1():
    menu = "choisir 1, 2 ou 3. Taper autre chose pour sortir"

    choix = "1"
    while (choix == "1" or choix == "2" or choix == "3"):
        print(menu)
        choix = input()
        if choix == "1":
            print("bon choix")
        elif choix == "2":
            print("autre bon choix")
        elif choix == "3":
            print("3e bon choix")
        else:
            print("fin de la boucle")


# EXEMPLE 2 - while(True)
# utile pour des boucles de jeu, ou des menus. Il faut
# inclure le mot-clé BREAK en quelque part : break met fin à la boucle

def exemple2a():
    still_playing = True
    while(still_playing):
        print("playing now... press Enter to continue or q to quit")
        choix = input()
        if choix.lower() == "q":
            break

def exemple2b():
    still_playing = True
    print("new game. lives = 3")
    lives  = 3
    while(still_playing):
        lives -= 1
        print("lost à life. lives =", lives)
        if lives <= 0:
            break


#EXEMPLE3 FOR SIMPLE

def exemple3():
    for n in range(10): #range(10) > (0,1,2,...,9)
        print(n)


#EXEMPLE 4 - FOR
# calcule de factoriel : n! = n * (n-1) * (n-2) *...*1

def exemple4():
    print("enter a whole number whose factorial will be calcalated")
    n = int(input())
    fact = 1
    for i in range(1,n+1): # range(n) > (0,1,2,...,n-1)
                        # range(1,n+1) > (1,2,...,n)
        fact = fact * i
    print("le factoriel de", n, "est", fact)



## SCRIPT POUR APPELER LES FONCTIONS
if __name__ == "__main__": 
    exemple3() 
    #   changer le nom de la fonction pour voir les différents exemples
    #   exemples disponibles : 1, 2a, 2b, 3, 4


## NOTES SUR "if __name__ == "__main__":
# Quand un fichier python est exécuté, l'interpréteur lui assigne le nom "__main__"
# Mais c'est possible que toutes les fonctions que tu as définis soient importées
# pour aider dans un autre fichier python (comme celles définies dans math.py)