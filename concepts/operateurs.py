import math     # pour aller au-delà de + - * /
    # c'est une bonne pratique d'importer tous les modules externes
    # au début du fichier pour rendre les outils importés disponibles
    # à tout le programme

# OPÉRATEURS MATHÉMATIQUES -> CALCULS
# + - / * 
# // (division entière) 
# % (modulo - donne le restant d'une division)
# PEDMAS : () -->  * / // %  -->  + - 
print("======CALCULS=======")
print("3 + 1 =", 3 + 1)
print("27 / 5 =", 27 / 5)
print("27 // 5 =", 27 // 5)
print("27 % 5 =", 27 % 5)
# utilise la module math que nous avons importés
print("3^6 = ", math.pow(3, 6))
print("sin(30 degrés) =", math.sin( math.radians(30) ))

# OPÉRATEURS LOGIQUES -> COMPARAISONS
# > < >= <= 
# != (pas égale) 
# == (égale) 
#    -> a = 2 (= assigne une valeur à une variable)
#    -> a == 2 (== compare les valeurs a et 2 pour tester leur égalité)
# and (True and True -> True, les autres combinaisons -> False) 
# or (un seul True -> True, False or False -> False) 
# not (opposé: not True -> False, not False -> True)
# ORDRE DES OPÉRATIONS : () --> < > <= >= == != --> not --> and --> or

print("=====COMPARAISONS=====")
genre = "mâle"
age = 17
print(genre == "femelle" or age < 25)
print(genre == "femelle" and age < 25)
print(not(genre == "femelle") and age < 25)
print(genre != "femelle" or age < 25)

# attend avant d'afficher le reste de la sortie
print("tape enter pour voir plus")
input()

# QUELQUES MÉTHODES DE MANIPULATION DE TEXTE

print("========TEXTE========")

# CONCATENER deux textes
# utiliser l'opérateur + pour joindre du texte
str1 = "David"
str2 = "Crowley"
print(str1 + str2)
print(str1 + " " + str2)

# print() peut prendre un ou plusieurs ARGUMENTS
# Chaque argument est séparé par une virgule quand on appelle la fonction
# print.
# Chaque argument est automatiquement converti en texte et ils sont tous
# séparés par un espace (" ")
print(str1, str2) 
    # deux arguments, automatiquement séparés par des espaces au console
print(str1 + str(25) +str(True) + str(-3.27)) 
    # ici on a un seul argument > une longue chaîne de texte de divers
    # morceaux convertis (avec str()) et concatenés (collés avec +) manuellement 
print(str1, 25, True, -3.27) 
    # ici on a plusieurs paramètres, convertis en texte et séparés automatiquement


# Les PARAMÈTRES NOMMÉS de print() -> sep et end
# Changer le comportement par défaut de print() en changeant les valeurs de
# ces deux variables
#   * le séparateur est la variable sep (= " ", espace, par défaut)
#   * la fin de ligne est la variable end (= "\n", retour de ligne, par défaut)
print("-- avec un séparateur = '-'")
print(str1, str2, sep = "-")
print("-- avec un séparateur = '\\n'")
print(str1, str2, sep = "\n") # \n est le caractère de retour de ligne
print("-- avec deux print() et un fin de ligne = ' '")
print(str1, end = " ") # utilise un espace à la fin au lieu d'un retour de ligne
print(str2)

# modifier la case du texte avec des MÉTHODES
# .lower() -> retourne une chaîne en minuscules
# .upper() -> retourne une chaîne en majuscules
# les méthodes sont appliquées sur des objets. Ici, ce sont des chaînes de texte
# Par exemple: "crier".upper() -> "CRIER"
print("-- changer la case")
print("crier".upper())

print("-- Comparer les chaînes de texte avec différentes cases")
str_maj = "ICS3U"
str_min = "ics3u"
str_mix = "Ics3U"

print(str_maj == str_min)
print(str_maj.lower() == str_min)
print(str_maj ==str_min.upper())
print(str_maj == str_min.upper() == str_mix.upper())

print("Devine ma couleur préférée.")
couleur = input()
print("ton choix est...", couleur.lower() == "bleu")
    # cette méthode évite qu'on ait à vérifier toutes les combinaisons de
    # cases possibles pour la bonne réponse de "bLeU"