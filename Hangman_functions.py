import pygame
from pygame.locals import *
import random

pygame.init()
run = True

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (190,190,190)
PINK = (255,192,203)

screen = pygame.display.set_mode((800, 600))
title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 15)
text_font_bold = pygame.font.SysFont("Arial", 16, bold = True)


mots = ["words.txt"]
mot_a_trouver = random.choice(mots)
lettres_trouvees = []
attempts = 7

def menu():
    screen.fill(WHITE) 
    text("Welcome to our \nHangman game!",title_font,(BLACK),400,50)
    text("What do you want to do ? : \nP. Play \nA. Add word \nQ. Quit \nType your choice:", text_font, (BLACK), 430, 200)
    display_hangman()


def display_hangman():
     # 1 wood
    pygame.draw.line(screen, (BLACK), [30, 400], [290, 400], 10)
    pygame.draw.line(screen, (BLACK), [60, 35], [60, 400], 10)
    pygame.draw.line(screen, (BLACK), [60, 38], [200, 38], 10)
    pygame.draw.line(screen, (BLACK), [60, 80], [115, 38], 10)
    pygame.draw.line(screen, (BLACK), [200, 35], [200, 80], 10)
    # 2 head
    pygame.draw.circle(screen, (BLACK), [201,115], 35,0)
    pygame.draw.circle(screen, (BLACK), [201,115], 35,10)
    # 3 chest
    pygame.draw.line(screen, (BLACK), [200, 150], [200, 250], 10) 
    # 4 left harm 
    pygame.draw.line(screen, (BLACK), [160, 160], [200, 200], 10)
    # 5 right harm 
    pygame.draw.line(screen, (BLACK), [240, 160], [200, 200], 10)
    # 6 left leg
    pygame.draw.line(screen, (BLACK), [160, 290], [200, 250], 10)
    # 7 right leg
    pygame.draw.line(screen, (BLACK), [240, 290], [200, 250], 10)


def text(text,font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))


def draw_hangman(attempts):
    if attempts <= 6:
        pygame.draw.line(screen, BLACK, (50, 450), (250, 450), 10)
        pygame.draw.line(screen, BLACK, (100, 450), (100, 50), 10)
        pygame.draw.line(screen, BLACK, (75, 50), (350, 50), 10)
        pygame.draw.line(screen, BLACK, (100, 125), (175, 50), 10)
        pygame.draw.line(screen, BLACK, (345, 50), (345, 100), 10)
    if attempts <= 5:
        pygame.draw.circle(screen, BLACK, (345, 130), 30)
    if attempts <= 4:
        pygame.draw.line(screen, BLACK, (345, 150), (345, 250), 10)
    if attempts <= 3:
        pygame.draw.line(screen, BLACK, (345, 180), (300, 160), 10)
    if attempts <= 2:
        pygame.draw.line(screen, BLACK, (345, 180), (400, 160), 10)
    if attempts <= 1:
        pygame.draw.line(screen, BLACK, (345, 250), (300, 285), 10)
    if attempts <= 0:
        pygame.draw.line(screen, BLACK, (345, 250), (400, 285), 10)
        

def write(texte, text_font, couleur, x, y):
    texte_surface = text_font.render(texte, True, couleur)
    screen.blit(texte_surface, (x, y))


def play_game():
    global mot_a_trouver, lettres_trouvees, attempts
    run = True
    while run :
        screen.fill(WHITE)

        lettres_affichees = " ".join([lettre if lettre in lettres_trouvees else "_" for lettre in mot_a_trouver])
        write(lettres_affichees, text_font, BLACK, 600, 300)

        write(f"Attempts remaining: {attempts}", text_font, BLACK, 600, 350)
 
        lettres_deja_essayees = " ".join(lettres_trouvees)
        write(f"Letters tried: {lettres_deja_essayees}", text_font_bold, BLACK, 600, 400)
        
        draw_hangman(attempts)

        if all([lettre in lettres_trouvees for lettre in mot_a_trouver]):
            write("Congrats! You won !", text_font, BLACK, 600, 450)
            pygame.display.update()
            play_game()
        
        if attempts == 0:
            write(f"Perdu ! Le mot était: {mot_a_trouver}", text_font, BLACK, 600, 450)
            pygame.display.update()
            play_game()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    lettre = chr(event.key)
                    if lettre not in lettres_trouvees:
                        lettres_trouvees.append(lettre)
                        if lettre not in mot_a_trouver:
                            attempts -= 1

        pygame.display.update()
    pygame.quit()


# def add_word():
#     screen.fill(WHITE) 
#     key = pygame.key.get_pressed()
#     display_hangman()
#     text("Type your word, or key Tab to return to main menu", text_font, (BLACK), 430, 200)
#     for event in pygame.event.get():
#         if key[pygame.K_TAB] == True:
#             return menu()
        
