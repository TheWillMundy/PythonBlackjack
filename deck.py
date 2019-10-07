import card

class DeckClass:
    def __init__(self):
        self.deck = self.create_deck()

    def create_ace_deck(self):
        # iterate through suits
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        cards = []
        for suit in suits:
            # Create ace
            card_obj = card.CardClass(suit, 1, 'Ace')
            for value in range(2, 10):
                card_obj = card.CardClass(suit, 1, 'Ace')
                cards.append(card_obj)
            # Then face cards
            for value in range(3):
                card_obj = card.CardClass(suit, 1, 'Ace')
                cards.append(card_obj)
        return cards

    def create_deck(self):
        # iterate through suits
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        cards = []
        for suit in suits:
            # Create ace
            card_obj = card.CardClass(suit, 1, 'Ace')
            for value in range(2, 10):
                card_obj = card.CardClass(suit, value, str(value))
                cards.append(card_obj)
            # Then face cards
            for value in range(3):
                switcher = {
                    0: 'Jack',
                    1: 'Queen',
                    2: 'King'
                }
                card_obj = card.CardClass(suit, 10, switcher.get(value, ''))
                cards.append(card_obj)
        return cards