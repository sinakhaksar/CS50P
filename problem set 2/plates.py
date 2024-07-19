#https://cs50.harvard.edu/python/2022/psets/2/plates/

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return length(s) and letter(s) and valid_input(s)


def length(s:str):
    if len(s) not in range(2,7): 
        return False
    elif s[0].isdigit() or s[1].isdigit():
        return False
    else:
        return True
    

def letter(s:str):  
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i+1].isalpha():
            return False

    for i in range(len(s)-1):
        if s[i].isdigit() and s[i] == '0':
            return False
    return True
        

def valid_input(s:str):
    for i in s : 
        if i.isalnum() == False:
            return False # Check if all characters are alphanumeric
    return True

if __name__ == "__main__":
    main()

"""
How to Test
Here’s how to test your code manually:

Run your program with python plates.py. Type CS50 and press Enter. Your program should output:
Valid
Run your program with python plates.py. Type CS05 and press Enter. Your program should output:
Invalid
Run your program with python plates.py. Type CS50P and press Enter. Your program should output
Invalid
Run your program with python plates.py. Type PI3.14 and press Enter. Your program should output
Invalid
Run your program with python plates.py. Type H and press Enter. Your program should output
Invalid
Run your program with python plates.py. Type OUTATIME and press Enter. Your program should output
Invalid
"""