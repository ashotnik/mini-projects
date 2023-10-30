#!/usr/bin/python3
import random

# List where a word is chosen
word_list = ["apple", "banana", "cherry", "potato", "tomato", "grape"]

# Hangman death variants
hangman_deads = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =======""",
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =======""",
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =======""",
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =======""",
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =======""",
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =======""",
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =======""",
]


# Get a random word from the list
def random_word(words):
    return random.choice(words)

# Display a found letter
def display_word(word, guess, hang, uncorrect):
    true_answer = ""
    for letter in word:
        if letter in guess:
            true_answer += letter
        else:
            true_answer += "-"
    if "-" not in true_answer:
        return True
    print(true_answer)
    print(hang[uncorrect])

# Play the game
def play(word, hangman):
    guessed_letters = []
    uncorrect_answers = 0
    win = display_word(word, guessed_letters, hangman, uncorrect_answers)
    while True:
        if win:
            print("You win! The correct answer is %s" % word)
            break
        letter = input("Enter a letter: ")
        if letter in guessed_letters:
            print("Letter is guessed")
        elif letter not in word:
            uncorrect_answers += 1
            if uncorrect_answers == 6:
                print(hangman[uncorrect_answers])
                print("Game over! The correct answer is %s" % word)
                break
        guessed_letters.append(letter)
        win = display_word(word, guessed_letters, hangman, uncorrect_answers)

def main():
    words = random_word(word_list)
    play(words, hangman_deads)

if __name__ == "__main__":
    main()
