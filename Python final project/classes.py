# Classes file

import pygame

# Create ball sprite
class Ball(pygame.sprite.Sprite):
    # Used to initiate the ball
    def __init__(self):
        # Calls inhertance (pygame.sprite.Sprite) and initializes the sprite
        super(Ball, self).__init__()
        # Set the image to premade image...
        self.image = pygame.image.load("ball.png")
        # Need to get the rect of the image in order to repos it later on
        self.rect = self.image.get_rect()

    # Position function, set the position of the image
    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

class User_paddle(pygame.sprite.Sprite):
    def __init__(self):
        super(User_paddle, self).__init__()
        self.image = pygame.image.load("paddle.png")
        self.rect = self.image.get_rect()
    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y