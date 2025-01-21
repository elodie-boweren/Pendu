import pygame
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (190, 190, 190)
PINK = (255, 192, 203)

# Screen setup
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hangman Game")

# Font
font = pygame.font.SysFont("monospace", 40)
small_font = pygame.font.SysFont("monospace", 20)

# Keyboard mapping
dictionary_keyboard = {
    K_a: "a", K_b: "b", K_c: "c", K_d: "d", K_e: "e", K_f: "f", K_g: "g",
    K_h: "h", K_i: "i", K_j: "j", K_k: "k", K_l: "l", K_m: "m", K_n: "n",
    K_o: "o", K_p: "p", K_q: "q", K_r: "r", K_s: "s", K_t: "t", K_u: "u",
    K_v: "v", K_w: "w", K_x: "x", K_y: "y", K_z: "z"
}

# Hangman drawing
def draw_hangman(attempts):
    if attempts <= 6:
        pygame.draw.line(window, BLACK, [30, 400], [290, 400], 7)
    if attempts <= 5:
        pygame.draw.line(window, BLACK, [60, 35], [60, 400], 7)
    if attempts <= 4:
        pygame.draw.line(window, BLACK, [60, 38], [200, 38], 7)
    if attempts <= 3:
        pygame.draw.line(window, BLACK, [200, 35], [200, 80], 7)
    if attempts <= 2:
        pygame.draw.circle(window, PINK, [200, 115], 35, 0)
        pygame.draw.circle(window, BLACK, [200, 115], 35, 7)
    if attempts <= 1:
        pygame.draw.line(window, BLACK, [200, 150], [200, 250], 7)
        pygame.draw.line(window, BLACK, [160, 160], [200, 200], 7)
        pygame.draw.line(window, BLACK, [240, 160], [200, 200], 7)
    if attempts == 0:
        pygame.draw.line(window, BLACK, [160, 290], [200, 250], 7)
        pygame.draw.line(window, BLACK, [240, 290], [200, 250], 7)

# Load words
def load_words():
    try:
        with open("words.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print("Error: 'words.txt' not found!")
        return []

# Add a word
def add_word():
    word = input("Enter a new word to add: ").lower()
    if not word.isalpha():
        print("Only letters are allowed.")
        return
    with open("words.txt", "a") as f:
        f.write(word + "\n")
    print(f"'{word}' has been added to the word list.")

# Main game function
def play_game():
    words = load_words()
    if not words:
        print("No words available to play.")
        return

    word = random.choice(words).lower()
    guessed = set()
    correct = set()
    attempts = 7

    running = True
    while running:
        window.fill(WHITE)
        draw_hangman(attempts)

        # Display word progress
        display_word = " ".join([letter if letter in correct else "_" for letter in word])
        word_text = font.render(display_word, True, BLACK)
        window.blit(word_text, (50, 300))

        # Display guessed letters
        guessed_text = small_font.render(f"Guessed: {', '.join(sorted(guessed))}", True, BLACK)
        window.blit(guessed_text, (50, 350))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key in dictionary_keyboard:
                    letter = dictionary_keyboard[event.key]
                    if letter in guessed:
                        print("You already guessed that letter.")
                        continue

                    guessed.add(letter)
                    if letter in word:
                        correct.add(letter)
                    else:
                        attempts -= 1

                    # Check win condition
                    if set(word) == correct:
                        print("You win!")
                        running = False

                    # Check lose condition
                    if attempts == 0:
                        print(f"You lose! The word was: {word}")
                        running = False

# Menu
def menu():
    while True:
        choice = input("\n1. Play\n2. Add a word\n3. Exit\nYour choice: ")
        if choice == "1":
            play_game()
        elif choice == "2":
            add_word()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
