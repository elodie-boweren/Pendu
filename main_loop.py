import pygame
from pygame.locals import *
import random
import json
from Hangman_functions import *

pygame.init()

#colors used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (190,190,190)
PINK = (255,192,203)

#screen and text formats
screen = pygame.display.set_mode((1000, 800))
title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 15)

# Load JSON file for words
with open("words_groups.json", "r") as file:
    words_data = json.load(file)

def difficulty_menu():
    """Display the difficulty selection menu and return the player's choice."""
    screen.fill(WHITE)
    text("Select a difficulty level:", title_font, BLACK, 400, 150)
    text("1 = Easy", text_font, BLACK, 430, 250)
    text("2 = Medium", text_font, BLACK, 430, 300)
    text("3 = Hard", text_font, BLACK, 430, 350)
    text("Type your choice", text_font, BLACK, 430, 400)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return None
            if event.type == KEYDOWN:
                if event.key == K_1:
                    return "easy"
                elif event.key == K_2:
                    return "medium"
                elif event.key == K_3:
                    return "hard"


def play_game_with_difficulty():
    """Play the game with words based on the selected difficulty."""
    difficulty = difficulty_menu()
    if not difficulty:
        return False

    # Get words for the selected difficulty
    words_list = next(
        (level["words"] for level in words_data["difficulty_levels"] if level["level"] == difficulty),
        []
    )

    if not words_list:
        print("No words found for the selected difficulty.")
        return False

    global guess_words, found_letters, attempts
    run_game = True
    guess_words = random.choice(words_list)
    found_letters = []
    attempts = 7

    while run_game:
        screen.fill(WHITE)
        letters_shown = " ".join([letter if letter in found_letters else "_" for letter in guess_words])
        write(letters_shown, text_font, BLACK, 600, 300)
        write(f"Attempts remaining: {attempts}", text_font, BLACK, 600, 350)

        letters_already_tried = " ".join(found_letters)
        write(f"Letters tried: ", text_font, BLACK, 600, 400)
        write(f"{letters_already_tried}", text_font, BLACK, 600, 450)
        draw_hangman(attempts)

        if all([letter in found_letters for letter in guess_words]):
            write("Congrats! You won!", text_font, BLACK, 600, 500)
            pygame.display.update()
            pygame.time.delay(3000)
            run_game = False
            return True

        if attempts == 0:
            write(f"Game over! The word was: {guess_words}", text_font, BLACK, 600, 500)
            pygame.display.update()
            pygame.time.delay(3000)
            run_game = False
            return True

        for event in pygame.event.get():
            if event.type == QUIT:
                run_game = False
            if event.type == KEYDOWN:
                if event.key >= K_a and event.key <= K_z:
                    letter = chr(event.key)
                    if letter not in found_letters:
                        found_letters.append(letter)
                        if letter not in guess_words:
                            attempts -= 1

        pygame.display.update()

    pygame.quit()


# Main loop
run = True
while run:
    key = pygame.key.get_pressed()
    menu()

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if key[K_1]:
            run = play_game_with_difficulty()
        elif key[K_2]:
            add_word()
        elif key[K_3]:
            run = False

    pygame.display.update()