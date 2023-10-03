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

#Display a finded letter
def display_word(word,guess,hang,un):

    true_anwser=""
    for i in word:
        if i in guess:
            true_anwser+=i
        else:
            true_anwser+="-"
    if not "-" in true_anwser:
        return True
    print(true_anwser)
    print(hang[un])
            



#Play game
def play(word,hangman):
    guessed_letter=[]
    uncorrect_anwsers=0
    win=display_word(word,guessed_letter,hangman,uncorrect_anwsers)
    while True:
        if win==True:
            print("You win! correct anwser is %a" %(word))
            break
        letter=input("Enter a letter: ")
        if letter in guessed_letter:
            print("Letter is Guessed")
        elif not letter in word: 
            uncorrect_anwsers+=1
            if uncorrect_anwsers==6:
                print(hangman[uncorrect_anwsers])
                print("Game over! Correct anwser is %a" %(word))
                break
        guessed_letter.append(letter)
        win=display_word(word,guessed_letter,hangman,uncorrect_anwsers)



def main():
    words=random_word(word_list)
    play(words,hangman_art)
    
main()