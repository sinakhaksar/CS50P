#https://cs50.harvard.edu/python/2022/psets/2/twttr/

# need this for test_twttr.py

def main():
    user_input = input('input: ')
    print(shorten(user_input))


def shorten(word):
    valves = ['a','A', 'e', 'E','i', 'I', 'o', 'O', 'u', 'U']

    for char in word : 
        if char in valves : 
            word = word.replace(char,'')
    
    return word


if __name__ == "__main__":
    main()
