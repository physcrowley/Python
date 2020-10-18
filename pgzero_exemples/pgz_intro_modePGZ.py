"""
cette version est pour un lancement avec Thonny en mode Pygame Zero
ou avec la commande `pgzrun` au console (au lieu de `python`)

les deux lignes effacées avec des commentaires doivent être ajoutées
pour un lancement normal... y inclut sur Repl.it en mode Pygame.
"""

#import pgzrun # ajouter cette ligne pour le lancer normalement

WIDTH = 400
HEIGHT = 300

def draw():
    screen.fill("red")
    screen.blit("franco-cite.jpg",(50,50)) # chemin de l'image, position dans la fenêtre

#pgzrun.go() # ajouter cette ligne pour le lancer normalement