# https://cs50.harvard.edu/python/2022/psets/4/figlet/
from pyfiglet import Figlet
import sys, random

f = Figlet()

def figletfunc(text):
    font =random.choice(f.getFonts())
    f.setFont(font=font)
    
    sys.exit(f.renderText(text))


def main():

    if len(sys.argv) in [1,3]:
        if len(sys.argv) == 1 : 
            figletfunc(userinput())

        elif sys.argv[1] in ['-f', '--font']: 
            font_checker(sys.argv[-1],userinput())

        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')

def font_checker(font,text):
    if font in f.getFonts():
        f.setFont(font=font)
        sys.exit(f.renderText(text=text))
    
    sys.exit('Invalid usage')

def userinput():
    return input('Input: ')

if __name__ == '__main__':
    main()

"""
How to Test
Here’s how to test your code manually:

Run your program with python figlet.py test. Your program should exit via sys.exit and print an error message:
Invalid usage
Run your program with python figlet.py -a slant. Your program should exit via sys.exit and print an error message:
Invalid usage
Run your program with python figlet.py -f invalid_font. Your program should exit via sys.exit and print an error message:
Invalid usage
Run your program with python figlet.py -f slant. Type CS50. Your program should print the following:
   ___________ __________ 
  / ____/ ___// ____/ __ \
 / /    \__ \/___ \/ / / /
/ /___ ___/ /___/ / /_/ / 
\____//____/_____/\____/  
Run your program with python figlet.py -f rectangles. Type Hello, world. Your program should print the following:
 _____     _ _                        _   _ 
|  |  |___| | |___      _ _ _ ___ ___| |_| |
|     | -_| | | . |_   | | | | . |  _| | . |
|__|__|___|_|_|___| |  |_____|___|_| |_|___|
                  |_|                       
Run your program with python figlet.py -f alphabet. Type Moo. Your program should print the following:
M   M         
MM MM         
M M M ooo ooo 
M   M o o o o 
M   M ooo ooo      
"""