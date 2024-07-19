#https://cs50.harvard.edu/python/2022/psets/1/extensions/

file = input('').split('.')
extesntion = file[-1].lower()


match extesntion: 
    case 'gif':
        print(f'image/{extesntion}')

    case 'jpg':
        print(f'image/{extesntion}')

    case 'jpeg':
        print(f'image/{extesntion}')

    case 'png':
        print(f'image/{extesntion}')

    case 'pdf':
        print(f'image/{extesntion}')

    case 'txt':
        print(f'image/{extesntion}')

    case 'zip':
        print(f'image/{extesntion}')

    case _ : 
        print('application/octet-stream')


"""
How to Test
Here’s how to test your code manually:

Run your program with python extensions.py. Type happy.jpg and press Enter. Your program should output:
image/jpeg   
Run your program with python extensions.py. Type document.pdf and press Enter. Your program should output:
application/pdf
"""