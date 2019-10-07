class CardClass:
    def __init__(self, suit, value, name):
        self.suit = suit
        self.value = value
        self.name = name
        if (value == 1):
            self.ace = True
        else:
            self.ace = False
    
    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value
    
    def is_ace(self):
        return self.ace
    
    def switch_ace_value(self):
        if (self.is_ace):
            if (self.value == 1):
                print("Ace value updated from 1 to 11.")
                self.value = 11
            else:
                print("Ace value updated from 11 to 1.")
                self.value = 1
    
    def to_string(self):
        return "%s of %s" % (self.name, self.suit)

