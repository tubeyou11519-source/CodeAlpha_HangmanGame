import random

WORDS = ["python", "developer", "github", "engineer", "keyboard"]
MAX_WRONG_GUESSES = 6

def choose_word():
    return random.choice(WORDS)

def display_progress(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def play():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(f"\nWord: {display_progress(word, guessed_letters)}")
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nYou win! The word was '{word}'.")
            return

    print(f"\nGame over! The word was '{word}'.")

def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()