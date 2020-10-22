import pgzrun
import random

WIDTH = 800
HEIGHT = 600
apple = Actor("cat")
score = 0

def draw():
  screen.clear()
  screen.draw.text("Score: " + str(score), midtop=(WIDTH/2,5), fontsize=40)
  apple.draw()
 
def place_apple():
    apple.x = random.randint(0, WIDTH - apple.width)
    apple.y = random.randint(100, HEIGHT - apple.height)
 
def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        score += 1
        place_apple()
    else:
        score -= 1
    
clock.schedule_interval(place_apple, 1.0)

pgzrun.go()
