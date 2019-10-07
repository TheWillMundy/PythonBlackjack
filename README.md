# Instructions
In order to start the game, simply type `python main.py` inside your shell. Just two words!

## In-game detailed instructions
You will then be able to add between 1-4 players to your game. Once you've selected the number of players, the dealing will begin with a shuffled deck of cards, and each player will be dealt sequentially. After each player has had a chance to see their cards, they must type something or a simple return statement to allow the next player to see their dealt hand (the screen is cleared following each player's turn, so each player cannot see the previous player's hand). After the last player has seen their hand, the dealer will deal themselves in and it will be the first player's turn once again.

Each player will see the dealer's faceup card as well as the total value of their cards. They can type 1 to receive another card or 2 to not receive any more cards. If they choose to not receive any more cards, it will be the next player's turn. 

Once all the players have gone, it will be the dealer's turn. Their facedown card will first be revealed. If all the players have busted, the dealer automatically wins. Otherwise, the dealer will begin to receive another card or stop taking cards. If the dealer hand's total value is below 17, they will take another card until the value is above 17. Once the value is above 17, if they have busted, the remaining players will win. Otherwise, their card value is compared to each remaining player's card value. The players whose card value is above that of the dealer will win, while those equal or below will lose.

Finally, there will be a prompt to play again or not. To play again, type "yes". Otherwise, type "no" or press return.

# Design Decisions
The `main.py` file contains the main game logic, handling the main flow of the game as well as any edge flows that might arise (ex: when the player receives aces, or the player types in a character other than the accepted responses for an input). The `main.py` file uses three files, `card.py`, `deck.py`, and `player.py` to modularize its structure. 

The `card.py` file contains a `CardClass` which the `deck.py` file uses to instantiate new cards in the deck object's `create_deck` method. Each card has a suit, numeric value, and "name", where the name allows for face cards and aces to be identified. Additionally, the card class has two helper methods to handle the ace edge case (one to check whether the card is an ace, the other to toggle the value between 1 and 11 depending on the user's choice). All cards that are aces have an initial value of 1. Cards also have a `to_string` method which prints their name and suit. 

The `deck.py` file contains a `DeckClass` which is instantiated to create a new deck object. Its method `create_deck` creates a full, ordered deck of 52 cards with all 4 suits represented. The deck is in an array structure, with each element being a single card element, as this structure could be easily shuffled using the random module.

The `player.py` file contains a `PlayerClass` which can be instantiated to create a new player. This player object stores its cards in an array since the order of the cards doesn't matter. Each card is its own object since for aces the value might change, and it is possible for a player to have more than one ace, so those two cards are not interchangeable. The player class also has some helper methods which allow for the main program driver to check whether they are busted, filter their card array to only aces, or reset their values so that the player can play with a fresh deal. 


# Choice of tooling
## Language: Python
I chose to use Python since it is very easy to create a terminal application with it, and the ability to hide previous text (through the terminal clear screen command) allows for each player to only view their own cards. Additionally, Python's ability to create classes allowed for a high degree of modularization between the different structures involved. Similarly, the ability to easily import modules allowed for the deck class to use the card class, as well as the main driver to use the card, deck, and player classes. Additionally, since we used Python we employed snake case for almost all of the program except for classes.

## Additional Libraries
### random
This was used in order to shuffle the deck, using its shuffle method.

### os & platform
`platform` was used to check the system platform, and then depending on the system (Windows or Linux/OSX) the `clear_screen` method could use the correct system call to clear the screen using the `os` module.

### Testing library
`unittest` was used so that 