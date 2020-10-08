my_string = "abcdefghij,123456"

#num = int(my_string) # erreur parce que my_string ne représente pas un nombre entier

print( len(my_string) ) # donne le nombre de charactères

substrings = my_string.split(",")
print(substrings)


print("entrer une coordonnée séparé par des virgules")
s_coord = input()
coords = s_coord.split(",")
for i in range(2):
    coords[i] = int(coords[i])