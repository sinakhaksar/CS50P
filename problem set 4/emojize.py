# https://cs50.harvard.edu/python/2022/psets/4/emojize/
import emoji

def emojiz():
    user_Input = input('Input: ')
    return emoji.emojize(user_Input, language='alias')


print(emojiz())

"""
How to Test
Here’s how to test your code manually:

Run your program with python emojize.py. Type :1st_place_medal: and press Enter. Your program should output:
Output: 🥇
Run your program with python emojize.py. Type :money_bag: and press Enter. Your program should output:
Output: 💰
Run your program with python emojize.py. Type :smile_cat: and press Enter. Your program should output:
Output: 😸
"""