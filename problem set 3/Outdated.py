# https://cs50.harvard.edu/python/2022/psets/3/outdated/

months =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def outdated():
    date = input('Date: ').split('/')
    
    if len(date) > 1: # it's the  MM/DD/YYYY  format
            
        try:
            if not int(date[0]) > 12 and not int(date[1]) > 31:
                print(f"{date[-1]}-{int(date[0]):02}-{int(date[1]):02}") 
                #returns YYYY-MM-DD -> MM & DD have a padding if are single digit => 3=False,  03=True
        except ValueError:
            outdated()
            return
    else:
        try:
            date = date[0].split(' ')
            month = months.index(date[0]) +1
            day = int(date[1][:-1])
            if day > 31 :
                outdated()
                return
        except ValueError:
            outdated()
            return

        print(f"{date[-1]}-{month:02}-{day:02}") 


if __name__ == "__main__":
    outdated()

"""
How to Test
Here’s how to test your code manually:

Run your program with python outdated.py. Type 9/8/1636 and press Enter. Your program should output:
1636-09-08
Run your program with python outdated.py. Type September 8, 1636 and press Enter. Your program should output:
1636-09-08
Run your program with python outdated.py. Type 23/6/1912 and press Enter. Your program should reprompt the user.
Run your program with python outdated.py. Type December 80, 1980 and press Enter. Your program should reprompt the user.
"""