# https://cs50.harvard.edu/python/2022/psets/3/grocery/

data = {}

state = True
while state:
    try: 
        ainput = input('>').lower().strip()
    except EOFError:
        ainput = input('>').lower().strip()
        break

    if ainput == 'end':
        state = False    
    elif ainput in data.keys():
        data[ainput] += 1
    else:
        data[ainput] = 1


for i in sorted(data):
    print(data[i], i.capitalize())
    

"""
How to Test
Here’s how to test your code manually:

Run your program with python grocery.py. Type mango and press Enter, then type strawberry and press Enter, followed by control-d. Your program should output:
1 MANGO
1 STRAWBERRY
Run your program with python grocery.py. Type milk and press Enter, then type milk again and press Enter, followed by control-d. Your program should output:
2 MILK
Run your program with python grocery.py. Type tortilla and press Enter, then type sweet potato and press Enter, followed by control-d. Your program should output:
1 SWEET POTATO
1 TORTILLA
"""