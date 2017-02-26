# /home/lucas/python/final_project

import pygame, time, random

pygame.init()

window_size = window_width, window_height = 1200, 800
window = pygame.display.set_mode(window_size)

pygame.display.set_caption("Hey")
window.fill((255,255,255))

clock = pygame.time.Clock()
FPS = 60

running = True

while(running): 
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False


    clock.tick(FPS)

pygame.quit()
quit()
