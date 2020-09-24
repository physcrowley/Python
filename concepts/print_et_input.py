print("C'est quoi ton nom?")
# print est un exemple d'une fonction
# chaque fonction :
#   1 -a un nom - print
#   2- peut prendre des paramètres (de l'information) -> vont entre les ()
#       ... si ça ne prend rien les parenthèses restent vident
#       ... print prend le texte à afficher ("C'est quoi ton nom")
#   3- peuvent retourner une valeur
#       ... ici print() fait un processus et ne retourne aucune valeur

nom = input()
# input est un exemple d'une fonction
#   1- le nom est input
#   2- il ne prend aucun paramètre - () vides
#   3- il va retourner le texte (str) tapé au console

print("Bienvenue", nom)
#   print peut aussi prendre une liste de paramètres
#     séparés par des virgules. Il évalue chaque paramètre
#     comme du texte et l'affiche sur la même ligne au console


# === 💡 input() DONNE TOUJOURS DU TEXTE ==========================
#   les fonctions int() et float() sont utilisées quand on a besoin
#   d'utiliser les valeurs reçues d'input() comme nombres

print("Inscrire un nombre entier")

entier = input() # retourne du texte (type = str)
print(type(entier), entier) # type() indique le type de la valeur, confirmant str
print("Le double de la valeur dans 'entier' est", entier * 2) # résultat inattendu

entier = int(entier) # convertir la valeur en int
print(type(entier), entier)
print("Le double de la valeur dans 'entier' est", entier * 2) # résultat attendu

# comme on utilise les fonctions habituellement :
print("Inscrire une valeur décimale")
decimal = float(input())
print(type(decimal), decimal)

