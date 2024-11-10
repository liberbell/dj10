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
    
    def still_has_cards(self):
        return len(self.hand.cards) != 0

print("Welcome to War, Shall we play a game?")

d = Deck()
d.shuffle()
half1, half2 = d.spilit_in_half
comp = Player("computer", Hand(half1))
name = input("What is your name?")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.split_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round.")
    print("here are the current standings.")
    print(user.name + " has the count: " + str(len(user.hand.cards)))
    print(user.name + " has the count: " + str(len(user.hand.cards)))
    print("Play a card!")
    print("\n")

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print("War!")

        table_cards.extend(user.remove_war_card())
        table_cards.extend(comp.remove_war_card())