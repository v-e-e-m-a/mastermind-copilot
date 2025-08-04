import random


# Wave 1
def generate_code():
    valid_letters = ['R', 'O', 'Y', 'G', 'B', 'P']
    code = []
    
    # Generate a code of 4 random letters from valid_letters
    for _ in range(4):
        code.append(random.choice(valid_letters))

    return code


def validate_guess(guess):
    valid_letters = {'R', 'O', 'Y', 'G', 'B', 'P'}

    # Exit early if guess is not exactly 4 elements long
    if len(guess) != 4:
        return False
    
    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = []
    for letter in guess:
        uppercased_guess.append(str(letter).upper())

    # Return False if we find an invalid element of guess
    for letter in uppercased_guess:
        if letter not in valid_letters:
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