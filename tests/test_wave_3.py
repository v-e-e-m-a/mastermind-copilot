from app.game import get_win_percentage, format_guess_stats

# --------------------------test get_win_percentage------------------------------------

def test_get_win_percentage_returns_int():
    # Arrange
    wins = 1
    plays = 15
    
    # Act
    result = get_win_percentage(wins, plays)
    
    # Assert 
    assert type(result) == int


def test_get_win_percentage_no_games_returns_zero():
    # Arrange
    wins = 0
    plays = 0
    
    # Act
    result = get_win_percentage(wins, plays)
    
    # Assert 
    assert result == 0


def test_get_win_percentage_no_wins_returns_zero():
    # Arrange
    wins = 4
    plays = 0
    
    # Act
    result = get_win_percentage(wins, plays)
    
    # Assert 
    assert result == 0


def test_get_win_percentage_even_percentage():
    # Arrange
    wins = 3
    plays = 4
    
    # Act
    result = get_win_percentage(wins, plays)
    
    # Assert 
    assert result == 75


def test_get_win_percentage_rounds_down():
    # Arrange
    wins = 1
    plays = 15
    
    # Act
    result = get_win_percentage(wins, plays)
    
    # Assert 
    assert result == 6

# --------------------------test format_guess_stats------------------------------------

def test_format_guess_stats_no_games():
    # Arrange
    guess_stats = {}
    
    # Act
    result = format_guess_stats(guess_stats)
    
    # Assert
    assert len(result) == 8
    for s in result:
        assert s == ''


def test_format_guess_stats_one_pair():
    # Arrange
    guess_stats = {1: 4}
    
    # Act
    result = format_guess_stats(guess_stats)
    
    # Assert
    assert len(result) == 8

    # Check first entry is 4 Xs
    assert len(result[0]) == 4
    assert type(result[0]) == str
    for char in result[0]:
        assert char == 'X'

    # Check following entries are empty
    for index in range(1, 8):
        assert result[index] == ''


def test_format_guess_stats_all_pairs():
    # Arrange
    guess_stats = {
        1: 4,
        2: 3,
        3: 4,
        4: 2,
        5: 6,
        6: 1,
        7: 1,
        8: 3
    }
    
    # Act
    result = format_guess_stats(guess_stats)
    
    # Assert
    assert len(result) == 8

    assert len(result[0]) == 4
    assert result[0] == 'XXXX'

    assert len(result[1]) == 3
    assert result[1] == 'XXX'

    assert len(result[2]) == 4
    assert result[2] == 'XXXX'
    
    assert len(result[3]) == 2
    assert result[3] == 'XX'

    assert len(result[4]) == 6
    assert result[4] == 'XXXXXX'

    assert len(result[5]) == 1
    assert result[5] == 'X'

    assert len(result[6]) == 1
    assert result[6] == 'X'

    assert len(result[7]) == 3
    assert result[7] == 'XXX'
