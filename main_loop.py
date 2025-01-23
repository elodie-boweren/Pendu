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
screen = pygame.display.set_mode((800, 600))
title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 50)

  
run = True
while run :
    #to recognize keyboard use
    key = pygame.key.get_pressed()

    menu()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if key[pygame.K_1] == True:
            play_game()
        elif key[pygame.K_2] == True:
            add_word()
        elif key[pygame.K_3] == True:
            run = False
    
    pygame.display.update()
   
pygame.quit()

