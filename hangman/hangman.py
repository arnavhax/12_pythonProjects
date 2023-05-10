import random
from hangman.words import words
import string
def get_word():
    word=random.choice(words)
    while('-' in word or ' ' in word or len(word)>6):
        word=random.choice(words)
    return word

def hangman():
    lives=10
    word=get_word()
    letters=set(word)
    guessed_letters=set()
    alphabet=string.ascii_letters
    while(letters!=guessed_letters and lives>0):
        guess=['-' if letter not in guessed_letters else letter for letter in word ]
        print(' '.join(guess))
        print(f'No. of lives remaining is {lives}')
        alpha=input("Guess an alphabet\n")
        if(alpha not in alphabet):
            print("Invalid input guess again")
        elif(alpha in guessed_letters):
            print("Already guessed try again\n")
        else:
            if(alpha in letters):
                guessed_letters.add(alpha)
            else:
                lives-=1
    print(f'The word is {word}')
flag=True
while(flag):
    hangman()
    inp=input('Do you wanna play again(y for yes)')
    if(inp=='y'):
        hangman()
    else:
        flag=False
print('Thankyou\n')    
