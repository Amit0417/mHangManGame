import random
from rWords import rwords
import string


def choose_word(rwords):
    # randomly choose any word from the list from rWords file
    word = random.choice(rwords)
    while "_" in word or " " in word:
        word = random.choice(rwords)

    return word.upper()


def hangman():
    word = choose_word(rwords)
    w_letter = set(word)  # for letters in words
    alpha = set(string.ascii_uppercase)
    guessed_letter = set()  # already guessed letters

    # for user input
    while len(w_letter) > 0:
        # guessed letters
        # ' '.join([x,ab,y,yz]) ---> 'x ab y yz'
        print ('You have used these letter: '  ,' '.join(guessed_letter))
        # current word is
        list_words = [letter if letter in guessed_letter else '_' for letter in word]
        print ('Current word is : '  ,' '.join(list_words))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alpha - guessed_letter:
            guessed_letter.add(user_letter)
            if user_letter in w_letter:
                w_letter.remove(user_letter)

        elif user_letter in guessed_letter:
            print("You have already used that character, Please try again with another character")

        else:
            print("Invalid Character, Please try again with another character")

    # this loop will execute only when len(w_letter) == 0
    if len(w_letter) == 0:
        print(" You have gussed the word: " , word)

hangman()