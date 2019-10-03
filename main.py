import deck

def main():
    players = 0
    
    print "Welcome to BlackJack!"
    # Set number of players
    while (True):
        players = input("How many players would like to play (1-4): ")
        # Check that they input an integer
        try:
            players = int(players)
            break
        except:
            print "Please enter a valid integer."
    
    # First create deck for the game
    deck_cls = deck.DeckClass()
    game_deck = deck_cls.create_deck()
    print(game_deck)

    # Start game
    while (True):
        print "The game has begun!"

        # Towards the end, check if a new deck is necessary
    print "Running!"

if __name__ == "__main__":
    main()