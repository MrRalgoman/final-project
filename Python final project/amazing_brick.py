import pygame

pygame.init()

# Colors
white = (255,255,255)
black = (0,0,0)

# Set the display width / height
DISP_W = 600
DISP_H = 700

# Initiate window
GAME_DISP = pygame.display.set_mode((DISP_W, DISP_H))
pygame.display.set_caption("Amazing Brick")

# Window background color
GAME_DISP.fill((255,255,255))
pygame.display.update()

X = DISP_W/2
Y = DISP_H/2

# Brick size
SIZE = 12

def amazing_brick():
    
    # Initiates game loop
    game_exit = True

    # Game loop
    while game_exit:
        # Gets all events
        for event in pygame.event.get():
            # Close event
            if event.type == pygame.QUIT:
                # Closes game loop
                game_exit = False

        # Draw diamond
        pygame.draw.polygon(GAME_DISP, black, [(X-SIZE, Y), (X, Y-SIZE), (X+SIZE, Y), (X, Y+SIZE)])

        pygame.display.update()

    # When game loop exits window closes
    pygame.quit()
    quit()

amazing_brick()