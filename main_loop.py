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

player = "player"

run = True
while run :
    #to recognize keyboard use
    key = pygame.key.get_pressed()

    menu()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if key[pygame.K_1] == True:
            run = play_game(player,7)
        elif key[pygame.K_2] == True:
            run = play_game(player,5)
        elif key[pygame.K_3] == True:
            run = play_game(player,3)      
        elif key[pygame.K_4] == True:
            add_word()
        elif key[pygame.K_5] == True:
            player = player_choice()
        elif key[pygame.K_6] == True:
            run = print_score()
        elif key[pygame.K_7] == True:
            run = False
    pygame.display.update()
   
pygame.quit()

