import pgzrun

working = False
box = Rect(50, 50, 50, 50)

def draw():
    screen.clear()
    if working:
        screen.fill("green")
    else:
        screen.fill("red")
    screen.draw.filled_rect(box, (0,0,0) )


def on_mouse_move(pos):
    global working
    if box.collidepoint(pos) and keyboard.s:
        working = True
    else:
        working = False


pgzrun.go()
