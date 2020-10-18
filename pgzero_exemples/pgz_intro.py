"""
Cette version est pour un lancement normal... y inclut sur Repl.it en mode Pygame.
Les lignes `import pgzrun` et `pgzrun.go()` sont essentiels dans ce cas.

Pour un lancement avec Thonny en mode Pygame Zero
ou avec la commande `pgzrun` au console (au lieu de `python`), il faut supprimer
la première et la dernière ligne de l'exemple.
"""

import pgzrun # pas nécessaire avec Thonny en mode Pygame Zero

WIDTH = 400
HEIGHT = 300

def draw():
    screen.fill("red")
    screen.blit("franco-cite.jpg",(50,50)) # chemin de l'image, position dans la fenêtre


pgzrun.go() # pas nécessaire avec Thonny en mode Pygame Zero