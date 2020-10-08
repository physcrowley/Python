my_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

index = my_string.find("Z") # donne l'adresse / l'indice de la lettre Z
index = my_string.find("z") # pas là > retourne -1 comme index

lettre_Z = my_string[25] # ou my_string[-11]
alphabet = my_string[:25] # ou my_string[0:25] 
nombres = my_string[26:] # ou my_string[26:len(my_string)] ou my_string[26:35]

chaque_deuxieme = my_string[0:35:2] # ou my_string[::2]
# le 3e argument indique les bonds

my_string.find("Z")