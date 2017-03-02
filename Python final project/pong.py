import pygame
from classes import *
from colors import *

pygame.init()

# Settings
DISP_W = 1000
DISP_H = 600
FPS = 60
boundary_thickness = 15
paddle_offset = 10

# Initiate window
GAME_DISP = pygame.display.set_mode((DISP_W, DISP_H))
pygame.display.set_caption("Pong")

# Allows us to limit the tick rate
clock = pygame.time.Clock()

# Sprite groups
ball_group = pygame.sprite.Group()
collision_group = pygame.sprite.Group()

# Initiating sprites
ball = Ball()
paddle1 = User_paddle()

# Adding to groups
ball_group.add(ball)
collision_group.add(paddle1)

# ----- Game Loop ----- #

# Setting the loop breakers
game_exit = False

# ball positon/velocity
ball_x = DISP_W/2
ball_y = DISP_H/2
velocity = 3
    
if ball_y >= DISP_H:
    velocity = -velocity

# Game loop
while not game_exit:

    # Gets the mouseX and mouseY every frame
    mX, mY = pygame.mouse.get_pos()
    
    # Gets all events
    for event in pygame.event.get():
        # Close event
        if event.type == pygame.QUIT:
            # Closes game loop
            game_exit = True            

    # Background fill
    GAME_DISP.fill(black)

    # Setting positions
    ball.set_pos(ball_x, ball_y)
    paddle1.set_pos(paddle_offset, mY-30)

    ball_x += velocity

    # Drawing sprites
    ball_group.draw(GAME_DISP)
    collision_group.draw(GAME_DISP)

    # Display update to draw on screen
    pygame.display.update()

    # Setting FPS
    clock.tick(FPS)

# ----- Game exit ----- #
pygame.quit()
quit()
