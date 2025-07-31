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

# Wave 2
# Add your Wave 2 functions here

# Wave 3
# Add your Wave 3 functions here
