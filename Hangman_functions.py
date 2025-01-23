import pygame
from pygame.locals import *
import random

pygame.init()
run = True

#colors used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (190,190,190)
PINK = (255,192,203)

#screen and text formatting
screen = pygame.display.set_mode((800, 600))
title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 15)
text_font_bold = pygame.font.SysFont("Arial", 16, bold = True)

#to get a new word for the game
words = random.choice(open("words.txt").read().splitlines())
guess_words = words
found_letters = []
attempts = 7

#Menu function
def menu():
    screen.fill(WHITE) 
    text("Welcome to our", title_font, (BLACK), 400, 50)
    text("Hangman game !", title_font, (BLACK), 400, 90)
    text("What do you want to do ?", text_font, (BLACK), 430, 200)
    text("1 = Play", text_font, (BLACK), 430, 230)
    text("2 = Add word", text_font, (BLACK), 430, 260)
    text("3 = Quit", text_font, (BLACK), 430, 290)
    text("Type your choice", text_font, (BLACK), 430, 320)
    display_hangman()

#Menu hangman display
def display_hangman():
     # 1 frame
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
    # 4 left arm 
    pygame.draw.line(screen, (BLACK), [160, 160], [200, 200], 10)
    # 5 right arm 
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
        pygame.draw.circle(screen, PINK, (345, 130),30, 0)
        pygame.draw.circle(screen, BLACK, (345, 130), 30, 10)
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
        
#Function for text style
def write(texte, text_font, couleur, x, y):
    texte_surface = text_font.render(texte, True, couleur)
    screen.blit(texte_surface, (x, y))

#Add a word to the .txt document
def add_word():
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
                #ESC to return to menu
                elif event.key == pygame.K_ESCAPE:
                    input_active = False
                #recognize key to erase letter entered
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    input_text += chr(event.key)
        
        pygame.display.update()
    
    # Return to menu after adding word
    menu()

#Function to play game
def play_game():
    global guess_words, found_letters, attempts
    run = True
    while run :
        screen.fill(WHITE)
        #Set screen with _ corresponding to each letter of then word until letter guessed
        letters_shown = " ".join([letter if letter in found_letters else "_" for letter in guess_words])
        write(letters_shown, text_font, BLACK, 600, 300)
        #update the number of attempts remaining
        write(f"Attempts remaining: {attempts}", text_font, BLACK, 600, 350)
        #
        letters_already_tried = " ".join(found_letters)
        write(f"Letters tried: ", text_font_bold, BLACK, 600, 400)
        write(f"{letters_already_tried}", text_font_bold, BLACK, 600, 430)
        #Draw hangman as attempts fail
        draw_hangman(attempts)
        #check if word guessed
        if all([letter in found_letters for letter in guess_words]):
            write("Congrats! You won !", text_font, BLACK, 600, 450)
            pygame.display.update()
            play_game()
        #check if all attempts have been used and some letters still not guessed
        if attempts == 0:
            write(f"Game over! The word was: {guess_words}", text_font, BLACK, 600, 450)
            pygame.display.update()
            play_game()
        #main game loop
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

        
