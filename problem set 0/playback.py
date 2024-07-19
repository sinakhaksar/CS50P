#https://cs50.harvard.edu/python/2022/psets/0/playback/

text = input('').split() # take the string and split it in a list 


for i in range(len(text)): 
    print(text[i],end='') # print the elemnts in the test list one by one  
    if i < len(text)-1: # so after the last word wouldn't print '...'
        print('...', end='')


"""
How to Test
Here’s how to test your code manually:

Run your program with python playback.py. Type This is CS50 and press Enter. Your program should output:
This...is...CS50    
Run your program with python playback.py. Type This is our week on functions and press Enter. Your program should output:
This...is...our...week...on...functions
Run your program with python playback.py. Type Let's implement a function called hello and press Enter. Your program should output
Let's...implement...a...function...called...hello
"""