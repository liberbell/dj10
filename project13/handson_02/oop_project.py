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
        return (self.allcards)

class Hand:
    pass

class Player:
    pass

print("Welcome to War, Shall we play a game?")