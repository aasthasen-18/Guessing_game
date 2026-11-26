import random

def play_game():
    # Generate random number (Note: Set secret_number = 42 to test the exact test cases)
    secret_number = random.randint(1, 100)
    # secret_number = 42  # Uncomment this line for testing
    
    attempts_left = 5
    attempts_used = 0

    print("\n--- Number Guessing Game (1 to 100) ---")

    while attempts_left > 0:
        user_input = input("Enter your guess: ")

        # Validate whole number
        try:
            guess = int(user_input)
        except ValueError:
            print(f"Invalid input. Enter a whole number. Attempts left: {attempts_left}")
            continue

        # Validate range
        if guess < 1 or guess > 100:
            print(f"Out of range. Enter a number between 1 and 100. Attempts left: {attempts_left}")
            continue

        # Process valid guess
        attempts_left -= 1
        attempts_used += 1

        if guess == secret_number:
            word = "attempt" if attempts_used == 1 else "attempts"
            print(f"Congratulations! You guessed it in {attempts_used} {word}")
            break
        elif guess < secret_number:
            print(f"Too low! Attempts left: {attempts_left}")
        else:
            print(f"Too high! Attempts left: {attempts_left}")
    else:
        print(f"Game Over! The number was {secret_number}")

    print(f"Total attempts used: {attempts_used}")

def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()