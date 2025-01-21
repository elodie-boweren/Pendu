import pygame
from pygame.locals import *

pygame.init()

# couleur
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (190,190,190)
PINK = (255,192,203)





# dico to dectect the good keyboard
dictionary_keyboard = {
    K_a: "a", K_b: "b", K_c: "c", K_d: "d", K_e: "e", K_f: "f", K_g: "g",
    K_h: "h", K_i: "i", K_j: "j", K_k: "k", K_l: "l", K_m: "m", K_n: "n",
    K_o: "o", K_p: "p", K_q: "q", K_r: "r", K_s: "s", K_t: "t", K_u: "u",
    K_v: "v", K_w: "w", K_x: "x", K_y: "y", K_z: "z"
}


mot = "banane"

def hangman(color):
    # 1 wood
    pygame.draw.line(window, (color), [30, 400], [290, 400], 7)
    pygame.draw.line(window, (color), [60, 35], [60, 400], 7)
    pygame.draw.line(window, (color), [60, 38], [200, 38], 7)
    pygame.draw.line(window, (color), [60, 80], [115, 38], 7)
    pygame.draw.line(window, (color), [200, 35], [200, 80], 7)
    # 2 head
    pygame.draw.circle(window, (PINK), [201,115], 35,0)
    pygame.draw.circle(window, (color), [201,115], 35,7)
    # 3 chest
    pygame.draw.line(window, (color), [200, 150], [200, 250], 7) 
    # 4 left harm 
    pygame.draw.line(window, (color), [160, 160], [200, 200], 7)
    # 5 right harm 
    pygame.draw.line(window, (color), [240, 160], [200, 200], 7)
    # 6 left leg
    pygame.draw.line(window, (color), [160, 290], [200, 250], 7)
    # 7 right leg
    pygame.draw.line(window, (color), [240, 290], [200, 250], 7)

window = pygame.display.set_mode((640, 480))
running = True
current_color = GREY

# font :
police = pygame.font.SysFont("monospace" ,40)
image_texte = police.render ( mot, 1 , (0,0,0) )


while running :

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in dictionary_keyboard:
                letter = dictionary_keyboard[event.key]
                if letter in mot:
                    current_color = BLACK
                else:
                    current_color = GREY
            if event.key == K_BACKSPACE:
                current_color = GREY


    window.fill(WHITE) 
    hangman(current_color)  
    window.blit(image_texte, (320,240))
    pygame.display.update()

pygame.quit()