# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
from decimal import Decimal

import requests, sys

api = "https://api.coindesk.com/v1/bpi/currentprice.json"


def main():
  if len(sys.argv) == 1 : 
    sys.exit('Missing command-line argument')

  try:
    number = Decimal(sys.argv[1])
  except ValueError:
    sys.exit('Command-line argument is not a number')

  print (f'${get_price(number)*number :,.4f}')


def get_price(n):
  try:
    response = requests.get(api)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
    data = response.json()
    return Decimal(data['bpi']['USD']['rate_float'])
  except (requests.RequestException, KeyError) as e:
    sys.exit(f"Error fetching Bitcoin price: {e}")


if __name__ == "__main__":
  print(main())


"""
How to Test
Here’s how to test your code manually:

Run your program with python bitcoin.py. Your program should use sys.exit to exit with an error message:
Missing command-line argument   
Run your program with python bitcoin.py cat. Your program should use sys.exit to exit with an error message:
Command-line argument is not a number
Run your program with python bitcoin.py 1. Your program should output the price of a single Bitcoin to four decimal places, using , as a thousands separator.
Run your program with python bitcoin.py 2. Your program should output the price of two Bitcoin to four decimal places, using , as a thousands separator.
Run your program with python bitcoin.py 2.5. Your program should output the price of 2.5 Bitcoin to four decimal places, using , as a thousands separator.
"""