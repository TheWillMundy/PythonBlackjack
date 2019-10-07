import unittest
from unittest import TestCase

import card
import deck
import player

class Test(TestCase):
    def test_create_deck_length(self):
        print("Should create the same length deck every time.")
        new_deck = deck.DeckClass()
        self.assertEqual(len(new_deck.create_deck()), len(new_deck.create_deck()))
    
    def test_create_card(self):
        print("Should create a card with specified values.")
        suit = "Hearts"
        value = 3
        name = str(value)
        new_card = card.CardClass(suit, value, name)
        self.assertEqual(new_card.get_suit(), suit)
        self.assertEqual(new_card.get_value(), value)
        self.assertEqual(new_card.to_string(), "%s of %s" % (name, suit))
    
    def test_is_ace(self):
        print("Should assert ace property is true for ace cards only.")
        ace_card = card.CardClass('Hearts', 1, 'Ace')
        non_ace_card = card.CardClass('Hearts', 3, '3')
        self.assertTrue(ace_card.is_ace())
        self.assertFalse(non_ace_card.is_ace())
    
    def test_switch_ace_value(self):
        print("Should toggle ace value.")
        ace_card = card.CardClass('Hearts', 1, 'Ace')
        self.assertEqual(ace_card.get_value(), 1)
        ace_card.switch_ace_value()
        self.assertEqual(ace_card.get_value(), 11)
        ace_card.switch_ace_value()
        self.assertEqual(ace_card.get_value(), 1)
    
    def test_player_card_value(self):
        print("Should return the correct total card value.")
        new_player = player.PlayerClass(1)
        card_1 = card.CardClass("Hearts", 10, "King")
        card_2 = card.CardClass("Spades", 9, str(9))
        new_player.add_card(card_1)
        new_player.add_card(card_2)
        card_total_value = card_1.get_value() + card_2.get_value()
        self.assertEqual(new_player.get_total_value(), card_total_value)

    def test_busted_player(self):
        print("Should indicate player is busted with total card value above 21")
        new_player = player.PlayerClass(1)
        card_1 = card.CardClass("Hearts", 10, "King")
        card_2 = card.CardClass("Spades", 10, "Queen")
        new_player.add_card(card_1)
        new_player.add_card(card_2)
        self.assertFalse(new_player.check_busted())
        card_3 = card.CardClass("Diamonds", 3, str(3))
        new_player.add_card(card_3)
        self.assertTrue(new_player.check_busted())
        
    def test_reset_player(self):
        print("Should reset player data except player number.")
        new_player = player.PlayerClass(1)
        self.assertEqual(new_player.get_cards(), [])
        new_card = card.CardClass("Hearts", 3, str(3))
        new_player.add_card(new_card)
        self.assertEqual(len(new_player.get_cards()), 1)
        new_player.reset()
        self.assertEqual(len(new_player.get_cards()), 0)

if __name__ == '__main__':
    unittest.main()