import pgzrun

WIDTH = 200
HEIGHT = 200

"""
Small object to hold the time variable and time change function

Using objects allows us to access and change game variables within
other game functions without declaring global variables
"""
class game_time:
    def __init__(self):
        self.elapsed_time = 0 # elapsed_time variable starts at 0
    
    def set_time(self):  # called at an interval of 1.0 seconds by the clock
        self.elapsed_time += 1

t = game_time() # t refers to a game_time object -> we can now access t
                # within our other functions

def draw():
    screen.clear()
    message = str(t.elapsed_time) + " seconds"
    screen.draw.text(message, midtop = (WIDTH/2, HEIGHT/2 - 5))
    
# calls t.set_time() function every second
clock.schedule_interval(t.set_time, 1.0)

pgzrun.go()