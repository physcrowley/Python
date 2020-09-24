""" CONSIGNES
Copier-coller un exemple à la fois dans votre éditeur de Python pour
voir ce qui se passe.
Inclure les commentaires devant l'exemple : ils suggèrent souvent quoi 
regarder ou quoi modifier pour comprendre l'exemple.
"""
# les """ ... """ désignent un commentaire sur plusieurs lignes
# tout ce qui est entre les """ est ignoré par Python


# Les conditions nous permettent de capter les erreurs avant que
# notre programme plante.
# Un cas important est la vérification que l'utilisateur a entré
# une information valide.

# EXEMPLE 1 - choix
menu =  "Entrer la valeur du choix qui te convient :\n"
menu += "1- ...\n"
menu += "2- ...\n"
menu += "3- ...\n"
print(menu)

choix = input() # je le garde en texte (str) par exprès

if choix == "1" : # la valeur de comparaison doit être du même type, str
    print(choix, "J'exécute l'option 1")
elif choix == "2" :
    print(choix, "J'exécute l'option 2")
elif choix == "3" :
    print(choix, "J'exécute l'option 3")
else : # on utilise l'else (si le reste est faux) pour capter les erreurs
    print(choix, "Désolé, je n'ai pas compris ton choix.")

print("fin, exemple1\n")


# Dans l'exemple précédant, tout ce qui n'est pas 1, 2 ou 3 - même des 
# choses qui ne sont pas des nombres, comme "na na na na" - produit
# une erreur captée par le bloc "else" parce qu'on a traité tout comme
# du texte et le texte peut être n'importe quoi.
#
# Mais si on veut des input() qui sont numériques, on doit les convertir
# et si l'utilisateur a inscrit quelque chose de non numérique, python va
# planter au int(input()) ou au float(input()).


# EXEMPLE 2 - erreur de conversion de nombre
print("début, exemple2")
print("Inscrit ton âge")

fake_input = "soixante dix"

age = int(fake_input)   # le programme plantera ici
                        # et on ne se rend même pas aux conditions

if 0 < age < 18 :
    print("mineur")
elif 18 < age < 30 :
    print("adulte")
elif 30 < age < 60 :
    print("adulte 'mature'")
elif age >= 60:
    print("adulte senior")
else:
    print("L'âge doit être plus grand que 0.")

print("fin, exemple 2\n")


# structure TRY - EXCEPT
#
# On utilise un bloc "try" quand c'est possible que le code produise
# une erreur chez Python qui fait planter le programme - on appelle ces 
# erreurs des EXCEPTIONS. Si aucune erreur n'est générée, alors le code dans 
# le bloc "try" s'exécute. Sinon, au lieu d'afficher l'erreur au console et 
# planter le programme, Python passera au bloc "except" pour faire le code qui
# se trouve là à la place.


# EXEMPLE 3 - capter les erreurs de conversion de nombre
print("début, exemple3")
print("Inscrit ton âge")

fake_input = "soixante dix"

try:
    age = int(fake_input)   # cette ligne produit une exception
                            # et on passe au bloc except 
except:
    print("Il faut que l'age soit un *nombre entier*.")
    age = -1 # age bidon pour continuer et tomber dans le else

if 0 < age < 18 :
    print("mineur")
elif 18 < age < 30 :
    print("adulte")
elif 30 < age < 60 :
    print("adulte 'mature'")
elif age >= 60:
    print("adulte senior")
else:
    print("L'âge doit être plus grand que 0.")

print("fin, exemple 3\n")


# EXEMPLE 4 - l'exemple 3 avec du vrai input
# En réalité, on mettrait la fonction input() dans le bloc try
print("début, exemple4")
print("Inscrit ton âge")

try:
    age = int(input())
except: # si l'input ne peut pas être converti en int
    print("Il faut que l'age soit un nombre entier.")
    age = -1 # age bidon pour continuer et tomber dans le else

if 0 < age < 18 :
    print("mineur")
elif 18 < age < 30 :
    print("adulte")
elif 30 < age < 60 :
    print("adulte 'mature'")
elif age >= 60:
    print("adulte senior")
else:
    print("L'âge doit être plus grand que 0.")

print("fin, exemple 4\n")