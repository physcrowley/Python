import pgzrun # pas nécessaire avec Thonny en mode Pygame Zero

WIDTH = 400
HEIGHT = 300

def draw():
    screen.fill("red")
    screen.blit("franco-cite.jpg",(50,50)) # chemin de l'image, position dans la fenêtre


pgzrun.go() # pas nécessaire avec Thonny en mode Pygame Zero

"""
les lignes `import pgzrun` et `pgzrun.go()` sont essentiels pour
tout programme qui est lancé comme un programme Python typique (avec le
bouton "Run" ou avec la commande `python` au console).

Il ne faut pas les avoir dans le code si tu lances le programme avec la
commande `pgzrun` au console ou avec un éditeur comme Thonny en mode
Pygame Zero
"""