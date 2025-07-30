import random

COLORS = {"R", "O", "Y", "G", "B", "P"}


# Wave 1
def generate_code():
    colors_tuple = tuple(COLORS)
    return [random.choice(colors_tuple) for _ in range(4)]


def validate_guess(guess):
    if len(guess) != 4:
        return False
    
    guess_uppercase = get_uppercased_guess(guess)
    return set(guess_uppercase).issubset(COLORS)


def get_uppercased_guess(guess):
    uppercased_guess = []
    for letter in guess:
        uppercased_guess.append(letter.upper())
    return uppercased_guess


def check_win_or_lose(guess, code, num_guesses):
    if num_guesses >= 8:
        return False

    guess_uppercase = get_uppercased_guess(guess)
    if code == guess_uppercase:
        return True


# Wave 2
def color_count(guess, code):
    # Create frequency maps of the letters in guess and code
    guess_map = {}
    code_map = {}
    for index in range(4):
        letter_guess = guess[index].upper()
        addOrUpdateDictEntry(letter_guess, guess_map)

        letter_code = code[index]
        addOrUpdateDictEntry(letter_code, code_map)

    # For each unique letter in code, see if it 
    # exists in guess; if so, increase count. 
    count = 0
    for key, code_value in code_map.items():
        if key in guess_map:
            guess_value = guess_map[key]
            if guess_value > code_value:
                count += code_value
            else:
                count += guess_value

    return count


def addOrUpdateDictEntry(letter, dict):
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 1


def correct_pos_and_color(guess, code):
    count = 0
    for index in range(4):
        if guess[index].upper() == code[index]:
            count += 1

    return count


def check_guess(guess, code):
    total_correct = correct_pos_and_color(guess, code)
    wrong_position = color_count(guess, code) - total_correct

    return total_correct, wrong_position


# Wave 3
def get_win_percentage(wins, plays):
    return int(wins / plays * 100) if plays else 0


def format_guess_stats(guess_stats):
    formatted_stats = [""] * 8
    for num_guesses, wins in guess_stats.items():
        formatted_stats[num_guesses - 1] = "X" * wins

    return formatted_stats

