#https://cs50.harvard.edu/python/2022/psets/0/faces/
happy= '🙂'
sad = '🙁'
pokerFace = '😐'


text = input().split()

for i in range(len(text)): 
    if text[i] == ':)':    
        text[i] = happy
    elif text[i] == ':(':
        text[i] = sad
    elif text[i] == ':|' or text[i] == ':/':
        text[i] = pokerFace

for i in text : 
    print(i, end=" ")


"""
How to Test
Here’s how to test your code manually:

Run your program with python faces.py. Type Hello :) and press Enter. Your program should output:
Hello 🙂
Run your program with python faces.py. Type Goodbye :( and press Enter. Your program should output:
Goodbye 🙁
Run your program with python faces.py. Type Hello :) Goodbye :( and press Enter. Your program should output
Hello 🙂 Goodbye 🙁
"""