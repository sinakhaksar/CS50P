# https://cs50.harvard.edu/python/2022/psets/3/fuel/

def fraction():
    try:
        num1,num2 = input('fraction: ').split('/')
        num1,num2 = int(num1), int(num2)
    except ValueError: # If input is not in the correct format, retry
        fraction()
        return 
    try:
        percent = round((num1 *100 )/ num2)
    except ZeroDivisionError: # If denominator is zero, retry
        fraction()
        return
    
    # No exception occurred, proceed with the calculation
    else:
        # show cases 
        if percent > 100 : 
            fraction() 
        elif percent == 100 : 
            print('F')
        elif percent == 0 :
            print('E')    
        else:  
            print(percent, "%",sep='')


if __name__ == "__main__":
    fraction()

"""
How to Test
Here’s how to test your code manually:

Run your program with python fuel.py. Type 3/4 and press Enter. Your program should output:
75% 
Run your program with python fuel.py. Type 1/4 and press Enter. Your program should output:
25%
Run your program with python fuel.py. Type 4/4 and press Enter. Your program should output:
F
Run your program with python fuel.py. Type 0/4 and press Enter. Your program should output:
E
Run your program with python fuel.py. Type 4/0 and press Enter. Your program should handle a ZeroDivisionError and prompt the user again.
Run your program with python fuel.py. Type three/four and press Enter. Your program should handle a ValueError and prompt the user again.
Run your program with python fuel.py. Type 1.5/3 and press Enter. Your program should handle a ValueError and prompt the user again.
Run your program with python fuel.py. Type 5/4 and press Enter. Your program should prompt the user again.
"""