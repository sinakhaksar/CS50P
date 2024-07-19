# E = m C2
#https://cs50.harvard.edu/python/2022/psets/0/einstein/

c =300000000

m = int(input('m>>'))
e = m * c *c
print(f'{e:,}')


"""
How to Test
Here’s how to test your code manually:

Run your program with python einstein.py. Type 1 and press Enter. Your program should output:
90000000000000000
Run your program with python einstein.py. Type 14 and press Enter. Your program should output:
1260000000000000000
Run your program with python einstein.py. Type 50 and press Enter. Your program should output
4500000000000000000
"""