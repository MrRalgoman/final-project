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

# ----- Functions ----- #
def text(text, size, color, x, y):
    myFont = pygame.font.SysFont("monospace", size)
    button = myFont.render(text, True, color)
    text_rect = button.get_rect(center=(x, y))
    GAME_DISP.blit(button, text_rect)

def outlinedRect(color, x, y, w, h):
    pygame.draw.rect(GAME_DISP, color, [x, y, w, h])
    pygame.draw.rect(GAME_DISP, black, [x+1, y+1, w-2, h-2])

def button(text, size, color, x, y, w, h, action=None):
    # sets list of the width and height of the button
    button_width = range(int(x), int(x)+int(w))
    button_height = range(int(y), int(y)+int(h))
    text_color = white
    # Get's mouse x and y
    mX, mY = pygame.mouse.get_pos()
    b1, b2, b3 = pygame.mouse.get_pressed()

    # Checks if the mouse is in the button width/height
    if mX in button_width and mY in button_height:
        # If left mouse button pressed
        if b1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "play":
                main()
        color = grey
        

    # Draw buttons and text
    pygame.draw.rect(GAME_DISP, white, [x, y, w, h])
    pygame.draw.rect(GAME_DISP, color, [x+1, y+1, w-2, h-2])
    myFont = pygame.font.SysFont("monospace", size)
    button = myFont.render(text, True, text_color)
    text_rect = button.get_rect(center=(x+w/2, y+h/2))
    GAME_DISP.blit(button, text_rect)

# ----- Game Start ----- #
def gameStart():

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                
        # Play button
        GAME_DISP.fill(black)
        text("Pong", 100, white, DISP_W/2, 100)
        text("By Lucas and Shawn", 25, white, DISP_W/2, 175)
        button("Play", 40, black, (DISP_W/2)-300, (DISP_H/2)-25, 200, 50, "play")
        button("Quit", 40, black, (DISP_W/2)+100, (DISP_H/2)-25, 200, 50, "quit")
        button("High Scores", 40, black, (DISP_W/2)-150, (DISP_H/2)+100, 300, 50)
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

# ----- Main Func ----- #
def main():

    # Setting the loop breakers
    game_exit = False
    game_pause = False
    game_over = False

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
            
            GAME_DISP.fill(black)
            # Pause menu text
            text("Game Paused", 75, white, DISP_W/2, 150)
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
            main()

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
            gameStart()

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

gameStart()
