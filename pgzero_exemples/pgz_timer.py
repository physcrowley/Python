import pgzrun

WIDTH = 200
HEIGHT = 200

elapsed_time = 0

def draw():
    screen.clear()
    message = str(elapsed_time) + " seconds"
    screen.draw.text(message, midtop = (WIDTH/2, HEIGHT/2 - 5))
    
def get_time(): # action we want to schedule has to be defined in a function
    global elapsed_time
    elapsed_time +=1
    
# calls get_time() function every second
clock.schedule_interval(get_time, 1.0) 

pgzrun.go()
