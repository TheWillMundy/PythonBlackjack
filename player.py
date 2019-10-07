class PlayerClass:
    def __init__(self, player_no):
        print "Person created"
        self.cards = []
        self.no = player_no
        self.busted = False
    
    def reset(self):
        self.cards = []
        self.busted = False
    
    def get_cards(self):
        return self.cards
    
    def get_total_value(self):
        return sum(map(lambda card: card.get_value(), self.cards))
    
    def add_card(self, card):
        self.cards.append(card)
        if (self.get_total_value() > 21):
            self.busted = True
    
    def get_last_card(self):
        return self.cards[-1]

    def check_busted(self):
        return self.busted
    
    def get_player_no(self):
        return self.no
    
    def initial_deal(self):
        new_cards = []
    
    def has_aces(self):
        if (len(filter(lambda card : card.is_ace(), self.get_cards())) > 0):
            return True
        else:
            return False
    
    def filter_aces(self):
        return filter(lambda card : card.is_ace(), self.get_cards())
    
    def to_string(self):
        print("")
        