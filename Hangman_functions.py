import pygame
from pygame.locals import *
import random

pygame.init()
run = True

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (190,190,190)
PINK = (255,192,203)
BLUE = (40, 120, 230)
GREEN = (40, 230, 120)

screen = pygame.display.set_mode((800, 600))
center_x, center_y = 400, 300
clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS,Arial', 24)
prompt = font.render('Entrez un nombre : ', True, BLUE)
prompt_rect = prompt.get_rect(center=(center_x, center_y))
user_input_value = ""
user_input = font.render(user_input_value, True, GREEN)
user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)

title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 15)
text_font_bold = pygame.font.SysFont("Arial", 16, bold = True)


words = random.choice(open("words.txt").read().splitlines())
guess_words = words
found_letters = []
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

def add_word():
    screen.fill(WHITE)
    input_text = ""
    input_active = True
    
    while input_active:
        screen.fill(WHITE)
        display_hangman()
        
        # Instructions
        text("Type a new word to add", text_font, BLACK, 400, 200)
        text("Press ENTER to save, ESC to cancel", text_font, BLACK, 400, 250)
        
        # Display current input
        current_input_text = text_font.render(input_text, True, BLACK)
        screen.blit(current_input_text, (400, 300))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Save word if not empty
                    if input_text and len(input_text) > 1:
                        with open("words.txt", "a") as file:
                            file.write("\n" + input_text.lower())
                        text("Word added successfully!", text_font, BLACK, 400, 350)
                        pygame.display.update()
                        pygame.time.delay(1000)
                        input_active = False
                
                elif event.key == pygame.K_ESCAPE:
                    input_active = False
                
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    input_text += chr(event.key)
        
        pygame.display.update()
    
    # Return to menu after adding word
    menu()
def play_game():
    global guess_words, found_letters, attempts
    run = True
    while run :
        screen.fill(WHITE)

        letters_shown = " ".join([letter if letter in found_letters else "_" for letter in guess_words])
        write(letters_shown, text_font, BLACK, 600, 300)

        write(f"Attempts remaining: {attempts}", text_font, BLACK, 600, 350)
 
        letters_already_tried = " ".join(found_letters)
        write(f"Letters tried: {letters_already_tried}", text_font_bold, BLACK, 600, 400)
        
        draw_hangman(attempts)

        if all([letter in found_letters for letter in guess_words]):
            write("Congrats! You won !", text_font, BLACK, 600, 450)
            pygame.display.update()
            play_game()
        
        if attempts == 0:
            write(f"Perdu ! Le mot était: {guess_words}", text_font, BLACK, 600, 450)
            pygame.display.update()
            play_game()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key)
                    if letter not in found_letters:
                        found_letters.append(letter)
                        if letter not in guess_words:
                            attempts -= 1

        pygame.display.update()
    pygame.quit()

def add_word():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    continuer = False
                    break
                elif event.key == pygame.K_BACKSPACE:
                    user_input_value = user_input_value[:-1]
                else:
                    user_input_value += event.unicode
                    user_input = font.render(user_input_value, True, GREEN)
                    user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
    clock.tick(30)
    screen.fill(0)
    screen.blit(prompt, prompt_rect)
    screen.blit(user_input, user_input_rect)
    pygame.display.flip()
# print("La valeur de l'utilisateur convertie en entier est:", int(user_input_value))
    

        
