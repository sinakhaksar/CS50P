# https://cs50.harvard.edu/python/2022/psets/2/nutrition/


Fruits = [
    {'name': 'Apple', 'weight': 242, 'calories': 130},
    {'name': 'Avocado', 'weight': 30, 'calories': 50},
    {'name': 'Banana', 'weight': 126, 'calories': 110},
    {'name': 'Cantaloupe', 'weight': 134, 'calories': 50},
    {'name': 'Grapefruit', 'weight': 154 , 'calories': 60},
    {'name': 'Grapes', 'weight': 126, 'calories': 90},
    {'name': 'Honeydew ', 'weight': 134, 'calories': 50},
    {'name': 'lemon', 'weight': 58, 'calories': 15},
    {'name': 'Lime', 'weight': 67, 'calories': 20},
    {'name': 'Nectarine', 'weight': 140, 'calories': 60},
    {'name': 'Orange', 'weight': 154, 'calories': 80},
    {'name': 'Peach', 'weight': 147, 'calories': 60},
    {'name': 'Pear', 'weight': 166, 'calories': 100},
    {'name': 'Pineapple', 'weight': 112, 'calories': 50},
    {'name': 'Plums', 'weight': 151, 'calories': 70},
    {'name': 'Strawberries', 'weight': 147, 'calories': 50},
    {'name': 'Sweet Cherries', 'weight': 140, 'calories': 100},
    {'name': 'Tangerine', 'weight': 109, 'calories': 50},
    {'name': 'Watermelon', 'weight': 280, 'calories': 80},
    ]

def main():
    item = input('Item: ').capitalize().strip()

    for fruit in Fruits : 
        if fruit['name'] == item:
            print('Calories:', fruit['calories'])

if __name__ == "__main__":
    main()


"""
How to Test
Here’s how to test your code manually:

Run your program with python nutrition.py. Type Apple and press Enter. Your program should output:
Calories: 130   
Run your program with python nutrition.py. Type Avocado and press Enter. Your program should output:
Calories: 50
Run your program with python nutrition.py. Type Sweet Cherries and press Enter. Your program should output
Calories: 100
Run your program with python nutrition.py. Type Tomato and press Enter. Your program should output nothing.

"""