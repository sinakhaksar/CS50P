#https://cs50.harvard.edu/python/2022/psets/2/twttr/

user_input = input('input: ')

valves = ['a','A', 'e', 'E','i', 'I', 'o', 'O', 'u', 'U']


for char in user_input : 
    if char in valves : 
        user_input = user_input.replace(char,'')

print(user_input)


"""
How to Test
Here’s how to test your code manually:

Run your program with python twttr.py. Type Twitter and press Enter. Your program should output:
Twttr   
Run your program with python twttr.py. Type What's your name? and press Enter. Your program should output:
Wht's yr nm?
Run your program with python twttr.py. Type CS50 and press Enter. Your program should output
CS50
"""