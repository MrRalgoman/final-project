import pygame
import sys
import time

pygame.init()


#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
grey = (100,100,100)

def drawScreen():
    #set screen size and fill 
    screen = pygame.display.set_mode((1000,600))
    screen.fill(white)
    #use a font 
    myFont = pygame.font.SysFont("monospace", 35)
    #draw first rectangle 
    pygame.draw.rect(screen, black, (100,50,400,100),0)
    label1 = myFont.render("PONG!", 1, (white))
    screen.blit(label1, (250, 100))
    
    #draw second rectangle
    pygame.draw.rect(screen, black, (100,250,400,100),0)
    label2 = myFont.render("HIGH SCORES", 1, (white))
    screen.blit(label2, (175, 300))
    #draw third rectangle
    pygame.draw.rect(screen, black, (100,450,400,100),0)
    label3 = myFont.render("QUIT", 1, (white))
    screen.blit(label3, (250, 500))

    pygame.display.update()
     
    #to change the colors of the diffrent options when hovered over
    
    while True:
        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
               #rectangle 1 
            if mx > 99 and mx < 500 and my > 46 and my < 149:
                pygame.draw.rect(screen, grey, (100,50,400,100),0)
                label1 = myFont.render("PONG!", 1, (white))
                screen.blit(label1, (250, 100))
            else:
                pygame.draw.rect(screen, black, (100,50,400,100),0)
                label1 = myFont.render("PONG!", 1, (white))
                screen.blit(label1, (250, 100))
                #rectangle 2
            if mx > 99 and mx < 500 and my > 250 and my < 350:
                pygame.draw.rect(screen, grey, (100,250,400,100),0)
                label2 = myFont.render("HIGH SCORES", 1, (white))
                screen.blit(label2, (175, 300))
            else:
                pygame.draw.rect(screen, black, (100,250,400,100),0)
                label2 = myFont.render("HIGH SCORES", 1, (white))
                screen.blit(label2, (175, 300))
            if mx > 99 and mx < 500 and my > 450 and my < 550:
                pygame.draw.rect(screen, grey, (100,450,400,100),0)
                label3 = myFont.render("QUIT", 1, (white))
                screen.blit(label3, (250, 500))
            else:
                pygame.draw.rect(screen, black, (100,450,400,100),0)
                label3 = myFont.render("QUIT", 1, (white))
                screen.blit(label3, (250, 500))

        pygame.display.update()
        time.sleep(.05)
        
       


drawScreen()
button()



