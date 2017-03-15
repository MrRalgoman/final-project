import pygame, sys, time, random
from classes import *
from colors import *

pygame.init()

#load music
pygame.mixer.music.load("rock_and_roll.ogg")
slap = pygame.mixer.Sound("slap.wav")

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
user_paddle = game_paddle("user_paddle.png")
AI_paddle = game_paddle("AI_paddle.png")

# Adding to groups
ball_group.add(ball)
collision_group.add(user_paddle)
collision_group.add(AI_paddle)

# --------------------- #
# ----- Functions ----- #
# --------------------- #

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

        # Changes the color to grey while mouse is in the button
        color = light
        text_color = black

        # If left mouse button pressed
        if b1 and action != None:

            if action == "quit":
                pygame.quit()
                quit()
            if action == "play":
                pygame.mixer.music.play(1)
                main()
            if action == "high scores":
                highScores()
            if action == "start":
                gameStart()
        

    # Draw buttons and text
    pygame.draw.rect(GAME_DISP, white, [x, y, w, h])
    pygame.draw.rect(GAME_DISP, color, [x+1, y+1, w-2, h-2])
    myFont = pygame.font.SysFont("monospace", size)
    button = myFont.render(text, True, text_color)
    text_rect = button.get_rect(center=(x+w/2, y+h/2))
    GAME_DISP.blit(button, text_rect)

# ---------------------- #
# ----- Game Start ----- #
# ---------------------- #

def gameStart():

    game_exit = False

    while not game_exit:
        pygame.mixer.music.play(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                
        # Play button
        GAME_DISP.fill(black)
        text("Pong.S", 100, white, DISP_W/2, 100)
        text("By Lucas and Shawn", 25, white, DISP_W/2, 175)
        button("Play", 40, black, (DISP_W/2)-100, (DISP_H/2)-40, 200, 50, "play")
        button("High Scores", 40, black, (DISP_W/2)-150, (DISP_H/2)+60, 300, 50, "high scores")
        button("Quit", 40, black, (DISP_W/2)-100, (DISP_H/2)+160, 200, 50, "quit")
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

# --------------------- #
# ----- Game Over ----- #
# --------------------- #

def gameOver(score):
    
    # Accepted username keys
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    charList = []
    for char in chars:
        charList.append(char)

    # Initiate the username for the game over loop
    username = ''

    game_over = True

    count = 0
    
    while game_over:

        count = count + 1

        # Calculate timer
        time = round((count/FPS), 1)

        pygame.mouse.set_visible(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
                    
            # Basic text input
            if event.type == pygame.KEYDOWN:
                # backspace
                if event.key == pygame.K_BACKSPACE:
                    username = username[0:-1]

                if event.key == pygame.K_RETURN:

                    # High scores file
                    if username == "" or username == " ":
                        username = "GUEST"

                    # Opens in a+ mode, the + creates a file if it's not already created
                    scores = open("high_scores.txt", "a+")
                    scores.write(username + "\n")
                    scores.write(str(score) + "\n")
                    scores.close()
                    game_over = False
                    gameStart()
                
                if len(username) <= 10: 
                    
                    # Space
                    if event.key == pygame.K_SPACE:
                        key = ' '
                        username = username + key
                    # Any key in the allowed character list
                    elif pygame.key.name(event.key) in charList:
                        key = pygame.key.name(event.key)
                        username = username + key
                    # Quit
                    elif event.key == pygame.K_ESCAPE:
                        game_over = False
                        gameStart()

        GAME_DISP.fill(black)

        # Game over text
        text("Game Over", 75, white, DISP_W/2, 100)
        text("You scored " + str(score) + " points!", 30, white, DISP_W/2, 175)
        text("Enter a username: " + username, 30, white, DISP_W/2, DISP_H/2)

        # The drawing of the blinking cursor for the text entry
        if str(time)[-1] in ['1', '2', '3', '4', '5']:
            if len(username) == 0:
                text("|", 35, white, DISP_W/2 + 160, DISP_H/2)
            if len(username) == 1:
                text("|", 35, white, DISP_W/2 + 172, DISP_H/2)
            if len(username) == 2:
                text("|", 35, white, DISP_W/2 + 181, DISP_H/2)
            if len(username) == 3:
                text("|", 35, white, DISP_W/2 + 190, DISP_H/2)
            if len(username) == 4:
                text("|", 35, white, DISP_W/2 + 199, DISP_H/2)
            if len(username) == 5:
                text("|", 35, white, DISP_W/2 + 208, DISP_H/2)
            if len(username) == 6:
                text("|", 35, white, DISP_W/2 + 217, DISP_H/2)
            if len(username) == 7:
                text("|", 35, white, DISP_W/2 + 226, DISP_H/2)
            if len(username) == 8:
                text("|", 35, white, DISP_W/2 + 235, DISP_H/2)
            if len(username) == 9:
                text("|", 35, white, DISP_W/2 + 244, DISP_H/2)
            if len(username) == 10:
                text("|", 35, white, DISP_W/2 + 253, DISP_H/2)
            if len(username) == 11:
                text("|", 35, white, DISP_W/2 + 262, DISP_H/2)
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

# ----------------------- #
# ----- High Scores ----- #
# ----------------------- #

def highScores():

    game_exit = False

    # runs if high_scores.txt exists
    try:

        high_scores = open("high_scores.txt", "r").readlines()

        count = 1

        # Converts the str numbers from the file to integers
        # Skips every other list item starting at 1 (only gets odds)
        for line in high_scores[1::2]:
            # Setting the list item to an integer
            number = int(line)
            # Replacing each position that we grabbed with the integer
            high_scores[count] = number
            # We are skipping ever other item in the loop so the count adds 2 every time
            count = count + 2

        scoreList = []

        # Creating sorted list
        for i in range(0, len(high_scores), 2):

            # Taking the pair of username and score from the high_scores list and
            # appending them onto the new scoreList as a pair for example:
            # scoreList = [[username, score], [username, score], [username, score]]
            scoreList.append(high_scores[i:i+2])

        # Actual sort, have to reverse so high to low
        scoreList = sorted(scoreList, key=lambda x: x[1], reverse = True)

        while not game_exit:

            pygame.mixer.music.stop()

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

            # Only displays the first 10 items in the list
            scoreList = scoreList[0:10]

            count = 0
            # Loops through the scorelist and displays them
            for line in scoreList:
                # Username
                text((line[0]).strip('\n'), 30, white, (DISP_W/2)-235, 133+count, "left")
                # Score
                text(str((line[1])), 30, white, (DISP_W/2)+15, 133+count, "left")
                # The count is the vertical distance in pixels between the usernames and scores
                count = count + 37

            pygame.display.update()
        
            clock.tick(FPS)

        pygame.quit()
        quit()

    # If high_scores.txt doesn't exist this runs
    except FileNotFoundError:

        while not game_exit:

            pygame.mixer.music.stop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

            GAME_DISP.fill(black)
            
            # Drawing message saying that the file does not exist
            text("High Scores", 60, white, DISP_W/2, 40)
            button("Back", 40, black, (DISP_W/2)-100, 525, 200, 50, "start")
            text("High score records not found...", 35, white, DISP_W/2, DISP_H/2)

            pygame.display.update()
            
            clock.tick(FPS)

        pygame.quit()
        quit()

# --------------------- #
# ----- Main Func ----- #
# --------------------- #

def main():

    # Setting the loop breakers
    game_exit = False
    game_pause = False

    # Ball initial position
    ball_x = DISP_W/2
    ball_y = DISP_H/2

    # Randomize the bounce angle every time the game starts
    vel_x = random.randint(3, 5)
    vel_y = random.randint(3, 5)

    # Change the speed after how many seconds
    rate = 5

    # Change the actual game ball speed increase interval here
    change = 0.75

    # Only the initial speed number that displays on screen
    speed = 1

    # Counter to determine the score inside the game loop
    count = 0

    # ----- Game Loop ----- #
    while not game_exit:

        # Unpauses the game music
        pygame.mixer.music.unpause()

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

            # Pauses the game music
            pygame.mixer.music.pause()

            pygame.mouse.set_visible(True)

            for event in pygame.event.get():
                # exits the pause and exits the game
                if event.type == pygame.QUIT:
                    # Breaks out of the pause loop
                    game_pause = False
                    # Breaks out of the game loop
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    # Resumes game
                    if event.key == pygame.K_SPACE:
                        game_pause = False
                        # Resume countdown
                        for i in range(3, 0, -1):

                            # Pause menu countdown text
                            GAME_DISP.fill(black)

                            # Have to redraw the ball and paddles
                            ball_group.draw(GAME_DISP)
                            collision_group.draw(GAME_DISP)
                            text("x" + str(round(speed, 1)) + " Speed", 25, white, (DISP_W/2)-90, 25)
                            text("Score: " + str(score), 25, white, (DISP_W/2)+90, 25)
                            text("Game Resuming in " + str(i)  + "...", 40, white, DISP_W/2, DISP_H/2)

                            pygame.display.update()

                            # Takes miliseconds
                            # Waits 1 second
                            pygame.time.wait(1000)
            
            GAME_DISP.fill(black)
            
            # Have to redraw the ball and paddles
            ball_group.draw(GAME_DISP)
            collision_group.draw(GAME_DISP)
            text("x" + str(round(speed, 1)) + " Speed", 25, white, (DISP_W/2)-90, 25)
            text("Score: " + str(score), 25, white, (DISP_W/2)+90, 25)
            # Pause menu text
            text("Game Paused", 75, white, DISP_W/2, 150)
            text("<SPACE> to resume...", 40, white, DISP_W/2, DISP_H/2)

            pygame.display.update()

        # ----- Game Events ----- #
        for event in pygame.event.get():
            # Close event
            if event.type == pygame.QUIT:
                # Breaks out of the game loop
                game_exit = True
            
            # Game pause
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Starts the game_pause loop
                    game_pause = True
 
        # Changes the speed based on the rate in seconds
        for i in range(0, count+1, rate):
            # Fires 1 frame based on what the rate is set to
            if count == 60 * i:
                # Changes the speed display on the game screen
                speed = speed + .2
                # Have to make sure that the speed changes in the correct direction
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

        # Timer display
        text("x" + str(round(speed, 1)) + " Speed", 25, white, (DISP_W/2)-90, 25)
        text("Score: " + str(score), 25, white, (DISP_W/2)+90, 25)

        # Setting positions
        ball.set_pos(ball_x, ball_y)
        user_paddle.set_pos(paddle_offset, mY-30)
        AI_paddle.set_pos((DISP_W - paddle_offset * 4), ball_y-7.5)

        # Checking for the collision of the ball and the users paddle
        if pygame.sprite.collide_rect(user_paddle, ball):
            # Animates the paddle to move a pixel forward for the frame it is colliding in
            user_paddle.set_pos(paddle_offset + 5, mY-30)

        if pygame.sprite.collide_rect(ball, AI_paddle):
            AI_paddle.set_pos((DISP_W - paddle_offset * 4) - 5, ball_y-7.5)

        # Collision detections
        if ball_y + 75 >= DISP_H or ball_y <= 0:
            # Inverts the y direction the ball is moving in
            vel_y = -vel_y

        # Checks if there is a collision in between the ball and collision group
        if pygame.sprite.groupcollide(ball_group, collision_group, False, False):
            # Inverts the x direction the ball is moving in
            vel_x = -vel_x
            # Plays the slap sound
            pygame.mixer.Sound.play(slap)

        # Setting the ball position based on the velocity
        ball_y += vel_y
        ball_x += vel_x


        # GAME OVER
        if ball_x <= -20:
            # Stops music when you die
            pygame.mixer.music.stop()
            # Calls the gameover function with the score you got
            gameOver(score)

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

# Starts the game
gameStart()
