
#https://cs50.harvard.edu/python/2022/psets/1/bank/


def greeting():
    grettingMessage = input(': ').strip().lower().split()
    
    if grettingMessage[0] == 'hello': 
        print('$0')
    elif grettingMessage[0][0] =='h': 
        print('$20')
    else:
        print('$100')

greeting()


"""
How to Test
Here’s how to test your code manually:

Run your program with python bank.py. Type Hello and press Enter. Your program should output:
$0 
Run your program with python bank.py. Type Hello, Newman and press Enter. Your program should output:
$0
Run your program with python bank.py. Type How you doing? and press Enter. Your program should output
$20
Run your program with python bank.py. Type What's happening? and press Enter. Your program should output
$100
"""