from .game import generate_code, validate_guess, color_count, correct_pos_and_color, check_guess, check_win_or_lose, get_win_percentage, format_guess_stats

# Implement game loop here
def mastermind():
    plays = 0
    wins = 0
    guess_stats = {}
    continue_playing = True

    while continue_playing:
        plays += 1
        user_guess_count = game_loop()
        if user_guess_count < 9:
            wins += 1
            if user_guess_count in guess_stats:
                guess_stats[user_guess_count] += 1
            else:
                guess_stats[user_guess_count] = 1

        print("Game Stats:")
        print(f"Total Games: {plays}")
        print(f"Win percent: {get_win_percentage(wins, plays)}")
        print("Win Distribution:")

        formatted_win_stats = format_guess_stats(guess_stats)
        for index in range(8):
            print(f"{index + 1}: {formatted_win_stats[index]}")
        print("")
        
        play_again = input("Would you like to play again? (y/n): ")
        continue_playing = play_again == "y"
    
def game_loop():
    print("Generating a 4-letter code...")
    code = generate_code()
    print(code)
    print("Guess the code! Each character in the code is" 
          + " one of the following letters: R, O, Y, G, B, P")
    print("")
    
    num_guesses = 0
    while num_guesses <= 8:
        num_guesses += 1
        guess = get_valid_guess()
        
        if check_win_or_lose(guess, code, num_guesses):
            print("You won! You guessed the code 🎉")
            return num_guesses

        guess_info = check_guess(guess, code)
        print(f"Total colors in the correct locations: {guess_info[0]}")
        print(f"Total correct colors in the wrong locations: {guess_info[1]}")

    print(f"You ran out of guesses. The code was {code}!")
    return num_guesses

def get_valid_guess():
    print("Enter a 4 letter guess:")
    guess = input("")
    
    while not validate_guess(guess):
        print(f'The guess "{guess}" was invalid')
        print("Please enter a new guess that is 4 letters long," 
              + "using only the letters R, O, Y, G, B, and P:")
        guess = input("")

    return guess
    
