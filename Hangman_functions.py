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

screen = pygame.display.set_mode((1000, 600))
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


def draw_hangman(attempts):
    if attempts <= 6:
        pygame.draw.line(screen, (BLACK), [30, 400], [290, 400], 10)
        pygame.draw.line(screen, (BLACK), [60, 35], [60, 400], 10)
        pygame.draw.line(screen, (BLACK), [60, 38], [200, 38], 10)
        pygame.draw.line(screen, (BLACK), [60, 80], [115, 38], 10)
        pygame.draw.line(screen, (BLACK), [200, 35], [200, 80], 10)
    if attempts <= 5:
        pygame.draw.circle(screen, (PINK), [201,115], 35,0)
        pygame.draw.circle(screen, (BLACK), [201,115], 35,10)
    if attempts <= 4:
        pygame.draw.line(screen, (BLACK), [200, 150], [200, 250], 10) 
    if attempts <= 3:
        pygame.draw.line(screen, (BLACK), [160, 160], [200, 200], 10)
    if attempts <= 2:
        pygame.draw.line(screen, (BLACK), [240, 160], [200, 200], 10)
    if attempts <= 1:
        pygame.draw.line(screen, (BLACK), [160, 290], [200, 250], 10)
    if attempts <= 0:
        pygame.draw.line(screen, (BLACK), [240, 290], [200, 250], 10)
        

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
    run_game = True
    words = ""
    words = random.choice(open("words.txt").read().splitlines())
    guess_words = words
    found_letters = []
    attempts = 7

    while run_game :
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
            pygame.time.delay(1000)
            run_game = False
            return True
        
        if attempts == 0:
            write(f"Perdu ! Le mot était: {guess_words}", text_font, BLACK, 600, 450)
            pygame.time.delay(1000)
            pygame.display.update()
            
            run_game = False
            return True
            

        for event in pygame.event.get():
            if event.type == QUIT:
                run_game = False
            if event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key)
                    if letter not in found_letters:
                        found_letters.append(letter)
                        if letter not in guess_words:
                            attempts -= 1
    
        pygame.display.update()
    
    pygame.quit()

        
