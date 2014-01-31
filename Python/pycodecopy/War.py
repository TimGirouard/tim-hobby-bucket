# War
# 2 players - highest card wins

import Cards, Games

class War_Card(Cards.Card):
    """ A War Card. """

    @property
    def value(self):

        if self.is_face_up:
            v = War_Card.RANKS.index(self.rank) + 1
        else:
            v = None
        return v

class War_Deck(Cards.Deck):
    """ A War Deck. """
    def populate(self):
        for suit in War_Card.SUITS:
            for rank in War_Card.RANKS:
                self.cards.append(War_Card(rank, suit))

class War_Hand(Cards.Hand):
    """ A War Hand. """
    def __init__(self,name,money = 0):
        super(War_Hand, self).__init__()
        self.name = name
        self.money = money

    def __str__(self):
        rep = self.name + ":\t" + super(War_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        rep += "$" + str(self.money)
        return rep

    @property
    def total(self):
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None

        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
            t += card.value

        return t

    def is_busted(self):
        return self.total > 21

class War_Player(War_Hand):
    """A War Player."""

    def win(self):
        print(self.name, "wins.")
        self.money += 1

class War_Game(object):
    """ A Game of War. """
    def __init__(self, names):
        self.players = []
        for name in names:
            player = War_Player(name)
            self.players.append(player)

        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):

        # deal initial card to both players
        if len(self.deck.cards) < 3:
            self.deck.clear()
            self.deck.populate()
            self.deck.shuffle()
            print("\nReshuffling...\n")
        else:
            self.deck.deal(self.players, per_hand = 1)
            for player in self.players:
                print(player)
            if self.players[0].total > self.players[1].total:
                self.players[0].win()
            elif self.players[0].total < self.players[1].total:
                self.players[1].win()
            else:
                print("It's a tie!")
            # remove everyone's cards
            for player in self.players:
                player.clear()

def main():
    print("\t\tWelcome to War!\n")

    names = []

    for i in range(2):
        name = None
        while not name:
            name = input("Enter player "+str(i+1)+ "'s name: ")
        names.append(name)

    print()

    game = War_Game(names)

    again = None
    while again != "n" and game.players:
        game.play()
        again = Games.ask_yes_no("\nDo you want to play again? (Y/N): ")

main()
input("\n\nPress the enter key to exit.")
        
