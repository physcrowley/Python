# Cet exemple simule ce que vous pourriez avoir dans un
# jeu où il faut suivre et mettre à jour la position de
# plusieurs objets. On ajoute nos objets à une liste
# avec la méthode append(). Dans ce cas, on assigne
# aléatoirement les positions initiales.
# 
# Les positions individuelles sont conservées dans une liste
# de 2 éléments (x et y). On a donc une liste qui contient
# des listes.
# 
# Dans la boucle du jeu, à chaque mise à jour de l'écran,
# il faut normalement calculer les nouvelles positions des
# objets. Ici, pour garder l'exemple simple, on ajoute 10 à
# la valeur x et enlève 5 à la valeur y. Noter qu'il y a DEUX
# références de liste
# -> la 1e est pour la position de l'objet dans la liste
# "positions"
# -> la 2e est pour la valeur x ou y
# 

from random import randint

positions = []

# ajouter des objets (éléments de liste) en leur donnant 
# des positions [x, y] aléatoirement 
for i in range(10):
    positions.append([randint(0,100), randint(0,60)])
    print(positions[i])


print("=================")
# on voit que positions est une liste de listes [x,y]
print(positions) 
print("=================")


# dans la boucle du jeu, changer les positions

for i in range(len(positions)):
    positions[i][0] += 10
    positions[i][1] -= 5
    print(positions[i])


