# installer pgzero avec la commande au console (cmd.exe):
# python -m pip install pgzero

import pgzrun # **module** pour programmer des jeux

# variables nécessaires pour le module pgzrun
WIDTH = 300
HEIGHT = 300

# méthode principale d'un programme pgzero
def draw():
    screen.fill((55, 0, 0)) # couleurs R, V, B

pgzrun.go()