from app.game import generate_code, validate_guess, check_win_or_lose

# --------------------------test generate_code------------------------------------

def test_generate_code_returns_list():
    #Arrange/Act
    result = generate_code()

    #Assert
    assert isinstance(result, list)


def test_generate_code_length_four():
    #Arrange/Act
    result = generate_code()

    #Assert
    assert len(result) == 4


def test_generate_code_uses_valid_letters():
    #Arrange
    valid_letters = {'R', 'O', 'Y', 'G', 'B', 'P'}

    #Act
    result = generate_code()

    #Assert
    for letter in result:
        assert letter in valid_letters


def test_generate_code_half_or_less_duplicates_over_10_runs():
    #Arrange/Act
    # Run generate_code multiple times and check for different outputs
    codes = {tuple(generate_code()) for _ in range(10)}

    #Assert
    # At least half of the codes generated should be unique
    assert len(codes) > 5

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


def test_validate_guess_true_lowercase_letters():
    #Arrange
    guess = ['b','b','p','p']

    #Act
    result = validate_guess(guess)

    #assert
    assert result is True


def test_validate_guess_false_empty_list():
    #Arrange
    guess = []

    #Act
    result = validate_guess(guess)

    #Assert
    assert result is False


def test_validate_guess_false_length_less_than_four():
    #Arrange
    guess = ['R','O','Y']

    #Act
    result = validate_guess(guess)

    #Assert
    assert result is False


def test_validate_guess_true_mixed_case_letters():
    #Arrange
    guess = ['R','o','Y','p']

    #Act
    result = validate_guess(guess)

    #Assert
    assert result is True


def test_validate_guess_false_non_string_types():
    #Arrange
    guess = ['R', 1, 'Y', 'P']

    #Act
    result = validate_guess(guess)

    #Assert
    assert result is False


def test_validate_guess_false_with_none_value():
    #Arrange
    guess = ['R', None, 'Y', 'P']

    #Act
    result = validate_guess(guess)

    #Assert
    assert result is False

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


def test_check_win_or_lose_true_at_max_guesses():
    #Arrange
    guess = ['R','B','B','P']
    code = ['R','B','B','P']
    num_guesses = 8

    #Act
    result = check_win_or_lose(guess, code, num_guesses)

    #Assert
    assert result is True


def test_check_win_or_lose_true_with_mixed_case_guess():
    #Arrange
    guess = ['r','B','b','P']
    code = ['R','B','B','P']
    num_guesses = 3

    #Act
    result = check_win_or_lose(guess, code, num_guesses)

    #Assert
    assert result is True


def test_check_win_or_lose_true_at_first_guess():
    #Arrange
    guess = ['R','B','B','P']
    code = ['R','B','B','P']
    num_guesses = 1

    #Act
    result = check_win_or_lose(guess, code, num_guesses)

    #Assert
    assert result is True


def test_check_win_or_lose_false_exceeds_max_with_wrong_guess():
    #Arrange
    guess = ['R','B','B','O']  # Wrong guess
    code = ['R','B','B','P']
    num_guesses = 9

    #Act
    result = check_win_or_lose(guess, code, num_guesses)

    #Assert
    assert result is False