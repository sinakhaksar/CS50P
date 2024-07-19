# https://cs50.harvard.edu/python/2022/psets/3/taqueria/

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
while True:
    order= input('Item: ').title().strip()
    if order == 'Break':
        break
    try:
        total += menu.get(order)
    except TypeError :
        continue
    print(total)



"""
How to Test
Here’s how to test your code manually:

Run your program with python taqueria.py. Type Taco and press Enter, then type Taco again and press Enter. Your program should output:
Total: $6.00  
and continue prompting the user until they input control-d.

Run your program with python taqueria.py. Type Baja Taco and press Enter, then type Tortilla Salad and press enter. Your program should output:
Total: $12.25
and continue prompting the user until they input control-d.

Run your program with python taqueria.py. Type Burger and press Enter. Your program should reprompt the user.
"""