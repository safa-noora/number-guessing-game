Guess-Game

Guess-Game is a number guessing game written in Python that runs in the terminal.

How to play
The player has 7 tries to guess a number between 1 and 100.
If the guess is correct, the player wins and the number of guesses used is shown.
If the guess is lower than the number, the game prints Low!
If the guess is higher than the number, the game prints High!
Input checks
If the input is not a whole number, the game asks the player to enter a valid number.
If the number is outside 1 to 100, the game asks for a number in range.
Invalid inputs are not counted as tries.
Game over

If all 7 tries are used without a correct guess, the game stops and shows the actual number.

How to run

Make sure Python is installed, then run this in the project folder:

python guess.py
