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


words = ["banane","chocolat"]
guess_words = random.choice(words)
found_letters = []


def menu():
    screen.fill(WHITE) 
    text("Welcome to our", title_font, (BLACK), 400, 50)
    text("Hangman game !", title_font, (BLACK), 400, 90)
    text("What do you want to do ?", text_font, (BLACK), 430, 200)
    text("1. Play on Easy mode", text_font, (BLACK), 430, 230)
    text("2. Play on Normal mode", text_font, (BLACK), 430, 250)
    text("3. Play on Hard mode", text_font, (BLACK), 430, 270)
    text("4. Add word", text_font, (BLACK), 430, 290)
    text("5. Quit", text_font, (BLACK), 430, 310)
    text("Type your choice", text_font, (BLACK), 430, 330)
    display_hangman()


def display_hangman():
     # 1 wood
    pygame.draw.line(screen, (BLACK), [30, 400], [290, 400], 10)
    pygame.draw.line(screen, (BLACK), [60, 35], [60, 400], 10)
    pygame.draw.line(screen, (BLACK), [60, 38], [200, 38], 10)
    pygame.draw.line(screen, (BLACK), [60, 80], [115, 38], 10)
    pygame.draw.line(screen, (BLACK), [200, 35], [200, 80], 10)
    # 2 head
    pygame.draw.circle(screen, (PINK), [201,115], 35,0)
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


def draw_hangman_easy(attempts):
    if attempts < 6:
        pygame.draw.line(screen, BLACK, (50, 450), (250, 450), 10)
        pygame.draw.line(screen, BLACK, (100, 450), (100, 50), 10)
        pygame.draw.line(screen, BLACK, (75, 50), (350, 50), 10)
        pygame.draw.line(screen, BLACK, (100, 125), (175, 50), 10)
        pygame.draw.line(screen, BLACK, (345, 50), (345, 100), 10)
    if attempts < 5:
        pygame.draw.circle(screen, PINK, (345, 130),30, 0)
        pygame.draw.circle(screen, BLACK, (345, 130), 30, 10)
    if attempts < 4:
        pygame.draw.line(screen, BLACK, (345, 150), (345, 250), 10)
    if attempts < 3:
        pygame.draw.line(screen, BLACK, (345, 180), (300, 160), 10)
    if attempts < 2:
        pygame.draw.line(screen, BLACK, (345, 180), (400, 160), 10)
    if attempts < 1:
        pygame.draw.line(screen, BLACK, (345, 250), (300, 285), 10)
    if attempts == 0:
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
def play_game_easy():
    global guess_words, found_letters, attempts
    attempts = 7
    run = True
    while run :
        screen.fill(WHITE)

        letter_shown = []

        for lettre in guess_words:
            if lettre in found_letters:
                letter_shown.append(lettre)
            else:
                letter_shown.append("_")

        letter_shown_str = " ".join(letter_shown)
        write(letter_shown_str, text_font, BLACK, 600, 300)

        write(f"Attempts remaining: {attempts}", text_font, BLACK, 600, 350)
 
        letters_already_tried = " ".join(found_letters)
        write(f"Letters tried: ", text_font_bold, BLACK, 600, 400)
        write(f"{letters_already_tried}", text_font_bold, BLACK, 600, 430)
        
        draw_hangman_easy(attempts)

        if all([letter in found_letters for letter in guess_words]):
            write("Congrats! You won !", text_font, BLACK, 600, 450)
            pygame.display.update()
            play_game_easy()
        
        if attempts == 0:
            write(f"Perdu ! Le mot était: {guess_words}", text_font, BLACK, 600, 450)
            pygame.display.update()
            play_game_easy()
        
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

def play_game_mid():
    global guess_words, found_letters, attempts
    attempts = 5
    run = True
    while run :
        screen.fill(WHITE)

        letter_shown = []

        for lettre in guess_words:
            if lettre in found_letters:
                letter_shown.append(lettre)
            else:
                letter_shown.append("_")

        letter_shown_str = " ".join(letter_shown)
        write(letter_shown_str, text_font, BLACK, 600, 300)

        write(f"Attempts remaining: {attempts}", text_font, BLACK, 600, 350)
 
        letters_already_tried = " ".join(found_letters)
        write(f"Letters tried: ", text_font_bold, BLACK, 600, 400)
        write(f"{letters_already_tried}", text_font_bold, BLACK, 600, 430)
        
        draw_hangman_mid(attempts)

        if all([letter in found_letters for letter in guess_words]):
            write("Congrats! You won !", text_font, BLACK, 600, 450)
            pygame.display.update()
            play_game_mid()
        
        if attempts == 0:
            write(f"Perdu ! Le mot était: {guess_words}", text_font, BLACK, 600, 450)
            pygame.display.update()
            play_game_mid()
        
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


def draw_hangman_mid(attempts):
    if attempts <= 4:
        pygame.draw.line(screen, BLACK, (50, 450), (250, 450), 10)
        pygame.draw.line(screen, BLACK, (100, 450), (100, 50), 10)
    if attempts <= 3:
        pygame.draw.line(screen, BLACK, (75, 50), (350, 50), 10)
        pygame.draw.line(screen, BLACK, (100, 125), (175, 50), 10)
        pygame.draw.line(screen, BLACK, (345, 50), (345, 100), 10)
    if attempts <= 2:
        pygame.draw.circle(screen, PINK, (345, 130),30, 0)
        pygame.draw.circle(screen, BLACK, (345, 130), 30, 10)
    if attempts <= 1:
        pygame.draw.line(screen, BLACK, (345, 180), (300, 160), 10)
        pygame.draw.line(screen, BLACK, (345, 150), (345, 250), 10)
    if attempts <= 0:
        pygame.draw.line(screen, BLACK, (345, 180), (400, 160), 10)
        pygame.draw.line(screen, BLACK, (345, 250), (300, 285), 10)
        pygame.draw.line(screen, BLACK, (345, 250), (400, 285), 10)


def play_game_hard():
    global guess_words, found_letters, attempts
    attempts = 3
    run = True
    while run :
        screen.fill(WHITE)

        letter_shown = []

        for lettre in guess_words:
            if lettre in found_letters:
                letter_shown.append(lettre)
            else:
                letter_shown.append("_")

        letter_shown_str = " ".join(letter_shown)
        write(letter_shown_str, text_font, BLACK, 600, 300)

        write(f"Attempts remaining: {attempts}", text_font, BLACK, 600, 350)
 
        letters_already_tried = " ".join(found_letters)
        write(f"Letters tried: ", text_font_bold, BLACK, 600, 400)
        write(f"{letters_already_tried}", text_font_bold, BLACK, 600, 430)
        
        draw_hangman_hard(attempts)

        if all([letter in found_letters for letter in guess_words]):
            write("Congrats! You won !", text_font, BLACK, 600, 450)
            pygame.display.update()
            end_game()
        
        if attempts == 0:
            write(f"You loose ! The word was: {guess_words}", text_font, BLACK, 600, 450)
            pygame.display.update()
            end_game()
        
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


def draw_hangman_hard(attempts):
        
    if attempts <= 2:
        pygame.draw.line(screen, BLACK, (50, 450), (250, 450), 10)
        pygame.draw.line(screen, BLACK, (100, 450), (100, 50), 10)
        pygame.draw.line(screen, BLACK, (75, 50), (350, 50), 10)
        pygame.draw.line(screen, BLACK, (100, 125), (175, 50), 10)
    if attempts <= 1:
        pygame.draw.line(screen, BLACK, (345, 50), (345, 100), 10)
        pygame.draw.circle(screen, PINK, (345, 130),30, 0)
        pygame.draw.circle(screen, BLACK, (345, 130), 30, 10)
    if attempts <= 0:
        pygame.draw.line(screen, BLACK, (345, 180), (300, 160), 10)
        pygame.draw.line(screen, BLACK, (345, 150), (345, 250), 10)
        pygame.draw.line(screen, BLACK, (345, 180), (400, 160), 10)
        pygame.draw.line(screen, BLACK, (345, 250), (300, 285), 10)
        pygame.draw.line(screen, BLACK, (345, 250), (400, 285), 10)

  
run = True
while run :

    key = pygame.key.get_pressed()

    menu()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if key[pygame.K_1] == True:
            play_game_easy()
            if key[pygame.K_1] == True:
                play_game_easy
            if key[pygame.K_2] == True:
                menu()    
        if key[pygame.K_2] == True:
            play_game_mid()
            if key[pygame.K_1] == True:
                play_game_easy
            if key[pygame.K_2] == True:
                menu() 
        if key[pygame.K_3] == True:
            play_game_hard()
            if key[pygame.K_1] == True:
                play_game_easy
            if key[pygame.K_2] == True:
                menu() 
        elif key[pygame.K_4] == True:
            add_word()
        elif key[pygame.K_5] == True:
            run = False    
    
    pygame.display.update()
   
pygame.quit()

def end_game():
    screen.fill(WHITE) 
    text("What do you want to do?", title_font, (BLACK), 400, 50)
    text("1 = Play again", title_font, (BLACK), 400, 90)
    text("2 = Back to menu", text_font, (BLACK), 430, 200)