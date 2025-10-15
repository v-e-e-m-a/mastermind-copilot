import pytest
from app.game import generate_code
from app.game import validate_guess
from app.game import check_code_guessed

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
    # Arrange/Act
    # Run generate_code multiple times and check for different outputs
    runs = 10
    codes = {tuple(generate_code()) for _ in range(runs)}
    
    # Assert
    # At least half of the codes generated should be unique
    assert len(codes) > runs / 2


def test_validate_guess_false_length_greater_than_four():
  # Arrange
  guess = ['R', 'R', 'R', 'R', 'R']

  # Act
  result = validate_guess(guess)

  # Assert
  assert result is False


def test_validate_guess_true_valid_letters_rygp():
  # Arrange
  guess = ['R', 'Y', 'G', 'P']

  # Act
  result = validate_guess(guess)

  # Assert
  assert result is True


def test_validate_guess_true_valid_letters_bp():
  # Arrange
  guess = ['B', 'B', 'P', 'P']

  # Act
  result = validate_guess(guess)

  # Assert
  assert result is True


def test_validate_guess_false_invalid_letters():
  # Arrange
  guess = ['R', 'S', 'Y', 'P']

  # Act
  result = validate_guess(guess)

  # Assert
  assert result is False


def test_validate_guess_true_lowercase_letters():
  # Arrange
  guess = ['b', 'b', 'p', 'p']

  # Act
  result = validate_guess(guess)

  # Assert
  assert result is True

# --------------------------test check_win_or_lose------------------------------------

def test_check_code_guessed_true():
  # Arrange
  guess = ['R', 'B', 'B', 'P']
  code = ['R', 'B', 'B', 'P']

  # Act
  result = check_code_guessed(guess, code)

  # Assert
  assert result is True


def test_check_code_guessed_false_if_game_ongoing():
  # Arrange
  guess = ['R', 'B', 'B', 'P']
  code = ['R', 'B', 'B', 'O']

  # Act
  result = check_code_guessed(guess, code)

  # Assert
  assert result is False