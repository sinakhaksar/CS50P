
#https://cs50.harvard.edu/python/2022/psets/0/tip/

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.strip('$')
    return float(d)


def percent_to_float(p):
    p =p.strip('%')
    
    return (float(p)/100)


main()

"""
How to Test
Here’s how to test your code manually:

Run your program with python tip.py. Type $50.00 and press Enter. Then, type 15% and press Enter. Your program should output:
Leave $7.50    
Run your program with python tip.py. Type $100.00 and press Enter. Then, type 18% and press Enter. Your program should output:
Leave $18.00
Run your program with python tip.py. Type $15.00 and press Enter. Then, type 25% and press Enter. Your program should output
Leave $3.75
"""