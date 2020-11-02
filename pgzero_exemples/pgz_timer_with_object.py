import pgzrun
import game_time as gt

WIDTH = 200
HEIGHT = 200

t = gt.game_time() # t refers to a game_time object -> we can now access t
            # within our other functions

def draw():
    screen.clear()
    message = str(t.elapsed_time) + " seconds"
    screen.draw.text(message, midtop = (WIDTH/2, HEIGHT/2 - 5))

# calls t.set_time() function every second
clock.schedule_interval(t.set_time, 1.0)

pgzrun.go()