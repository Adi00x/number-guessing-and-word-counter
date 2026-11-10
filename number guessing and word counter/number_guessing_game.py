"""
Number Guessing Game
A simple game where the user tries to guess a randomly generated number.
"""

import random


def get_difficulty():
    """Get difficulty level from user."""
    print("\nSelect Difficulty Level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    while True:
        try:
            choice = int(input("Enter choice (1-3): "))
            if choice == 1:
                return 1, 50, 10
            elif choice == 2:
                return 1, 100, 7
            elif choice == 3:
                return 1, 200, 5
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")


def play_game(min_val, max_val, max_attempts):
    """Play the number guessing game."""
    secret_number = random.randint(min_val, max_val)
    attempts = 0

    print(f"\nI'm thinking of a number between {min_val} and {max_val}.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1

            if guess < min_val or guess > max_val:
                print(f"Please enter a number between {min_val} and {max_val}.")
                attempts -= 1
                continue

            if guess == secret_number:
                print(f"\n[+] Congratulations! You guessed it in {attempts} attempt(s)!")
                return True
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Attempts remaining: {remaining}\n")

        except ValueError:
            print("Please enter a valid number.")
            attempts -= 1

    print(f"\n[-] Game Over! The number was {secret_number}.")
    return False


def main():
    """Main game loop."""
    print("=" * 50)
    print("    NUMBER GUESSING GAME")
    print("=" * 50)

    games_played = 0
    games_won = 0

    while True:
        min_val, max_val, max_attempts = get_difficulty()
        won = play_game(min_val, max_val, max_attempts)

        games_played += 1
        if won:
            games_won += 1

        print(f"\nStats: Played {games_played}, Won {games_won}, Win Rate: {games_won/games_played*100:.1f}%")

        play_again = input("\nPlay again? (y/n): ").lower().strip()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()