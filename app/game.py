import random


# Wave 1
VALID_LETTERS = {'R', 'O', 'Y', 'G', 'B', 'P'}

def generate_code():
    # Generate a code of 4 random letters from VALID_LETTERS
    letters_list = list(VALID_LETTERS)
    code = [random.choice(letters_list) for _ in range(4)]

    return code


def validate_guess(guess):
    # Exit early if guess is not exactly 4 elements long
    if len(guess) != 4:
        return False
    
    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = uppercase_list(guess)

    # Return False if we find an invalid element of guess
    for letter in uppercased_guess:
        if letter not in VALID_LETTERS:
            return False
        
    return True


def check_code_guessed(guess, code):
    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = uppercase_list(guess)

    # Check if the guess and code are identical (win condition)
    return code == uppercased_guess


def uppercase_list(char_list):
    """Convert a list of characters to uppercase."""
    uppercased_list = [str(letter).upper() for letter in char_list]
    return uppercased_list

# Wave 2
# Add your Wave 2 functions here


# Wave 3
# Add your Wave 3 functions here