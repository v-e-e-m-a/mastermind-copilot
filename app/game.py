# Wave 1
# Add your Wave 1 functions here

#generate_code
# - takes no arguments
# - returns a list of 4 letters
# - each letter must be one of: R, O, Y, G, B, P
# - letters may be repeated
# - the list must be generated randomly
import random

def generate_code():
    valid_letters = ['R', 'O', 'Y', 'G', 'B', 'P']
    return [random.choice(valid_letters) for _ in range(4)]

def validate_guess(guess):
    valid_letters = {'R', 'O', 'Y', 'G', 'B', 'P'}
    if len(guess) != 4:
        return False
    for letter in guess:
        if str(letter).upper() not in valid_letters:
            return False
    return True

# Function to check if the guess matches the code (case-insensitive)
def check_code_guessed(guess, code):
    """
    Determines if the user's guess matches the code (case-insensitive).
    Args:
        guess (list): A 4-element list representing the user's guess.
        code (list): A 4-element list representing the code to guess.
    Returns:
        bool: True if guess matches code (case-insensitive), False otherwise.
    """
    return [str(g).upper() for g in guess] == [str(c).upper() for c in code] 


# Add your Wave 2 functions here

# Wave 3
# Add your Wave 3 functions here
