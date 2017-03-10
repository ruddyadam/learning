# the point of this is to make a flat circle that you can toss around with the mouse and it will bounce off the walls

import pygame
import random
import math

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

ball_is_a_circle = True
ball_radius = 20
ball_width = 40
ball_height = 40

dot_is_a_circle = False
dot_radius = 1
dot_width = 2
dot_height = 2
number_of_dots = 500

pygame.init()
screen = pygame.display.set_mode((display_width,display_height)) #create window
pygame.display.set_caption('Ball Fling and Bounce') #set caption
clock = pygame.time.Clock() #set clock variable for FPS

#plays music
pygame.mixer.init()
pygame.mixer.music.load(song)
pygame.mixer.music.play()


def distance_to_closest_dot_point(test_tuple):
    dist_x = ball.x - test_tuple[0]
    dist_y = ball.y - test_tuple[1]
    distance = math.sqrt((dist_x * dist_x) + (dist_y * dist_y))
    return distance

#create circle (ball)
class Ball():

    #ball position and movement variables
    x = 100
    y = 100
    dx = 10
    dy = 10
    speed_decay_counter = 0
    speed_decay_rate = fps

    #def __init__(self):


    def draw_ball(self):
        if ball_is_a_circle == True:
            pygame.draw.circle(screen, white, (self.x, self.y), ball_radius, 0)
        else:
            pygame.draw.ellipse(screen, white, (self.x, self.y, ball_width, ball_height), 0)

    def update_position(self):
        self.x += self.dx
        self.y += self.dy

    def bounce(self):
        if ball_is_a_circle == True:
            if self.y - ball_radius < 0 or self.y + ball_radius > display_height:
                self.dy *= -1

            if self.x - ball_radius < 0 or self.x + ball_radius > display_width:
                self.dx *= -1
        else:
            if self.y < 0 or self.y > display_height - ball_height:
                self.dy *= -1

            if self.x < 0 or self.x > display_width - ball_width:
                self.dx *= -1
    def speed_decay(self):
        if not self.dx == 0 or not self.dy == 0:
            if self.speed_decay_counter < self.speed_decay_rate:
                self.speed_decay_counter += 1
            else:                   #bring the dx and dy closer to 0
                if self.dx < 0:
                    self.dx += 1
                elif self.dx > 0:
                    self.dx -= 1

                if self.dy < 0:
                    self.dy += 1
                elif self.dy > 0:
                    self.dy -= 1

                self.speed_decay_counter = 0

class Dot():

    x = 0   #position x
    y = 0   #position y
    dx = 0  #speed and direction x
    dy = 0  #speed and direction y
    speed_decay_counter = 0 #keeps track of cycles to know when to slow by 1 unit
    speed_decay_rate = fps  #sets the amount of cycles where speed will decay by 1
    #amount_to_decay_by = 1 #TODO: fix so amount can be any amount, but must reach 0 in decay method below


    def __init__(self):
        self.x = random.randint(2, (display_width - 2)) #to spawn each object in a random location
        self.y = random.randint(2, (display_height - 2))

    def draw_dot(self):
        if dot_is_a_circle == True: #
            pygame.draw.circle(screen, white, (self.x, self.y), dot_radius, 0)
        else:
            pygame.draw.rect(screen, white, (self.x, self.y, dot_width, dot_height), 0)

    def update_position(self):
        self.x += self.dx
        self.y += self.dy

    def bounce(self):
        if self.y < 0 or self.y > display_height - dot_height:
            self.dy *= -1

        if self.x < 0 or self.x > display_width - dot_width:
            self.dx *= -1

    def dot_is_rect_collide(self): #rectangle/rectlangle
        pass

    # closest edge of dot to ball
    def closest_dot_edge(self):
        test_x = self.x
        test_y = self.y

        if ball.x < self.x:
            test_x = self.x                 # dot left edge is closest
        elif ball.x > self.x + dot_width:
            test_x = self.x + dot_width     # dot right edge is closest

        if ball.y < self.y:
            test_y = self.y                 # top edge is closest
        elif ball.y > self.y + dot_height:
            test_y = self.y + dot_height    # bottom edge is closest

        test_tuple = (test_x, test_y)
        return test_tuple

    def collision(self):
        if distance_to_closest_dot_point(self.closest_dot_edge()) <= ball_radius:
            return True
        else:
            return False

    #TODO: set_deflect_direction() needs to be fixed
    # the speed of the deflection is dependent on the radius of the circle
    # dx, dy is currently not only direction, but speed.
    # Fix so direction and speed are separate, direction to be slope, and speed on collision
    # to be double ball relative speed.  This should also mean fixing speed and decay in general

    def set_deflect_direction(self):
        self.dx = self.x - ball.x # + ball x relative
        self.dy = self.y - ball.y # + ball y relative

    def speed_decay(self):
        if not self.dx == 0 or not self.dy == 0:
            if self.speed_decay_counter < self.speed_decay_rate:
                self.speed_decay_counter += 1
            else:                   #bring the dx and dy closer to 0
                if self.dx < 0:
                    self.dx += 1
                elif self.dx > 0:
                    self.dx -= 1

                if self.dy < 0:
                    self.dy += 1
                elif self.dy > 0:
                    self.dy -= 1

                self.speed_decay_counter = 0

quitGame = False
pygame.mouse.set_pos(cursor_start_pos)
ball = Ball()   #creates one ball

#creates a list whose contents is d1, d2, d3... dn, where n is number_of_dots
#TODO: the below may be unnnecessary.  put range in the dot_objects list comprehension instead
dot_list = []
for i in range(0, number_of_dots):
    dot_list.append('d'+str(i))

#creates a list of objects from dot_list
dot_objects = [Dot() for dot_item in dot_list]

#prints the list of dot objects, for testing.
#for dot_object in dot_objects:
#    print(dot_objects)

#main loop
while not quitGame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True

        #if pygame.key.get_pressed() == pygame.K_SPACE:
        #    ball.dx, ball_dy = 0

        #print(event)  # prints key/mouse events in the console

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()



    # will lock ball to mouse cursor if left click
    if pygame.mouse.get_pressed() == (True, False, False):
        #print('ball x: ' + str(float(ball.x)))
        #print('ball y: ' + str(float(ball.y)))

        if ball_is_a_circle == True:
            ball.x = pygame.mouse.get_pos()[0]
            ball.y = pygame.mouse.get_pos()[1]

            #print('ball x: ' + str(float(ball.x)))
            #print('ball y: ' + str(float(ball.y)))

            # moving the mnouse and letting go of the ball gives locks that speed and direction to the ball
            ball.dx, ball.dy = pygame.mouse.get_rel()

        else:
            # left-clicking the mouse on the ball locks the ball to the cursor
            ball.x = pygame.mouse.get_pos()[0] - ball_width / 2
            ball.y = pygame.mouse.get_pos()[1] - ball_height / 2

            # moving the mnouse and letting go of the ball gives locks that speed and direction to the ball
            ball.dx, ball.dy = pygame.mouse.get_rel()

    #if pygame.mouse.get_pressed() == (False, False, True):
    #    ball = Ball()

    screen.fill(black)
    ball.update_position()
    ball.draw_ball()
    ball.bounce()   #ball will bounce off walls
    ball.speed_decay()

    #screen.lock()
    for dot_object in dot_objects:
        if dot_object.collision():
            dot_object.set_deflect_direction()

        dot_object.update_position()
        dot_object.draw_dot()
        dot_object.bounce()
        dot_object.speed_decay()   #slow down

        # to see what's happening with the stragglers at the end that won't stop
        #if not dot_object.dx == 0 or not dot_object.dy == 0:
        #    print(dot_object.dx,dot_object.dy)

    #screen.unlock()

    clock.tick(fps)
    pygame.display.update()

#next step:
#TODO: dots bounce off each other

#next step:
#TODO: space bar stops the ball

#next step:
#TODO: each time you click not on the ball, it creates a new ball
#TODO: each ball bounces off the walls and other balls
