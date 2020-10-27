import pgzrun

WIDTH = 800
HEIGHT = 600

ball = Actor("ballon-nike", midbottom=(150, HEIGHT) )

def draw():
    # les choses dessinées en premier sont en-dessous
    
    screen.fill((0,255,0))
    #screen.blit("ballon-nike", center=(WIDTH/2, HEIGHT/2) )
    
    screen.draw.text("Text color", (WIDTH/2, HEIGHT - 50), color="blue")

    ball.draw()
    # les choses dessinés en derniers sont sur le dessus

def update():
    ball.x += 1
    ball.angle -= 1

def on_mouse_down(pos):
    if ball.collidepoint(pos):
        ball.y -= 10

pgzrun.go()