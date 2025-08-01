import random

# Wave 1
# generate_code 
# - takes no arguments  
# - returns a list of 4 letters
# - each letter must be one of: R, O, Y, G, B, P
# - letters can be repeated
# - the list is randomly generated

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


def check_win_or_lose(guess, code, num_guesses):
    # Exit early if the number of guesses exceeds 8
    if num_guesses > 8:
        return False
    
    # Convert guess to uppercase for case-insensitive comparison
    guess_upper = [letter.upper() for letter in guess]
    
    # Check if the guess and code are identical (win condition)
    # The guard clause guarantees the number of guesses is 8 or less
    if guess_upper == code:
        return True
    
    # Game is still in progress
    return None

# Wave 2
# Add your Wave 2 functions here

# Wave 3
# Add your Wave 3 functions here
