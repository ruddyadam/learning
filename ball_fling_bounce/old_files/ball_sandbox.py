import pygame
import random
from pygame.locals import *
import math

#make them react to being hit by bouncing in the opposite direction of being hit...
#at teh speed they were being hit
#with a decaying speed
#and then bounce off each other as well
#create config file usage

#when the ball touches a dot, it turns yellow.  this decays

#collision point to circle


display_width = 800
display_height = 600
fps = 30


dot_width = 2
dot_height = 2
number_of_dots = 100

ball_is_a_circle = True
ball_radius = 20
ball_width = 40
ball_height = 40
ball_start_pos = (display_width / 2, display_height / 2)

white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)
yellow = (255,255,0)

mouse_visible = False
pygame.init()
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Flat Circle "moving"')
clock = pygame.time.Clock()


class Dot():

    def __init__(self):
        self.position_x = random.randint(2, (display_width -2))
        self.position_y = random.randint(2, (display_height -2))
        self.direction_x = 0
        self.direction_y = 0

    def draw_dot(self):
        pygame.draw.rect(screen, yellow, (self.position_x, self.position_y, dot_width, dot_height),0)

    def update_position(self):


    def coordinates(self):
        return ((self.position_x, self.position_y))

class Ball():

    def __init__(self):
        pass

    def draw_ball(self): #ball currently locked to cursor
        if ball_is_a_circle == True:
            self.pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, white, (self.pos[0], self.pos[1]), ball_radius, 0)
        else:
            pygame.draw.rect(screen, white, (self.pos[0], self.pos[1], ball_width, ball_height), 0)

def ball_dot_collision_test(dot_object):

    ball_pos = pygame.mouse.get_pos()
    dot_pos = (dot_object.position_x, dot_object.position_y)

    # use pythagorean theorem to get distance from the dot to the ball
    distance_x = float(dot_pos[0] - ball_pos[0])
    distance_y = float(dot_pos[1] - ball_pos[1])

    distance = math.sqrt((distance_x*distance_x)+ (distance_y * distance_y))

    #if the dot is less than or equal to the ball's radius, then collision occurred and return True
    if distance <= ball_radius:
        return True
    else:
        return False

def move_dot(dot_object):

    ball_speed = pygame.mouse.get_rel()
    print(ball_speed)
    ball_pos = pygame.mouse.get_pos()
    dot_pos = (dot_object.position_x, dot_object.position_y)

    # use pythagorean theorem to get distance from the dot to the ball
    distance_x = dot_pos[0] - ball_pos[0]
    distance_y = dot_pos[1] - ball_pos[1]

    if dot_pos[0] < ball_pos[0]:
        dot_object.position_x -= ball_speed[0]
    elif dot_pos[0] > ball_pos[0]:
        dot_object.position_x += ball_speed[0]
    else:
        pass

    if dot_pos[1] < ball_pos[1]:
        dot_object.position_y -= ball_speed[1]
    elif dot_pos[1] > ball_pos[1]:
        dot_object.position_y += ball_speed[1]
    else:
        pass

#mouse button down to spawn a ball locked to the cursor.
#mouse button up to release the ball at the speed and direction of the mouse
#decay the ball speed

#creates a list whose contents is d1, d2, d3... dn, where n is number_of_dots
dot_list = []
for i in range(0, number_of_dots):
    dot_list.append('d'+str(i))

#creates a list of objects from dot_list
dot_objects = [Dot() for dot_item in dot_list]

#instantiates ball
ball = Ball()

pygame.mouse.set_visible(mouse_visible)
quitGame = False
pygame.mouse.set_pos(ball_start_pos)

while not quitGame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True

        #print(event)  #prints key/mouse events in the console

    screen.fill(black)

    for dot in dot_objects:

        if ball_dot_collision_test(dot) == True:
            # move dot away from center of ball with trajectory through dot
            move_dot(dot)
            #print(dot.direction_x,dot.direction_y)
            # with speed of relative distance of ball
        #dot.update_position()
        dot.draw_dot()




    ball.draw_ball()

    clock.tick(60)
    pygame.display.update()

#pygame.quit()
#quit()

