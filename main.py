import random

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def menu():
    return input("\nWhat do you want to do ? : \n 1. Play \n 2. Add word \n 3. Exit \nYour choice: ")

def game():
    word_choice = random.choice(open('words.txt').read().splitlines())

    solution = word_choice.lower()
    solution_display = word_choice
    attempts = 7
    display = ""
    found_letters = ""
    tried_letters = set()  #keeps all the letters already tried
    for l in solution:
        display = display + "_"
    print(">> Welcome to the hangman game <<")

    while attempts > 0:
        #updates display to show the word
        display = ""
        for i,x in enumerate(solution):
            if x in found_letters:
                display += solution_display[i]
            else:
                display += "_"
        
        if "_" not in display:
            print(f">>> You Win ! <<< \nThe word was {word_choice}")
            play_again = input("Type P to play again and E to exit the game: ")
            if play_again.upper() == "P":
                game()
            return

        print("Word to guess : ", display)
        print(f"Letters already tried: {', '.join(sorted(tried_letters))}")  #shows the letters already tried
        proposal = input("Propose a letter : ")[0:1].lower()
        
        #checks if it's a letter
        if proposal not in alphabet:
            print("-> Please make sure to enter a letter")
            continue #goes back to the start of the loop without counting it as an attempt

        #checks if the letter has already been tried
        if proposal in tried_letters:
            print("-> You already tried this letter! Choose another one.")
            continue  

        tried_letters.add(proposal)  #adds new letter to the letters already tried

        if proposal in solution:
            found_letters = found_letters + proposal
            print("-> Great !")
        else:
            attempts = attempts - 1 
            print("-> Nope")

        if attempts <= 6:
            print(" ==========Y=")
        if attempts <= 5:
            print(" ||/       | ")
        if attempts <= 4:
            print(" ||        0 ")
        if attempts <= 3:
            print(" ||       /|\ ")
        if attempts <= 2:
            print(" ||        | ")
        if attempts <= 1:
            print("/||       / \  ")
        if attempts == 0:
            print("==============\n")
            print(f"You lost! The word was: {solution}")
            play_again = input("Type P to play again and E to exit the game: ")
            if play_again.upper() == "P":
                game()


def add_word():
    word = input("\nAdd a word to the game : ").lower()
    
    word_is_valid = True
    for letter in word:
        if letter not in alphabet:
            word_is_valid = False
            break

    if not word_is_valid:
        print("Please make sure to enter a word containing only letters")
        return
            
    with open('words.txt', 'r') as f:
        if word in f.read().splitlines():
            print(f"The word '{word}' is already in the game!")
            return
        

    with open('words.txt', 'a') as f:
        f.write('\n' + word)
    print(f"The word '{word}' has been added to the game")

def main():
    while True:
        choice = menu()
        if choice == "1":
            try:
                game()
                continue
            except KeyboardInterrupt:
                continue
        
        elif choice == "2":
            try:
                add_word()
                continue
            except KeyboardInterrupt:
                continue

        elif choice == "3":
                print ("Goodbye !")
                break
            
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()