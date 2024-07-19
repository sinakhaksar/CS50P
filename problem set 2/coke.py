#https://cs50.harvard.edu/python/2022/psets/2/coke/
money = 0

while money <= 50 : 
    print('Amount Due:',abs(money-50))
    user_input = int(input('Insert Coin: '))
    
    if user_input in [25, 10, 5]:
        money += user_input


print('Change Ownd:',money-50)

"""
How to Test
Here’s how to test your code manually:

Run your program with python coke.py. At your Insert Coin: prompt, type 25 and press Enter. Your program should output:
Amount Due: 25   
and continue prompting the user for coins.

Run your program with python coke.py. At your Insert Coin: prompt, type 10 and press Enter. Your program should output:
Amount Due: 40
and continue prompting the user for coins.

Run your program with python coke.py. At your Insert Coin: prompt, type 5 and press Enter. Your program should output:
Amount Due: 45
and continue prompting the user for coins.

Run your program with python coke.py. At your Insert Coin: prompt, type 30 and press Enter. Your program should output:
Amount Due: 50
because the machine doesn’t accept 30-cent coins! Your program should then continue prompting the user for coins.

Run your program with python coke.py. At your Insert Coin: prompt, type 25 and press Enter, then type 25 again and press Enter. Your program should halt and display:
Change Owed: 0
Run your program with python coke.py. At your Insert Coin: prompt, type 25 and press Enter, then type 10 and press Enter. Type 25 again and press Enter, after which your program should halt and display:
Change Owed: 10
"""