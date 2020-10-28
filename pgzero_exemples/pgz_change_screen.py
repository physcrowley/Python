import pgzrun
import pgz_timer_with_object as t

WIDTH = 800
HEIGHT = 600

ticks = t.game_time()

click_right = True

def draw_right():
    screen.fill("blue")

def draw_left():
    screen.fill("red")

def on_mouse_down(pos):
    global click_right
    if pos[0] <= WIDTH/2: # côté gauche
        click_right = False
        ticks.elapsed_time = 0 # reset le temps
                               # reset une liste -> ma_liste = [] ou ma_liste.clear()
    else: # côté droit
        click_right = True

def draw():
    if click_right: # côté droit
        draw_right()
    else:           # côté gauche
        draw_left()

    message = str(ticks.elapsed_time) + " seconds"
    screen.draw.text(message, midtop = (WIDTH/2, HEIGHT/2 - 5))


clock.schedule_interval(ticks.set_time, 1.0)

pgzrun.go()