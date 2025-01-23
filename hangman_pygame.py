import pygame
from pygame.locals import *
import random

pygame.init()

window = pygame.display.set_mode((1000, 800))
font = pygame.font.SysFont("Arial", 24)
# Définir les couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
line_width = 10 
police = pygame.font.SysFont(None, 40)
police_titre = pygame.font.SysFont(None, 60)


mots = ["words.txt"]
mot_a_trouver = random.choice(mots)
lettres_trouvees = []
attempts = 7
run = True

def afficher_texte(texte, police, couleur, x, y):
    texte_surface = police.render(texte, True, couleur)
    window.blit(texte_surface, (x, y))


def draw_hangman(attempts):
    if attempts <= 6:
        pygame.draw.line(window, BLACK, (50, 450), (250, 450), line_width)
    if attempts <= 5:
        pygame.draw.line(window, BLACK, (100, 450), (100, 50), line_width)
    if attempts <= 4:
        pygame.draw.line(window, BLACK, (75, 50), (350, 50), line_width)
    if attempts <= 3:
        pygame.draw.line(window, BLACK, (100, 125), (175, 50), line_width)
    if attempts <= 2:
        pygame.draw.line(window, BLACK, (345, 50), (345, 100), line_width)
    if attempts <= 1:
        pygame.draw.circle(window, BLACK, (345, 130), 30)
    if attempts <= 0:
        pygame.draw.line(window, BLACK, (345, 150), (345, 250), line_width)
        pygame.draw.line(window, BLACK, (345, 250), (300, 285), line_width)
        pygame.draw.line(window, BLACK, (345, 250), (400, 285), line_width)
        pygame.draw.line(window, BLACK, (345, 180), (400, 200), line_width)
        pygame.draw.line(window, BLACK, (345, 180), (300, 200), line_width)



def game():
    global mot_a_trouver, lettres_trouvees, attempts

    run=True
    while run :
        window.fill(WHITE)

        lettres_affichees = " ".join([lettre if lettre in lettres_trouvees else "_" for lettre in mot_a_trouver])
        afficher_texte(lettres_affichees, police, BLACK, 600, 300)

        afficher_texte(f"Essais restants: {attempts}", police, BLACK, 600, 350)
 
        lettres_deja_essayees = " ".join(lettres_trouvees)
        afficher_texte(f"Lettres essayées: {lettres_deja_essayees}", police, BLACK, 600, 400)
        
        draw_hangman(attempts)

        if all([lettre in lettres_trouvees for lettre in mot_a_trouver]):
            afficher_texte("Vous avez gagné !", police, BLACK, 600, 450)
            pygame.display.update()
            game()
        
        if attempts == 0:
            afficher_texte(f"Perdu ! Le mot était: {mot_a_trouver}", police, BLACK, 600, 450)
            pygame.display.update()
            game()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    lettre = chr(event.key)
                    if lettre not in lettres_trouvees:
                        lettres_trouvees.append(lettre)
                        if lettre not in mot_a_trouver:
                            attempts -= 1

        pygame.display.update()

game()
