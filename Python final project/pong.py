import pygame, sys, time, random
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
user_paddle = paddle("user_paddle.png")
AI_paddle = paddle("AI_paddle.png")

# Adding to groups
ball_group.add(ball)
collision_group.add(user_paddle)
collision_group.add(AI_paddle)

# ----- Functions ----- #
def text(text, size, color, x, y, position=None):
    myFont = pygame.font.SysFont("monospace", size)
    display = myFont.render(text, True, color)
    text_rect = display.get_rect(center=(x, y))
    if position == "left":
        text_rect = display.get_rect()
        text_rect.x = x
        text_rect.y = y
    GAME_DISP.blit(display, text_rect)

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
            if action == "high scores":
                highScores()
            if action == "start":
                gameStart()
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
        text("Pongs", 100, white, DISP_W/2, 100)
        text("By Lucas and Shawn", 25, white, DISP_W/2, 175)
        button("Play", 40, black, (DISP_W/2)-100, (DISP_H/2)-40, 200, 50, "play")
        button("High Scores", 40, black, (DISP_W/2)-150, (DISP_H/2)+60, 300, 50, "high scores")
        button("Quit", 40, black, (DISP_W/2)-100, (DISP_H/2)+160, 200, 50, "quit")
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

#----- High Scores -----#
def highScores():

    game_exit = False

    high_scores = open("high_scores.txt", "r").readlines()

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        # Drawing high score stuff
        GAME_DISP.fill(black)
        text("High Scores", 60, white, DISP_W/2, 40)
        button("Back", 40, black, (DISP_W/2)-100, 525, 200, 50, "start")
        outlinedRect(white, (DISP_W/2)-250, 85, 500, 420)
        pygame.draw.line(GAME_DISP, white, ((DISP_W/2)-250, 125), ((DISP_W/2)+249, 125))
        pygame.draw.line(GAME_DISP, white, ((DISP_W/2), 85), ((DISP_W/2), 503))
        text("User", 30, white, ((DISP_W/2)-200), 105)
        text("Score", 30, white, ((DISP_W/2)+60), 105)

        count = 0
        for line in high_scores:
            line = line.strip("\n")
            line = line.split()
            text((line[0] + line[1].ljust(10)), 30, white, (DISP_W/2)-235, 135+count, "left")
            count = count + 37

        pygame.display.update()
        
    clock.tick(FPS)

    pygame.quit()
    quit()

# ----- Main Func ----- #
def main():

    # Accepted username keys
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    charList = []
    for char in chars:
        charList.append(char)

    # Initiate the username for the game over loop
    username = ''

    # Setting the loop breakers
    game_exit = False
    game_pause = False
    game_over = False

    # ball positon/velocity
    ball_x = DISP_W/2
    ball_y = DISP_H/2
    # Randomize the bounce angle every time the game starts
    vel_x = random.randint(3, 5)
    vel_y = random.randint(3, 5)
    speed = 1

    # Change speed after how many seconds and by how much
    rate = 5
    change = 0.2

    # Counter to determine the score inside the game loop
    count = 0

    # ----- Game Loop ----- #
    while not game_exit:

        # Setting mouse to invisible while playing
        pygame.mouse.set_visible(False)

        # Score is the number of seconds a player lasts
        count = count + 1

        # pretty close to 1 second
        score = int(count/FPS)
        
        # Gets the mouseX and mouseY every frame
        mX, mY = pygame.mouse.get_pos()

        # ----- Game Pause ----- #
        while game_pause:

            pygame.mouse.set_visible(True)

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
                            ball_group.draw(GAME_DISP)
                            collision_group.draw(GAME_DISP)
                            text("x" + str(round(speed, 1)) + " Speed", 25, white, (DISP_W/2)-90, 25)
                            text("Score: " + str(score), 25, white, (DISP_W/2)+90, 25)
                            text("Game Resuming in " + str(i)  + "...", 50, white, DISP_W/2, DISP_H/2)
                            pygame.display.update()
                            # Takes miliseconds
                            pygame.time.wait(1000)
            
            GAME_DISP.fill(black)
            ball_group.draw(GAME_DISP)
            collision_group.draw(GAME_DISP)
            text("x" + str(round(speed, 1)) + " Speed", 25, white, (DISP_W/2)-90, 25)
            text("Score: " + str(score), 25, white, (DISP_W/2)+90, 25)
            # Pause menu text
            text("Game Paused", 75, white, DISP_W/2, 150)
            button("<SPACE> to resume", 25, black, (DISP_W/2)-150, (DISP_H/2)-20, 300, 40)
            pygame.display.update()

        # ----- Game Over ----- #
        while game_over:

            pygame.mouse.set_visible(True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    game_exit = True
                    
                # Basic text input
                if event.type == pygame.KEYDOWN:
                    # backspace
                    if event.key == pygame.K_BACKSPACE:
                        username = username[0:-1]
                    # space
                    if len(username) <= 10:
                        if event.key == pygame.K_SPACE:
                            key = ' '
                            username = username + key
                        # any key in the allowed character list
                        elif pygame.key.name(event.key) in charList:
                            key = pygame.key.name(event.key)
                            username = username + key
                        # quit
                        elif event.key == pygame.K_ESCAPE:
                            game_over = False
                            gameStart()
                        # continue
                        elif event.key == pygame.K_RETURN:
                            game_over = False
                            # High scores file
                            if username == "" or username == " ":
                                username = "GUEST"
                            username = username.ljust(10) + str(score)
                            scores = open("high_scores.txt", "a")
                            scores.write(username + "\n")
                            scores.close()
                            gameStart()

            GAME_DISP.fill(black)
            # Game over text
            text("Game Over", 75, white, DISP_W/2, 100)
            text("Enter a username: " + username, 30, white, DISP_W/2, DISP_H/2)
            pygame.display.update()

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
 
        # Changes the speed based on the rate in seconds
        for i in range(0, count+1, rate):
            if count == 60 * i:
                speed = speed + .2
                if vel_x > 0:
                    vel_x = vel_x + change
                else:
                    vel_x = vel_x - change

                if vel_y > 0:
                    vel_y = vel_y + change
                else:
                    vel_y = vel_y - change

        # Background fill
        GAME_DISP.fill(black)

        # timer display
        text("x" + str(round(speed, 1)) + " Speed", 25, white, (DISP_W/2)-90, 25)
        text("Score: " + str(score), 25, white, (DISP_W/2)+90, 25)

        # Setting positions
        ball.set_pos(ball_x, ball_y)
        user_paddle.set_pos(paddle_offset, mY-30)
        AI_paddle.set_pos((DISP_W - paddle_offset * 4), ball_y-7.5)

        if pygame.sprite.collide_rect(user_paddle, ball):
            user_paddle.set_pos(paddle_offset + 5, mY-30)

        if pygame.sprite.collide_rect(ball, AI_paddle):
            AI_paddle.set_pos((DISP_W - paddle_offset * 4) - 5, ball_y-7.5)

        # Collision detections
        if ball_y + 20 >= DISP_H or ball_y <= 0:
            vel_y = -vel_y

        if ball_x >= DISP_W:
            vel_x = -vel_x

        # Checks if there is a 
        if pygame.sprite.groupcollide(ball_group, collision_group, False, False):
            vel_x = -vel_x

        ball_y += vel_y
        ball_x += vel_x

        # GAME OVER
        if ball_x <= -20:
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

main()
