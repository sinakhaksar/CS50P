#https://cs50.harvard.edu/python/2022/psets/1/interpreter/

def interpreter(num1,opration,num2):

    num1,num2 = int(num1),int(num2)
    match opration : 
        case '+':
            return(num1 + num2)
        case '-':
            return(num1 - num2)
        case '/':
            return(num1 / num2)
        case '*':
            return(num1 * num2)

def main():
        
    while True:
        try:
            num1,opration,num2 = input('Expression: ').strip().split(" ")
            print(f'{float(interpreter(num1, opration, num2)):.1f}')
        except ValueError:
            print('ERORR!\nformat:\nnumber space opration space number\n1 + 3')

if __name__ == "__main__":
    main()

"""
How to Test
Here’s how to test your code manually:

Run your program with python interpreter.py. Type 1 + 1 and press Enter. Your program should output:
2.0 
Run your program with python interpreter.py. Type 2 - 3 and press Enter. Your program should output:
-1.0
Run your program with python interpreter.py. Type 2 * 2 and press Enter. Your program should output
4.0
Run your program with python interpreter.py. Type 50 / 5 and press Enter. Your program should output
10.0
"""