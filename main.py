import deck
import random
import os
import platform
from player import PlayerClass

def clear_screen():
    system_name = platform.system()
    if (system_name == "Windows"):
        _=os.system("cls")
    else:
        _=os.system('clear')

def main():
    players = []

    print "Welcome to BlackJack!"
    # Set number of players
    flag = False
    while (True):
        # Check that they input an integer
        try:
            player_ct = input("How many players would like to play (1-4): ")
            player_ct = int(player_ct)
            if (player_ct < 1 or player_ct > 4):
                continue
            for player in range(player_ct):
                players.append(PlayerClass(player + 1))
            break
        except:
            if (flag):
                return
            print "Please enter a valid integer, or any character to exit."
            flag = True
    
    # First create & shuffle deck for the game
    deck_cls = deck.DeckClass()
    shuffled_deck = deck_cls.create_deck()

    random.shuffle(shuffled_deck)

    # Start game
    while (True):
        # Phase 1: Deal
        print("The dealing will now begin.\n")
        for player in players:
            # Reset players
            player.reset()
            player_no = player.get_player_no()
            print("Player %s, you have been dealt: \n" % player_no)
            for _ in range(2):
                dealt_card = shuffled_deck.pop()
                print(dealt_card.to_string())
                player.add_card(dealt_card)
            # Post initial dealing
            total_value = player.get_total_value()
            print("The total value of your cards is: %s" % total_value)
            if (player_no < len(players)):
                raw_input("Type anything once you are ready to continue to the next player.")
                clear_screen()
            else:
                raw_input("Type anything once you are ready for the dealer to deal themselves in.")
                clear_screen()
        # Dealer is dealt
        dealer = PlayerClass("Dealer")
        for _ in range(2):
            dealt_card = shuffled_deck.pop()
            dealer.add_card(dealt_card)

        # Loop on hit or not
        for player in players:
            flag = False
            player_no = player.get_player_no()
            print("The dealer's face up card is: %s" % dealer.get_last_card().to_string())
            while (True):
                aces = player.filter_aces()
                if (len(aces) > 0):
                    print("It appears you have %d aces. Below, select whether to adjust their value or not." % len(aces))
                    for ace in aces:
                        update = raw_input("If you'd like to switch the value of this ace from %d then type 'yes', otherwise type 'no'. \n" % ace.get_value())
                        if (update == "yes"):
                            ace.switch_ace_value()
                        else:
                            print("Ok, nothing will be done to this ace. \n")
                try:
                    print("Player %s, your current total hand value is: %s" % (player_no, player.get_total_value()))
                    option = input("Player %s, type 1 to hit or 2 to stand: " % player_no)
                    option = int(option)
                    if (option == 2):
                        break
                    else:
                        dealt_card = shuffled_deck.pop()
                        print(dealt_card.to_string())
                        player.add_card(dealt_card)
                        total_value = player.get_total_value()
                        print("The total value of your cards is now: %s" % total_value)
                        if (player.check_busted()):
                            raw_input("You've busted! Type anything to continue.")
                            clear_screen()
                            break
                except:
                    if (flag):
                        return
                    print("Please enter 1 to hit, 2 to stay, or any character to exit")
                    flag = True
            clear_screen()
        
        # Now the dealer's turn
        print("The dealer's facedown card is: %s" % dealer.get_cards()[0].to_string())
        players_in = filter(lambda player : player.check_busted() == False, players)
        if (len(players_in) > 0 and dealer.get_total_value() < 17):
            while (dealer.get_total_value() < 17):
                dealt_card = shuffled_deck.pop()
                print("The dealer has drawn another card: %s \n" % dealt_card.to_string())
                dealer.add_card(dealt_card)
        if (dealer.check_busted()):
            print("The dealer has busted with a final value of: %s" % dealer.get_total_value())
        else:
            print("The dealer hand's final value is: %s" % dealer.get_total_value())
        
        if (len(players_in) < 1):
            print("No players are still in, so the House has won.")
        else:
            for player in players_in:
                player_no = player.get_player_no()
                if (dealer.check_busted() or player.get_total_value() > dealer.get_total_value()):
                    print("Player %s has beaten the dealer!" % player_no)
                else:
                    print("Unfortunately Player %s has lost to the dealer." % player_no)
        play_again = raw_input("If you'd like to play again, type 'yes': ")
        if (play_again != "yes"):
            return
        clear_screen()
        # Towards the end, check if a new deck is necessary

if __name__ == "__main__":
    main()