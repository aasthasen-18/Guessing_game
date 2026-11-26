# Number Guessing Game (Python)

A command-line Number Guessing Game built in Python 3 as part of the **Bachelor of Technology (CSE) in association with IBM** First Semester coursework (Problem Statement 5).

## Overview

In this game, the computer generates a secret random number between **1 and 100**, and the player has **5 attempts** to guess it. After each valid guess, the program provides helpful feedback (`Too low!` or `Too high!`) until the player either guesses the number or runs out of attempts.

## Features

- **Random Number Generation:** Uses Python's built-in `random` module to generate a secret integer between `1` and `100`.
- **Attempt Tracking:** Limits the player to `5` valid attempts per round and displays remaining tries after each guess.
- **Input Validation:**
  - Handles non-numeric inputs (e.g., `"abc"`) gracefully using `try-except` without crashing or deducting an attempt.
  - Rejects out-of-range numbers (`< 1` or `> 100`) without penalizing the player's remaining attempts.
- **Replayability:** Prompts the user to play again (`y/n`) after each round finishes.
- **Clean Grammar Formatting:** Dynamically adjusts singular/plural output (`1 attempt` vs. `attempts`).

## Concepts Used

- **Loops:** `while` loops (including `while-else` constructs) for game rounds and replay functionality.
- **Conditional Statements:** `if`, `elif`, and `else` for guess evaluation and range validation.
- **Functions:** Modular structure using `play_game()` and `main()`.
- **Exception Handling:** `try` and `except ValueError` for safe integer type conversion.
- **Modules:** `random.randint()` for generating the secret target.

## Prerequisites

- **Python 3.x** installed on your system.

## How to Run

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt and navigate to the project directory:
   ```bash
   cd path/to/project
   ```
3. Run the Python script:
   ```bash
   python main.py
   ```
   *(On some Windows setups, you may need to use `py main.py`.)*

## Test Cases & Verification

To verify the fixed test cases (`secret_number = 42`), uncomment `# secret_number = 42` in `main.py` and comment out `secret_number = random.randint(1, 100)`.

| Test Case | Scenario | Input(s) | Expected Output |
| :--- | :--- | :--- | :--- |
| **Test Case 1** | Normal Input (First-try win) | `42` | `Congratulations! You guessed it in 1 attempt` |
| **Test Case 2** | Boundary / Minimum & Maximum Input | `1`, then `100` | `Too low! Attempts left: 4` <br> `Too high! Attempts left: 3` |
| **Test Case 3** | Invalid & Out-of-Range Input | `abc`, then `150` | `Invalid input. Enter a whole number. Attempts left: 5` <br> `Out of range. Enter a number between 1 and 100. Attempts left: 5` |
| **Test Case 4** | Full 5-Attempt Loss Scenario | `10`, `90`, `50`, `30`, `20` | `Too low!` / `Too high!` hints followed by `Game Over! The number was 42` |

## Example Gameplay

```text
--- Number Guessing Game (1 to 100) ---
Enter your guess: 50
Too high! Attempts left: 4
Enter your guess: 25
Too low! Attempts left: 3
Enter your guess: 42
Congratulations! You guessed it in 3 attempts
Total attempts used: 3

Play again? (y/n): n
Thanks for playing!
```

## Project Structure

```text
├── main.py       # Main source code containing game logic and input validation
└── README.md     # Project documentation
```# Guessing_game
