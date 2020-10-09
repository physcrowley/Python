
# Quelques exemples de l'utilisation des listes

# Ce fichier est aussi structuré (définitions de fonctions, 
# condition if name = main) pour être utilisé de façon modulaire,
# soit que le fichier puisse être importé dans d'autres projets
# Python pour rendre les fonctions disponibles ailleurs.

def exemple_couleurs():
    couleurs = ["rouge", "bleu", "vert", "jaune"]

    print("quelle est ta couleur préférée?")
    couleur_utilisateur = input()

    if couleur_utilisateur.lower() not in couleurs:
        print("on n'a pas les mêmes goûts")
    else: print("moi aussi")


def exemple_moyenne():
    #demander plein de valeurs
    #ajouter chaque valeur à une liste
    #calculer la somme de toutes les valeurs dans la liste
    #diviser cette somme par la longueur de la liste
    #afficher le résultat

    pass # pass = fait rien > une définition de fonction ne peux pas être vide


# script qui commence
if __name__ == "__main__":
    exemple_couleurs() # tester cette fonction
    exemple_moyenne() # tester cette fonction
