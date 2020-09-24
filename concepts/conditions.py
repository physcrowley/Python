""" CONSIGNES
Copier-coller un exemple à la fois dans votre éditeur de Python pour
voir ce qui se passe.
Inclure les commentaires devant l'exemple : ils suggèrent souvent quoi 
regarder ou quoi modifier pour comprendre l'exemple.
"""

# Les CONDITIONS indiquent à python quelle partie du code il doit
# exécuter selon si quelque chose est vraie (True) ou fausse (False).
# 
# La structure d'une condition est la suivante :
# 
# <déclarations avant la condition>
#
# <condition> :
#    <déclarations à faire>         | Ces lignes s'appellent
#    <seulement si la condition>    | un BLOC de code.
#    <est vrai>                     | Elles doivent être indentées
#
# <déclarations après la condition>
# 

# EXEMPLE 1 - gérer l'affichage d'un message
print("début, exemple 1")
valeur = 12 # changer le nombre à plus que 10 pour voir la différence

if valeur > 10 : #condition
    print("message conditionnel") # seulement si la condition est vraie

print("fin, exemple 1\n")


# mot-clé IF
# Pour signaler à Python que la déclaration est une condition, 
# il faut 
#   ... commencer la ligne avec le mot "if"
#   ... terminer la ligne avec un deux points ":"
#
# La condition elle-même utilise les opérateurs de logique qu'on
# a déjà vus.
# 
# Pour dire à Python quelles déclarations sont conditionnelles,
# il faut
#   ... les placer immédiatement après la déclaration "if ... :""
#   ... les décaler par une tabulation vers la droite
#
# Dès qu'une ligne n'a plus cette indentation vers la droite, la
# déclaration n'est plus dans le bloc conditionnel et sera exécutée
# peu importe la condition.


# EXEMPLE 2 - CONDITIONS SUCCESSIVES (les deux seront évaluées)
nom = "JAVA"  # changer ces valeurs pour rendre les conditions
age = 16        # vraies ou fausses et voir ce qui se passe

print("début, exemple 2")
print(nom, age)
if nom.lower() == "java" : # rappel - le .lower() simplifie la comparaison de textes
    print("c'est pour l'année prochaine, en ics4u")
if age > 18 :
    print("vous êtes majeur")
print("fin, exemple 2\n")


# mot-clés ELIF et ELSE
# Dans l'exemple précédant, même si la première condition IF est fausse,
# la deuxième condition IF sera évaluée.
# Parfois, on veut une CONDITION EXCLUSIVE, où seulement un bloc de code
# peut être exécuté. On utilise les mot-clés "else" et "elif" (contraction
# de "else if") pour analyser les cas et choisir le bloc qui convient.
#
# La structure générale est :
# if <condition> :
#   <si la condition est vraie, faire ceci>
#
# elif <2e condition> :
#   <sinon, si la 2e condition est vraie, faire ceci>
# <on peut enchaîner le nombre d'elif qu'on veut>
#
# else :
#   <si le reste est faux, alors faire ceci>


# EXEMPLE 3 - conditions exclusives (seulement un bloc sera évalué)
print("Quelle est ta couleure préférée?")

couleur = input().lower()

print(couleur, end = "... ")

if couleur == "bleu" :
    print("moi aussi")
elif couleur == "vert" :
    print("c'est joli")
elif couleur == "rouge" :
    print("c'est très vif!")
else:
    print("ah oui, bien sûr")

print("fin, exemple 3\n")
