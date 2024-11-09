from random import shuffle

SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K".split()

# mycards = [(s, r) for s in SUITE for r in RANKS]
class Deck:
    
    def __init__(self):
        print("Creating new ordered deck...")
        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])

class Hand:
    
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))
    
    def add(self, add_cards):
        self.cards.extend(add_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}]".format(self.name, drawn_card))
        print("\n")
        return drawn_card
    
    def remove_war_card(self):
        war_cards = []
        for x in range(3):
            war_cards.append(self.hand.remove_card())
        return war_cards

print("Welcome to War, Shall we play a game?")