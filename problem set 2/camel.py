# https://cs50.harvard.edu/python/2022/psets/2/camel/


def main():

    camelCase =  input('camelCase: ')
    print(convert(camelCase))

def convert(camelCase):
    for char in camelCase:
        if char == char.capitalize():
            camelCase = camelCase.replace(char, f'_{char.lower()}') 
    return(camelCase)

if __name__ == "__main__":
    main()


"""
How to Test
Here’s how to test your code manually:

Run your program with python camel.py. Type name and press Enter. Your program should output:
name   
Run your program with python camel.py. Type firstName and press Enter. Your program should output:
first_name
Run your program with python camel.py. Type preferredFirstName and press Enter. Your program should output:
preferred_first_name

"""