import random

def play_game():
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    print("\nI'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f" Correct! You guessed the number in {attempts} attempts.\n")
                return True
        except ValueError:
            print(" Invalid input. Please enter a valid number.")

    print(f"Sorry! You've used all {max_attempts} attempts. The number was {number_to_guess}.\n")
    return False

def main():
    wins = 0
    losses = 0

    print("=====  Welcome to the Number Guessing Game =====")

    while True:
        result = play_game()
        if result:
            wins += 1
        else:
            losses += 1

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print(f"\n Game Over! Your Score: {wins} Wins, {losses} Losses.")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
