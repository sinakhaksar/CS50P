# https://cs50.harvard.edu/python/2022/psets/4/professor/
import random

score = 0 
wrongans = 0


def main():
    global score
    level = get_level()
    
    for _ in range(10):
        a,b = generate_integer(level=level), generate_integer(level=level)
        checker(a,b)

    print('socre:',score)


def checker(a, b):
    global wrongans, score

    print(f'{a} + {b} = ',end='')
    ansUser = input().strip()

    if ansUser == str(a+b) : 
        score +=1
        wrongans = 0
    else:
        wrongans += 1
        print('EEE')
        if wrongans == 3 : 
            print(f'{a} + {b} = {a+b}')
            wrongans = 0
            return
        
        checker(a,b)


def get_level():
    level = input('Level: ')
    
    if level not in ['1', '2', '3']:
        return get_level()
    
    return int(level)


def generate_integer(level):
    ndigit = 10 ** level
    return random.randint((ndigit/10), ndigit-1)


if __name__ == "__main__":
    main()


"""
How to Test
Here’s how to test your code manually:

Run your program with python professor.py. Type -1 and press Enter. Your program should reprompt you:
Level:   
Run your program with python professor.py. Type 4 and press Enter. Your program should reprompt you:
Level:   
Run your program with python professor.py. Type 1 and press Enter. Your program should begin posing addition problems with positive, single-digit integers. For example:
6 + 6 =    
Your program should output 10 distinct problems before printing the number of questions you answered correctly and exiting.

Run your program with python professor.py. Type 1 and press Enter. Answer the first question incorrectly. Your program should output:
EEE
before reprompting you with the same question.

Run your program with python professor.py. Type 1 and press Enter. Answer the first question incorrectly, three times. Your program should output the correct answer. For example:
6 + 6 = 12
and then move on to another question. Answer the remaining questions correctly. Your program should output a score of 9.

Run your program with python professor.py. Type 1 and press Enter. Answer all 10 questions correctly. Your program should output a score of 10.
"""