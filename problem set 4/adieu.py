# https://cs50.harvard.edu/python/2022/psets/4/adieu/

def greeting():
    user_Input = ['']

    while user_Input[-1] != 'end':
        
        user_Input.append(input('Name: '))
    
    name = ''
    text = 'Adieu, adieu, to'
    user_Input = user_Input[1:-1]
    lenn = len(user_Input)
    
    if lenn == 1 :
        name = user_Input[0] 
        print(text, name)

    elif  lenn == 2: 
        name = f' {user_Input[0]} and {user_Input[1]}' 
        print(text + name)

    elif lenn >= 3:
        for _ in user_Input[:-1]:
            name += _+', '
        name += 'and ' + user_Input[-1]
        print(text , name)

if __name__ == "__main__":
    greeting()

"""
How to Test
Here’s how to test your code manually:

Run your program with python adieu.py. Type Liesl and press Enter, followed by control-d. Your program should output:
Adieu, adieu, to Liesl 
Run your program with python adieu.py. Type Liesl and press Enter, then type Friedrich and press Enter, followed by control-d. Your program should output:
Adieu, adieu, to Liesl and Friedrich
Run your program with python adieu.py. Type Liesl and press Enter, then type Friedrich and press Enter. Now type Louisa and press Enter, followed by control-d. Your program should output:
Adieu, adieu, to Liesl, Friedrich, and Louisa
"""