import pygame
from pygame.locals import *
from Hangman_functions import *

pygame.init()

#colors used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (190,190,190)
PINK = (255,192,203)

#screen and text formats
screen = pygame.display.set_mode((900, 600))
title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 50)

  
run = True
while run :
    #to recognize keyboard use

    menu()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                play_game()
            elif event.key == pygame.K_2:
                add_word()
            elif event.key == pygame.K_3:
                run = False
    
    pygame.display.update()
   
pygame.quit()

