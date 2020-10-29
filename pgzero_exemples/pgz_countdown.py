import pgzrun

set_time = 30 # une variable de référence que tu peux modifier
current_time = float(set_time) # le temps qu'il reste, en décimal

def count_down():
    global current_time
    current_time -= 1.0 # diminue de 1


def draw():
    screen.clear()
    screen.draw.text(str(current_time) + " s", (0,0))


clock.schedule_interval(count_down, 1.0) # appelle la fonction count_down chaque seconde


pgzrun.go()