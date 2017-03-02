import pygame, sys, time
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

def text(text, size, color, x, y):
    myFont = pygame.font.SysFont("monospace", size)
    button = myFont.render(text, True, color)
    text_rect = button.get_rect(center=(x, y))
    GAME_DISP.blit(button, text_rect)

def outlinedRect(color, x, y, width, height):
    pygame.draw.rect(GAME_DISP, color, [x, y, width, height])
    pygame.draw.rect(GAME_DISP, black, [x+1, y+1, width-2, height-2])


# ----- Game Func ----- #
def pong():

    # Setting the loop breakers
    game_exit = False
    game_pause = False
    game_over = False
    game_start = True

    # ball positon/velocity
    ball_x = DISP_W/2
    ball_y = DISP_H/2
    velocity = 3
        
    if ball_y >= DISP_H:
        velocity = -velocity

    # ----- Game Loop ----- #
    while not game_exit:
        
        # Gets the mouseX and mouseY every frame
        mX, mY = pygame.mouse.get_pos()

        # ----- Game Start ----- #
        while game_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_start = False
                    game_exit = True

            game_start = False

        # ----- Game Pause ----- #
        while game_pause:
            for event in pygame.event.get():
                # exits the pause and exits the game
                if event.type == pygame.QUIT:
                    game_pause = False
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    # Resumes game
                    if event.key == pygame.K_SPACE:
                        game_pause = False
                        # Resume countdown
                        for i in range(3, 0, -1):
                            GAME_DISP.fill(black)
                            text("Game Resuming in " + str(i)  + "...", 50, white, DISP_W/2, DISP_H/2)
                            pygame.display.update()
                            time.sleep(1)

            # Pause menu text
            text("Game Paused", 75, white, DISP_W/2, (DISP_H/2) - 100)
            outlinedRect(white, DISP_W/2 - 150, DISP_H/2 - 20, 300, 40)
            text("<SPACE> to resume", 25, white, DISP_W/2, DISP_H/2)
            
            pygame.display.update()

        # ----- Game Over ----- #
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    game_exit = True

            GAME_DISP.fill(black)
            text("You've Failed!", 100, white, DISP_W/2, DISP_H/2)
            pygame.display.update()
            time.sleep(1)
            game_over = False
            game_start = True

        # ----- Game Events ----- #
        for event in pygame.event.get():
            # Close event
            if event.type == pygame.QUIT:
                # Closes game loop
                game_exit = True
            
            # Game pause
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_pause = True

        # Background fill
        GAME_DISP.fill(black)

        # Setting positions
        ball.set_pos(ball_x, ball_y)
        paddle1.set_pos(paddle_offset, mY-30)

        ball_x += -velocity

        # GAME OVER
        if ball_x <= -25:
            game_over = True

        # Drawing sprites
        ball_group.draw(GAME_DISP)
        collision_group.draw(GAME_DISP)

        # Display update to draw on screen
        pygame.display.update()

        # Setting FPS
        clock.tick(FPS)

    # ----- Game Over ----- #
    pygame.quit()
    quit()

pong()
