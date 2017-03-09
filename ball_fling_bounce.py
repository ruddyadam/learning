# the point of this is to make a flat circle that you can toss around with the mouse and it will bounce off the walls

import pygame
import random

#song that will play
song = 'SIDwave_-_Kohinoor_future_version-SIDwave_-_Kohino.ogg'

#colors
white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)
yellow = (255,255,0)

display_width = 800
display_height = 600
fps = 30

cursor_start_pos = (display_width / 2, display_height / 2)

ball_is_a_circle = False
ball_radius = 20
ball_width = 40
ball_height = 40

pygame.init()
screen = pygame.display.set_mode((display_width,display_height)) #create window
pygame.display.set_caption('Ball Fling and Bounce') #set caption
clock = pygame.time.Clock() #set clock variable for FPS


#plays music
pygame.mixer.init()
pygame.mixer.music.load(song)
pygame.mixer.music.play()

#create circle (ball)
class Ball():

    #position and movement variables
    x = 100
    y = 100
    dx = 2
    dy = 2

    #def __init__(self):


    def draw_ball(self): #ball currently locked to cursor
        if ball_is_a_circle == True:
            pygame.draw.circle(screen, white, (self.x, self.y), ball_radius, 0)
        else:
            pygame.draw.ellipse(screen, white, (self.x, self.y, ball_width, ball_height), 0)

    def update_position(self):
        self.x += self.dx
        self.y += self.dy

    def bounce(self):
        if self.y < 0 or self.y > display_height - ball_height:
            self.dy *= -1

        if self.x < 0 or self.x > display_width - ball_width:
            self.dx *= -1

quitGame = False
pygame.mouse.set_pos(cursor_start_pos)
ball = Ball()  #creates an initial ball

#main loop
while not quitGame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True

        #if pygame.key.get_pressed() == pygame.K_SPACE:
        #    ball.dx, ball_dy = 0

        print(event)  # prints key/mouse events in the console

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()



    # will lock ball to mouse cursor if left click
    if pygame.mouse.get_pressed() == (True, False, False):
        if ball_is_a_circle == False:

            # left-clicking the mouse on the ball locks the ball to the cursor
            ball.x = pygame.mouse.get_pos()[0] - ball_width / 2
            ball.y = pygame.mouse.get_pos()[1] - ball_height / 2

            # moving the mnouse and letting go of the ball gives locks that speed and direction to the ball
            ball.dx, ball.dy = pygame.mouse.get_rel()

        else:
            pass

    #if pygame.mouse.get_pressed() == (False, False, True):
    #    ball = Ball()

    screen.fill(black)
    ball.update_position()


    ball.draw_ball()
    ball.bounce()   #ball will bounce off walls
    clock.tick(60)
    pygame.display.update()


#next step:
#space bar stops the ball

#next step:
#each time you click not on the ball, it creates a new ball
#each ball bounces off the walls and other balls
