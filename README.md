#  Estimation Game (Python)

A simple and interactive number guessing game built with Python.  
The program selects a random number between 1 and 100, and the player tries to guess it with guidance from the system.

---

##  Features

-  Random number generation (1–100)
-  Unlimited attempts
-  Input validation (non-numeric input protection)
-  "Higher" / "Lower" hint system
-  Clean algorithmic structure
-  Error handling

---

## How the Game Works

1. The program picks a hidden number between **1 and 100**.
2. The user enters guesses.
3. The program gives hints:
   - `Enter a larger number!`
   - `Enter a smaller number!`
4. If the user types something other than a number, the program warns them.
5. Once the number is correctly guessed, the program displays the total number of attempts.

---

## Project Structure

etimation-game/
│── number_game.py
│── README.md
│── LICENSE
└── .gitignore


## Run the Project

Make sure Python 3.13 or newer is installed.
python number_game.py



Author

Furkan İpek
