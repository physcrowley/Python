import pgzrun

# boucle du jeu > événements -> update -> draw


WIDTH = 600
HEIGHT = 300

dog = Actor("dog.png")
dog.pos = (WIDTH/2, HEIGHT/2)

def draw():
    screen.fill("white")
    dog.draw()

def on_mouse_move(pos):
    print("Position: " + str(pos))
    dog.angle = dog.angle_to(pos)
    print("Angle: " + str(round(dog.angle)))

pgzrun.go()