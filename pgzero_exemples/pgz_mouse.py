import pgzrun

WIDTH = 600
HEIGHT = 300

cat = Actor("cat.png")
cat.midleft = (WIDTH, HEIGHT/2)
speed = 1 # nombre de pixels par update

def draw():
    screen.fill("white")
    cat.draw()

def on_mouse_move(pos):
    cat.pos = pos

pgzrun.go()