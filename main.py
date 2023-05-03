import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
            guess=int(input(f'Guess a number between 1 and {x}\n'))
            if(guess<random_number):
                print("Too low guess again\n")
            elif(guess>random_number):
                print("Too high guess again\n")
            else:
                print(f'Yes you got it right the number is {random_number}\n')

def computer_guess(x):
    feedback=''
    low=1
    high=x
    
    while feedback !='c':
        if(low!=high):
            guess=random.randint(low,high)
        else:
            guess=low
        print(guess)
        feedback=input('Is the number too high(H), too low(L) or Correct(C)\n').lower()
        if(feedback=='l'):
            low =guess+1
        elif(feedback=='h'):
             high=guess-1
    print(f'I guessed it right, the number is{guess}\n')

# guess(10)
computer_guess(1000)