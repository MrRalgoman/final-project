import pygame
import sys

pygame.init()


#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

def drawScreen():
    screen = pygame.display.set_mode((600,600))
    screen.fill(white)

    myFont = pygame.font.SysFont("monospace", 35)

    pygame.draw.rect(screen, green, (100,50,400,100),0)

    label = myFont.render("PLAY AMAZING BRICK!", 1, (black))
    screen.blit(label, (100, 100))

    pygame.draw.rect(screen, green, (100,250,400,100),0)

    label = myFont.render("HIGH SCORES", 1, (black))
    screen.blit(label, (100, 300))

    pygame.draw.rect(screen, green, (100,450,400,100),0)

    label = myFont.render("QUIT", 1, (black))
    screen.blit(label, (100, 500))



    pygame.display.update()

drawScreen()



