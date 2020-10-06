my_list = [] #les listes sont entourées de crochets
my_list.append(1) # ajouter une valeur à la fin
my_list.append('b')
print(my_list) # affiche la liste complète
print(my_list[0]) # affiche le premier élément avec l'indice 0
print(my_list[-1]) # affiche le dernier élément
print(len(my_list)) # la longueur de la liste

for i in range(len(my_list)): # range(len(my_list)) > range(2) > 0,1 
    my_list[i] *= 2 # je peux modifier les éléments de la liste un par un SUR PLACE
    print(my_list[i])

# il y a une boucle spécial pour OBSERVER SANS MODIFIER les éléments d'une liste
for element in my_list:
    element *= 2
    print(element)

print(my_list[0])

    

