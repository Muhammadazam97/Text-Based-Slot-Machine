Text-Based Slot Machine 🎰

A simple, text-based slot machine game written in Python. The game allows users to deposit money, place bets on one or multiple lines, and play until they cash out or run out of funds. This project provides an introduction to game logic, random generation, and basic user interaction in Python.

How It Works

1. Deposit Money:
   The user starts by depositing an amount of money, which sets their initial balance.

2. Place Bets:

   The player can bet on 1, 2, or 3 lines of the slot machine.
   The bet amount on each line is chosen by the user.
   Total bet = (bet amount) * (number of lines bet on).
3. Spin the Slot Machine:

   The slot machine "spins," randomly generating symbols on each line.
   Winning lines multiply the bet amount and add to the user's balance.
4. Check Results:

   If the user has a winning line, their winnings are added to their balance.
   The user can choose to play again or cash out.
5. End Game:

   The game continues until the player decides to cash out or their balance reaches zero.

Features

* Simple text-based interface
* Randomly generated symbols for each reel
* Multiple betting options (1-3 lines)
* Balance updates with each win or loss

Usage
1. Run the program:
python main.py

2. Follow the on-screen instructions to:
* Deposit money
* Place bets on lines
* Spin the slot machine and check for wins
* Choose to play again or cash out

Example:

What would you like to deposit? $100

Enter the number of lines to bet on (1-3): 2

What would you like to bet on each line? $10

You are betting $10 on 2 lines. Total bet is equal to: $20

[ 🎲 🎰 🎲 ] - You won $50!

Current balance: $130

Would you like to play again? (y/n): 



File Structure

main.py: The main script containing game logic and functions.
README.md: Information about the project.

Future Improvements

* Add additional line options and winning combinations.
* Improve payout logic with more realistic slot machine configurations.
* Implement a graphical interface.
