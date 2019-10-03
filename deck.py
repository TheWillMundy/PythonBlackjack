import card

class DeckClass:
    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):
        # iterate through suits
        deck = {
            'Hearts': [],
            'Spades': [],
            'Clubs': [],
            'Diamonds': []
        }
        for suit in deck.keys():
            cards = []
            for value in range(1, 14):
                switcher = {
                        1: 'Ace',
                        11: 'Jack',
                        12: 'Queen',
                        13: 'King'
                    }
                string_value = switcher.get(value, str(value))
                cards.append((string_value, value))
            deck[suit] = cards
        self.deck = deck
        return deck