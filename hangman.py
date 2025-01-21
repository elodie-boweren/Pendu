import pygame
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (190,190,190)
PINK = (255,192,203)

window = pygame.display.set_mode((640, 480))
running = True

while running :

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    window.fill(WHITE)    
    # 1 wood
    pygame.draw.line(window, (BLACK), [30, 400], [290, 400], 7)
    pygame.draw.line(window, (BLACK), [60, 35], [60, 400], 7)
    pygame.draw.line(window, (BLACK), [60, 38], [200, 38], 7)
    pygame.draw.line(window, (BLACK), [60, 80], [115, 38], 7)
    pygame.draw.line(window, (BLACK), [200, 35], [200, 80], 7)
    # 2 head
    pygame.draw.circle(window, (PINK), [201,115], 35,0)
    pygame.draw.circle(window, (BLACK), [201,115], 35,7)
    # 3 chest
    pygame.draw.line(window, (BLACK), [200, 150], [200, 250], 7) 
    # 4 left harm 
    pygame.draw.line(window, (BLACK), [160, 160], [200, 200], 7)
    # 5 right harm 
    pygame.draw.line(window, (BLACK), [240, 160], [200, 200], 7)
    # 6 left leg
    pygame.draw.line(window, (BLACK), [160, 290], [200, 250], 7)
    # 7 right leg
    pygame.draw.line(window, (BLACK), [240, 290], [200, 250], 7)

    pygame.display.update()
pygame.quit()