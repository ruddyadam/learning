import pygame

display_width = 800
display_height = 600
FPS = 30
ellipse_width = 40
ellipse_height = 40

white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)
yellow = (255,255,0)

x = 100
dx = 3
y = 100
dy = 3

#speed = dx = dy = 3

screen = pygame.display.set_mode((display_width,display_height))
#pygame.mixer.init()
#pygame.mixer.music.load('Future City Records - FCR Compilation Vol. X - 01 Arwelone - Everlasting Journey.ogg')
#pygame.mixer.music.play()
animation_timer = pygame.time.Clock()

#while pygame.mixer.get_busy():
#   pygame.time.Clock().tick(10)

endProgram = False
pygame.mouse.set_pos(display_width/2,display_height/2)

if dx >= 0:
    right = True
    left = False
else:
    left = True
    right = False
if dy >= 0:
    down = True
    up = False
else:
    up = True
    down = False

#counter = 0
while not endProgram:


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            endProgram = True

    pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed() == (False, False, True):
        #makes center of ball snap to cursor
        x = pygame.mouse.get_pos()[0] - ellipse_width/2
        y = pygame.mouse.get_pos()[1] - ellipse_height/2

    elif pygame.mouse.get_pressed() == (True, False, False):
        #ball will follow cursor
        if x + ellipse_width/2 < pos[0]:
            x += dx
            right = True
            left = False

        elif x + ellipse_width/2 > pos[0]:
            x -= dx
            left = True
            right = False

        if y + ellipse_height/2 < pos[1]:
            y += dy
            down = True
            up = False

        if y + ellipse_height/2 > pos[1]:
            y -= dy
            up = True
            down = False

    else:       #if mouse button released, do the following
        #makes ball keep going in the direction it was just going.  This may end up being only up, down, left, or right
        if right == True:
            x += dx
        else:
            x -= dx

        if up == True:
            y -= dy
        else:
            y += dy

        #bounces ball off the walls # this is problematical as I need to change up down lkeft right booleans
        if y < 0 or y > display_height - ellipse_height:
            dy *= -1

        if x < 0 or x > display_width - ellipse_width:
            dx *= -1

    print (up,down,left,right)
    #counter += 1
    #print(counter)
    screen.fill(blue)

    pygame.draw.ellipse(screen, (white), (x,y,ellipse_width,ellipse_height))

    animation_timer.tick(FPS)

    pygame.display.update()