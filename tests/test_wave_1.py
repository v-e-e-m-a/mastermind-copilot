from app.game import generate_code, validate_guess, check_win_or_lose

# --------------------------test generate_code------------------------------------

def test_generate_code_length_four():
    #Arrange/Act
    result = generate_code()

    #Assert
    assert len(result) == 4

def test_generate_code_is_list():
    #Arrange/Act
    result = generate_code()

    #Assert
    assert type(result) == list

def test_generate_code_uses_valid_letters():
    #Arrange
    valid_letters = ['R', 'O', 'Y', 'G', 'B', 'P']

    #Act
    result = generate_code()

    #Assert
    for letter in result:
        assert letter in valid_letters

# --------------------------test validate_guess------------------------------------

def test_validate_guess_false_length_greater_than_four():
    #Arrange
    guess = ['R','R','R','R','R']

    #Act
    result = validate_guess(guess)

    #Assert
    assert result is False


def test_validate_guess_true_valid_letters_rygp():
    #Arrange
    guess = ['R','Y','G','P']

    #Act
    result = validate_guess(guess)

    #assert
    assert result is True


def test_validate_guess_true_valid_letters_bp():
    #Arrange
    guess = ['B','B','P','P']

    #Act
    result = validate_guess(guess)

    #assert
    assert result is True


def test_validate_guess_false_invalid_letters():
    #Arrange
    guess = ['R','S','Y','P']

    #Act
    result = validate_guess(guess)

    #assert
    assert result is False


def test_validate_guess_true_mixed_case_letters():
    #Arrange
    guess = ['B','b','p','P']

    #Act
    result = validate_guess(guess)

    #assert
    assert result is True


def test_validate_guess_true_lowercase_letters():
    #Arrange
    guess = ['b','b','p','p']

    #Act
    result = validate_guess(guess)

    #assert
    assert result is True

# --------------------------test check_win_or_lose------------------------------------

def test_check_win_or_lose_both_conditions_true():
    #Arrange
    guess = ['R','B','B','P']
    code = ['R','B','B','P']
    num_guesses = 3

    #Act
    result = check_win_or_lose(guess, code, num_guesses)

    #Assert
    assert result is True


def test_check_win_or_lose_false_if_exceeds_max_guesses():
    #Arrange
    guess = ['R','B','B','P']
    code = ['R','B','B','P']
    num_guesses = 9

    #Act
    result = check_win_or_lose(guess, code, num_guesses)

    #Assert
    assert result is False


def test_check_win_or_lose_none_if_game_ongoing():
    #Arrange
    guess = ['R','B','B','P']
    code = ['R','B','B','O']
    num_guesses = 2

    #Act
    result = check_win_or_lose(guess, code, num_guesses)

    #Assert
    assert result is None