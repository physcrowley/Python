# ===COMMENT UTILISER CE FICHIER===
# Utiliser pythontutor.com pour visualiser les étapes d'exécution
#   un exemple à la fois. Copie le code de l'exemple dans l'éditeur,
#   cliquer Visualiser et cliquer Next en passant à travers chaque
#   étape. Ce qui se passe en mémoire et au console s'affiche sur
#   le côté droit de l'écran 
#   *** choisir l'option "Render all objects on heap" pour voir
#       correctement les objets en mémoire

#EXEMPLE 1 - les variables sont des noms pour référer
# à des objets en mémoire
msg = 42 
print(msg)

#EXEMPLE 2 - les variables pointent à des addresses en mémoire
#  si on assigne une variable à une autre, on ne partage pas sa
#  valeur mais son adresse!
variable = "bleu"
variable2 = variable
variable = "rouge"

#EXEMPLE 3 - les types des variables peuvent changer durant le 
#  programme. C'est flexible, mais c'est aussi une source potentielle
#  d'erreurs de logique
num = "25"
print(num * 2)
num = 25
print(num * 2)
num = 25.0
print(num * 2)

# c'est mieux d'être plus clair avec les noms de variables pour les 
# utiliser correctement ailleurs dans le programme
compte = 25
message = "coucou"
resultat = 12.5

#EXEMPLE 4 - saisir des valeurs avec Python
print("Entrer un nombre :")
valeur = input() # input() donne du texte (str)
entier = int(valeur) # int() convertit en entier (int)
decimal = float(valeur) # float convertit en décimal (float)