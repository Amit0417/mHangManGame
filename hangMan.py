import random
#from rWords import rwords
import string

user = input("welcome to hungman game\nEnter Your Name -> ")
rwords=[]
print ("Hello ! ",user,"\nI'll choose a word given by you\nthen you have to guess that word ")
print("Enter 10 words that you like and I will make a list of It :")

for i in range(11):
    temp = input("enter word :")
    rwords.append(temp)

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

    lives = 10 # chance's of trying while guessing the letter

    # for user input
    while len(w_letter) > 0 and lives > 0:
        # guessed letters
        # ' '.join([x,ab,y,yz]) ---> 'x ab y yz'
        print ('You have', lives  ,' lives left and you have used these letter: '  ,' '.join(guessed_letter))
        # current word is
        list_words = [letter if letter in guessed_letter else '_' for letter in word]
        print ('Current word is : '  ,' '.join(list_words))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alpha - guessed_letter:
            guessed_letter.add(user_letter)
            if user_letter in w_letter:
                w_letter.remove(user_letter)
            else:
                lives = lives-1 # for reducing the chance's of trying if choose wrong letter
                print("This letter is not in the word")

        elif user_letter in guessed_letter:
            print("You have already used that character, Please try again with another character")

        else:
            print("Invalid Character, Please try again with another character")

    # this loop will execute only when len(w_letter) == 0
    if lives == 0:
        print("Sorry! you have died, The word was ", word)
    else:
        print("Congratulations!",user," You have gussed the word: " , word)

hangman()
