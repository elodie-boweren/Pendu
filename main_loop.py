import pygame
from pygame.locals import *
from Hangman_functions import *
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (190,190,190)
PINK = (255,192,203)

screen = pygame.display.set_mode((1000, 600))
title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 15)

  


run = True
while run == True:

    key = pygame.key.get_pressed()

    menu()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if key[pygame.K_1] == True:
            run = play_game()
        elif key[pygame.K_a] == True:
            add_word()
        elif key[pygame.K_q] == True:
            run = False
    
    pygame.display.update()

pygame.quit()


