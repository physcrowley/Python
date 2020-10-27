import pgzrun

WIDTH = 300
HEIGHT = 600

#cat = Actor("cat.png")
#cat.pos = (0, HEIGHT/2)
#speed = 1 # nombre de pixels par update()

class cat_object:
    def __init__(self):
        self.sprite = Actor("cat.png")
        self.sprite.pos = (0, HEIGHT/2)
        self.speed = 1

cats = []
for i in range(5):
    cats.append(cat_object())
    cats[i].speed = i
    cats[i].sprite.y = 50 + 120 * i

def draw():
    screen.fill("white")
    for cat in cats:
        cat.sprite.draw()

def update():    
    for cat in cats:
        if (cat.sprite.x < WIDTH):
            cat.sprite.x = cat.sprite.x + cat.speed
        else:
            cat.speed += 1
            cat.sprite.x = 0

pgzrun.go()