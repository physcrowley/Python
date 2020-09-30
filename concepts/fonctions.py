## ===COMMENT UTILISER CE FICHIER===
# Utiliser pythontutor.com pour visualiser les étapes d'exécution
#   un exemple à la fois. Copie le code de l'exemple dans l'éditeur,
#   cliquer Visualiser et cliquer Next en passant à travers chaque
#   étape. Ce qui se passe en mémoire et au console s'affiche sur
#   le côté droit de l'écran 
#   *** choisir l'option "Render all objects on heap" pour voir
#       correctement les objets en mémoire


# C'est quoi une fonction?
#
# Un nom qui représente un ensemble de code, comme une variable représente
# une valeur ou un objet. On peut alors utiliser juste le nom de la
# fonction au lieu d'écrire le code au complet.
# 
# Caractéristiques :
#     -nom suivi par des parenthèses > p. ex. print(), qui les distinguent des
#         variables (juste des noms sans parenthèses).
#     -arguments > valeurs qu'on place entre les parenthèses qui seront utilisées
#         par la fonction
#     -valeur de retour > une fonction peut avoir aucune valeur de retour et simplement
#         faire quelque chose MAIS la plupart des fonctions retournent une valeur au
#         programme utilisant le mot-clé "return".


# EXEMPLE 1 - fonction très simple

def bienvenue():
    print("Allô toi!")


#bienvenue()


# EXEMPLE 2 - fonction avec argument

def affiche_message(msg):
    print(msg)

#affiche_message() # > erreur (manque un argument)
#affiche_message(3)
#affiche_message("coucou")
#age = int(input("C'est quoi ton age?"))
#affiche_message("Bonjour " + str(age))

def affiche_message2(msg = "Bonjour [par défaut]"):
    print(msg)

#affiche_message2() # pas d'erreur > valeur par défaut
#affiche_message2("Bonjour par l'utilisateur")

def affiche_addition(a, b):
    print(a + b)

#affiche_addition(2, 3)
#affiche_addition(10, 20)

# EXEMPLE 3 - fonction avec valeur de retour

def addition(a, b):
    result = a + b
    return result

#r1 = addition(2, 3)
#print(r1)

#print(addition(10, 20))





# EXEMPLE 4 - fonction qui s'appelle lui-même - la récursivité
#
# La RÉCURSIVITÉ est un concept fondamental en génie informatique. 
# C'est quand une fonction s'appelle elle-même pour compléter sa tâche.
# Cet appel doit être conditionnel et il doit avoir une condition logique de
# fin sinon ces auto-appels se répètent infiniment et font planter l'ordinateur! 

def remainder(a, b):
    """ Recursive calculation of the remainder (%, modulo) from integer division """
    
    if a < b: # if a < b, it is the remainder
        return a 
    return remainder(a-b, b) # otherwise, subtract b from a and test again

print(remainder(100, 3))


/*
Restant de 10 / 3 (combien de fois 3 entre dans 10?)
10 - 3 = 7 (1)
7 - 3 = 4 (2)
4 - 3 = 1 (3)
reste 1
*/
