import random


# Wave 1
VALID_LETTERS = {'R', 'O', 'Y', 'G', 'B', 'P'}

def generate_code():
    code = []
    
    # Generate a code of 4 random letters from VALID_LETTERS
    letters_list = list(VALID_LETTERS)
    for _ in range(4):
        code.append(random.choice(letters_list))

    return code


def validate_guess(guess):
    # Exit early if guess is not exactly 4 elements long
    if len(guess) != 4:
        return False
    
    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = []
    for letter in guess:
        uppercased_guess.append(str(letter).upper())

    # Return False if we find an invalid element of guess
    for letter in uppercased_guess:
        if letter not in VALID_LETTERS:
            return False
        
    return True


def check_win_or_lose(guess, code, num_guesses):
    # Exit early if the number of guesses exceeds 8
    if num_guesses > 8:
        return False

    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = []
    for letter in guess:
        uppercased_guess.append(str(letter).upper())

    # Check if the guess and code are identical (win condition)
    # The guard clause guarantees the number of guesses is 8 or less
    if code == uppercased_guess:
        return True
    else: # Game is still in progress
        return None


# Wave 2
# Add your Wave 2 functions here


# Wave 3
# Add your Wave 3 functions here