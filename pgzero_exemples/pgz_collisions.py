import pgzrun
import random

WIDTH = 800
HEIGHT = 600


# Créer une liste de chats
cats = []

# Dire comment créer un chat
def make_cat():
    cats.append(Actor("cat.png",(random.randint(0,WIDTH), random.randint(0, HEIGHT))))

# Initiliser la liste de chats
for i in range(10):
    make_cat()

# Créer un chien
dog = Actor("dog.png")

# Tout dessiner
def draw():
    screen.clear()
    for c in cats:
        c.draw()
    dog.draw()

# Vérifier les collisions
def update():
    for c in cats:
        if c.colliderect(dog): # objet1.colliderect(objet2) / objet.collidepoint(pos)
            cats.remove(c) # enlever le chat de la liste
            clock.schedule(make_cat, 1.0) # créer un nouveau chat à un endroit aléatoire
                                          # après un délai d'une seconde

# Le chien suit la souris
def on_mouse_move(pos):
    dog.pos = pos

pgzrun.go()