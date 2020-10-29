#exemple incomplet pour montrer quelques idées

import pgzrun

set_time = 30 # une variable de référence que tu peux modifier
current_time = float(set_time) # le temps qu'il reste, en décimal
level = 1

def count_down():
    global current_time
    current_time -= 1.0 # diminue de 1

def draw_level(level): # aucune logique de jeu, juste des objets à dessiner
    if level == 1:
        # commandes pour dessiner la scène
    if level == 2:
        # commandes pour dessiner la scène

def choose_level(time, lives, level):  # quel scène dessiner
    if time == 0 and lives > 0:
        draw_level(level + 1)
    elif time == 0:
        draw_game_over()
    else:
        draw(level)

def draw(): # dessiner -> envoyer à pgzrun
    screen.clear()
    choose_level(level)


clock.schedule_interval(count_down, 1.0) # appelle la fonction count_down chaque seconde


pgzrun.go()