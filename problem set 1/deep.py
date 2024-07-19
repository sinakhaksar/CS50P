#https://cs50.harvard.edu/python/2022/psets/1/deep/

def deep_thought_answer():
    # Prompt user for input
    user_input = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

    # Normalize user input for comparison (convert to lowercase and remove spaces)
    normalized_input = user_input.lower().replace(" ", "")

    # List of accepted answers (all case variations)
    accepted_answers = ["42", "fortytwo", "forty-two"]

    # Check if normalized input matches any accepted answer
    if normalized_input in accepted_answers:
        print("Yes")
    else:
        print("No")

# Call the function to prompt the user and check the answer
deep_thought_answer()


"""
How to Test
Here’s how to test your code manually:

Run your program with python deep.py. Type 42 and press Enter. Your program should output:
Yes 
Run your program with python deep.py. Type Forty Two and press Enter. Your program should output:
Yes
Run your program with python deep.py. Type forty-two and press Enter. Your program should output
Yes
Run your program with python deep.py. Type 50 and press Enter. Your program should output
No
"""