import pygame, objects

pygame.init()

# Colors
white = (255,255,255)
black = (0,0,0)

# Set the display width / height
DISP_W = 1000
DISP_H = 600

# Initiate window
GAME_DISP = pygame.display.set_mode((DISP_W, DISP_H))
pygame.display.set_caption("Pong")

# Window background color
GAME_DISP.fill(black)
pygame.display.update()

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

    # When game loop exits window closes
    pygame.quit()
    quit()

amazing_brick()
