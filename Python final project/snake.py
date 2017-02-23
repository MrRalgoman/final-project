import pygame

pygame.init()

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,100,100)
GREEN = (0,255,0)
BLUE = (120,120,255)
ORANGE = (255,165,0)
YELLOW = (255,255,0)

DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 600
B_WIDTH = 20
BORDER_WIDTH_RECT = [B_WIDTH, B_WIDTH, DISPLAY_WIDTH - B_WIDTH * 2, DISPLAY_HEIGHT - B_WIDTH * 2]

# Draw window
GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# Set window title
pygame.display.set_caption('Snake')
# Initiate timer
clock = pygame.time.Clock()

# Breaker for game loop
GAME_EXIT = False

LEAD_X = DISPLAY_WIDTH/2
LEAD_Y = DISPLAY_HEIGHT/2
LEAD_X_CHANGE = 0
LEAD_Y_CHANGE = 0

FPS = 18

BLOCK_SIZE = 20

# lists for movement, add and remove keys used here. (Shouldn't need to)
LEFT = [pygame.K_LEFT, pygame.K_a]
RIGHT = [pygame.K_RIGHT, pygame.K_d]
UP = [pygame.K_UP, pygame.K_w]
DOWN = [pygame.K_DOWN, pygame.K_s]

while not GAME_EXIT:
    # Game loop
    for event in pygame.event.get():
        # quits game
        if event.type == pygame.QUIT:
            GAME_EXIT = True
        # Snake movements
        if event.type == pygame.KEYDOWN:
            # Left/Right movements
            if event.key in LEFT:
                LEAD_X_CHANGE = -BLOCK_SIZE
                LEAD_Y_CHANGE = 0
            if event.key in RIGHT:
                LEAD_X_CHANGE = BLOCK_SIZE
                LEAD_Y_CHANGE = 0
            # Up/Down movements
            if event.key in UP:
                LEAD_Y_CHANGE = -BLOCK_SIZE
                LEAD_X_CHANGE = 0
            if event.key in DOWN:
                LEAD_Y_CHANGE = BLOCK_SIZE
                LEAD_X_CHANGE = 0

    # Boundaries
    if LEAD_X >= DISPLAY_WIDTH - 20 or LEAD_X < 20:
        GAME_EXIT = True
    if LEAD_Y >= DISPLAY_HEIGHT - 20 or LEAD_Y < 20:
        GAME_EXIT = True

    # Adds or subtracts the change from the boxes original position (300, 300)
    LEAD_X += LEAD_X_CHANGE
    LEAD_Y += LEAD_Y_CHANGE
        		
    GAME_DISPLAY.fill(RED)
    GAME_DISPLAY.fill(BLUE, rect=BORDER_WIDTH_RECT)
    pygame.draw.rect(GAME_DISPLAY, YELLOW, [LEAD_X, LEAD_Y, BLOCK_SIZE, BLOCK_SIZE])
    # Updates the window drawing with base
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()