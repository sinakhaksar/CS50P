#https://cs50.harvard.edu/python/2022/psets/1/meal/


def main():
    userInput = input('what time is it? ').strip()

    if 'exit' in userInput:
        quit()
    try: #checks that a time is enterd  
        hours,minutes = userInput.split(':')
        checker(int(hours), int(minutes)) #values are provided from checker 
    except ValueError: 
        print('value ERROR \ntime:time')
        main()

    match(convert(hours,minutes))

def checker(hours, minutes): #checks that the numbers are acual times
    if 0 <= hours <= 24 : 
        if 0 <= minutes <= 60 : 
            return(hours, minutes)
        else:
            print(f'ERROR\nminuts have a problem--> {minutes} is not a VALID TIME!!')
            main()
    else:
        print(f'ERROR\nhour have a problem--> {hours} is not a VALID TIME!!')
        main()


def convert(h,m):
    # h = str(h)
    m = int(m) # quick fix
    m = str(round(m *1.66))

    return float(h +'.'+(m))

def match(time):

    match time : 
        case range(7, 8):
            return('breakfast time')  
                  
        case range(12, 13):
            return('lunch time')
        
        case range(18,19):
            return('dinner time')


if __name__ == "__main__":
    main()


"""
How to Test
Here’s how to test your code manually:

Run your program with python meal.py. Type 7:00 and press Enter. Your program should output:
breakfast time   
Run your program with python meal.py. Type 7:30 and press Enter. Your program should output:
breakfast time
Run your program with python meal.py. Type 12:42 and press Enter. Your program should output
lunch time
Run your program with python meal.py. Type 18:32 and press Enter. Your program should output
dinner time
Run your program with python meal.py. Type 11:11 and press Enter. Your program should output nothing.
"""