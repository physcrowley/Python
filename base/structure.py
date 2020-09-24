# le "#" indique que le reste de la ligne est un COMMENTAIRE
# qui est lisible par les humains mais ignoré par l'ordinateur 
# quand il interprète et exécute le programme


# chaque DÉCLARATION est sur une seule ligne

print("Bonjour le monde!")
print("Comment ça va") # les déclarations sont lues et réalisées
                       # dans l'ordre qu'ils se trouvent dans le
                       # script (le fichier .py)


# un BLOC de code...
#   1- vient après une déclaration qui finit par ":"
#   2- doit être indenté (décalé par des espaces vers la droite)
# Il y a plusieurs types de blocs que nous étudierons, mais
# les 2 blocs dans l'exemple sont un "if" et un "else"

if 1 > 2:
    print("woohoo")
else:
    print("beuh")


# code qui s'exécute après la structure if-else
print("fin")