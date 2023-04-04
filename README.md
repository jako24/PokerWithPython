# Poker Game

This is a simple poker game implemented in Python. Classes for Cards, Decks, Players, and PokerGame are included. The game is played with a streamlined form of the conventional Texas Hold'em rules, where each player is given a set number of cards, and the highest-ranking hand wins.

Each conceivable hand in the game is given a score using a dictionary; a higher score indicates a stronger hand. With Royal Flush being the highest hand and High Card being the lowest, the scoring system is consistent with the normal ranks found in most poker games.

# Usage 

To use the code, simply create a PokerGame object with the necessary number of players and cards each hand by importing the classes from the poker.py file. For instance:

```
from poker import PokerGame

# Create a game with 4 players and 5 cards per hand
game = PokerGame(4, 5)

# Play the game
print(game.play())

```
The cards will be dealt, each player's hand will be shown, and the winner will be decided via the play() method. The console will print the winner's name along with their hand ranking.

# License

This code is licensed under the MIT License. Feel free to use it for any purpose.


