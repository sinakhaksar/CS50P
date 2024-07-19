# https://cs50.harvard.edu/python/2022/psets/4/game/

import random


def returnlevel():
    level= input('level: ')
    try:
        level = int(level)
    except ValueError:
        return returnlevel()
        
    if level < 0:
        return returnlevel()   
    return level    


def game():
    level = returnlevel() + 1
    target = random.choice([x for x in range(1,level)])

    checker(target=target)
    

def checker(target):
    try:
        guess = int(input('Guess: '))
    except ValueError:
        return checker(target)
    
    if guess == target:
        print("just right!")
        return
    elif guess > target: 
        print('Too large!')
    elif guess < target:
        print('Too samll!')
    else:
        print('Invalid input. Please enter a number.')

    checker(target=target)

    
def aditionalData():
    # i could add a percent before each try and like if
    # level is 100 before the First Guess the chnce is 1%
    # after eluminating each number the chance incrises ...   
    ...

game()


"""
How to Test
Here’s how to test your code manually:

Run your program with python game.py. Type cat at a prompt that says Level: and press Enter. Your program should reprompt you:
Level:   
Run your program with python game.py. Type -1 at a prompt that says Level: and press Enter. Your program should reprompt you:
Level:   
Run your program with python game.py. Type 10 at a prompt that says Level: and press Enter. Your program should now be ready to accept guesses:
Guess:   
Run your program with python game.py. Type 10 at a prompt that says Level: and press Enter. Then type cat. Your program should reprompt you:
Guess:   
Run your program with python game.py. Type 10 at a prompt that says Level: and press Enter. Then type -1. Your program should reprompt you:
Guess:   
Run your program with python game.py. Type 1 at a prompt that says Level: and press Enter. Then type 1. Your program should output:
Just right!  
There’s only one possible number the answer could be!

Run your program with python game.py. Type 10 at a prompt that says Level: and press Enter. Then type 100. Your program should output:
Too large!  
Looks like you’re guessing outside the range you specified.

Run your program with python game.py. Type 10000 at a prompt that says Level: and press Enter. Then type 1. Your program should output:
Too small!  
"""