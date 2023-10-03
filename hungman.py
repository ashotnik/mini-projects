#!/usr/bin/python3
import random

#List where choose a word
word_list= ["apple", "banana", "cherry", "potato", "tomato", "grape"]

#Hangman deads variant
hangman_art = [
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

#Get Random word from list
def random_word(words):
    return random.choice(words)

#Display a word count and Welcome
# def display_word(word):
    
   
#     return cnt_w

#Play game
def play(word):
    print("Hello, Welcome to Hangman")
    cnt_w=""
    for i in range(len(word)):
        cnt_w+="-"
    print(cnt_w)
    while True:
        dd=""
        letter=input("Enter a letter: ")
        for i in word:
            if letter==i:
                dd+=letter
            else:
                dd+="-"
        print(dd)



def main():
    words=random_word(word_list)
    # letter_cnt=display_word(words)
    play(words)
    
main()