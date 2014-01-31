# War
# 2 players - resolve whole game

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

    def __str__(self):
        rep = self.name + ":\t" + super(War_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
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

        # deal initial cards to both players
        
        self.deck.deal(self.players, per_hand = 26)
        for player in self.players:
            for card in player.cards:
                card.flip()
                
        #start off the game (display players and flip first card)

        for player in self.players:
            print("\n")
            print(player)
            player.cards[0].flip()
        while self.players[0].cards and self.players[1].cards:

            #cards not tied: a battle
            
            if self.players[0].cards[0].value != self.players[1].cards[0].value:
                input("\nNext flip: \n")
                print("\n")
                for player in self.players:
                    print(player.name, ":", player.cards[0])

                #player one wins the battle
                
                if self.players[0].cards[0].value > self.players[1].cards[0].value:
                    print("\n", self.players[1].cards[0], "belongs to", self.players[0].name, "now.")
                    self.players[0].cards.append(self.players[1].cards[0])
                    self.players[0].cards[len(self.players[0].cards)-1].flip()
                    self.players[0].cards.append(self.players[0].cards[0])
                    self.players[0].cards[len(self.players[0].cards)-1].flip()
                    self.players[0].cards.remove(self.players[0].cards[0])
                    self.players[1].cards.remove(self.players[1].cards[0])
                    
                #player two wins the battle

                elif self.players[0].cards[0].value < self.players[1].cards[0].value:
                    print("\n", self.players[0].cards[0], "belongs to", self.players[1].name, "now.")
                    self.players[1].cards.append(self.players[0].cards[0])
                    self.players[1].cards[len(self.players[1].cards)-1].flip()
                    self.players[1].cards.append(self.players[1].cards[0])
                    self.players[1].cards[len(self.players[1].cards)-1].flip()
                    self.players[0].cards.remove(self.players[0].cards[0])
                    self.players[1].cards.remove(self.players[1].cards[0])

                #display result of the war, set up next round

                for player in self.players:
                    print("\n")
                    print(player)

                    #someone's out of cards, reset game

                    if not player.cards:
                        self.deck.clear()
                        self.deck.populate()
                        self.deck.shuffle()
                        self.players[0].clear()
                        self.players[1].clear()
                        print("\nReshuffling...\n")
                        return player.name
                    else:
                        player.cards[0].flip()

            #cards tied: a war

            tempy = War_Hand("The pot")
                        
            while self.players[0].cards[0].value == self.players[1].cards[0].value:

                for player in self.players:
                    if not player.cards:
                        self.deck.clear()
                        self.deck.populate()
                        self.deck.shuffle()
                        self.players[0].clear()
                        self.players[1].clear()
                        print("\nReshuffling...\n")
                        return player.name
                    
                input("\nNext flip: \n")
                for player in self.players:
                    print(player.name, ":", player.cards[0])
                print("\nIt's a tie!\n")
                input("Flip, flip, flip...\n")
                tempy.add(self.players[0].cards[0])
                self.players[0].cards.remove(self.players[0].cards[0])
                tempy.add(self.players[1].cards[0])
                self.players[1].cards.remove(self.players[1].cards[0])

                for player in self.players:
                    if not player.cards:
                        self.deck.clear()
                        self.deck.populate()
                        self.deck.shuffle()
                        self.players[0].clear()
                        self.players[1].clear()
                        print("\nReshuffling...\n")
                        return player.name
                
                #flip the fourth or last card

                if len(self.players[0].cards) > 4 and len(self.players[1].cards) > 4:
                    self.players[0].cards[3].flip()
                    print(self.players[0].name, ":", self.players[0].cards[3])
                    self.players[1].cards[3].flip()
                    print(self.players[1].name, ":", self.players[1].cards[3])
                elif not len(self.players[0].cards) > 4:
                    self.players[0].cards[-1].flip()
                    print(self.players[0].name, ":", self.players[0].cards[-1])
                    self.players[1].cards[len(self.players[0].cards)-1].flip()
                    print(self.players[1].name, ":", self.players[1].cards[len(self.players[0].cards)-1])
                elif not len(self.players[1].cards) > 4:
                    self.players[1].cards[-1].flip()
                    print(self.players[1].name, ":", self.players[1].cards[-1])
                    self.players[0].cards[len(self.players[1].cards)-1].flip()
                    print(self.players[0].name, ":", self.players[0].cards[len(self.players[1].cards)-1])

                input("\nGah!!!\n")
                
                #determine the winner of the war

                if len(self.players[0].cards) > 4 and len(self.players[1].cards) > 4:
                    player_one = self.players[0].cards[3].value > self.players[1].cards[3].value
                    player_two = self.players[0].cards[3].value < self.players[1].cards[3].value
                elif not len(self.players[0].cards) > 4:
                    player_one = self.players[0].cards[-1].value > self.players[1].cards[len(self.players[0].cards)-1].value
                    player_two = self.players[0].cards[-1].value < self.players[1].cards[len(self.players[0].cards)-1].value
                elif not len(self.players[1].cards) > 4:
                    player_one = self.players[0].cards[len(self.players[1].cards)-1].value > self.players[1].cards[-1].value
                    player_two = self.players[0].cards[len(self.players[1].cards)-1].value < self.players[1].cards[-1].value
                else:
                    print("What the hell did you do?")

                if len(self.players[0].cards) > 4 and len(self.players[1].cards) > 4:
                    for i in range(0, 4):
                        tempy.add(self.players[1].cards[0])
                        tempy.add(self.players[0].cards[0])
                        self.players[0].cards.remove(self.players[0].cards[0])
                        self.players[1].cards.remove(self.players[1].cards[0])
                else:
                    while self.players[0].cards and self.players[1].cards:
                        tempy.add(self.players[1].cards[0])
                        tempy.add(self.players[0].cards[0])
                        self.players[0].cards.remove(self.players[0].cards[0])
                        self.players[1].cards.remove(self.players[1].cards[0])
                print(tempy)

                #player one wins the war
                
                if player_one:
                    input("\nAnd let's take a look under those Xs...")
                    for card in tempy.cards:
                        if not card.value:
                            card.flip()
                    print("\n")
                    print(tempy, "belongs to", self.players[0].name, "now.")
                    for i in range(len(tempy.cards)-1,-1,-1):
                        tempy.cards[i].flip()
                        tempy.give(tempy.cards[i], self.players[0])
                    
                #player two wins the war

                elif player_two:
                    input("\nAnd let's take a look under those Xs...")
                    for card in tempy.cards:
                        if not card.value:
                            card.flip()
                    print("\n")
                    print(tempy, "belongs to", self.players[1].name, "now.")
                    for i in range(len(tempy.cards)-1,-1,-1):
                        tempy.cards[i].flip()
                        tempy.give(tempy.cards[i], self.players[1])

                else:
                    input("\nAnother war!!!\n")
                    for player in self.players:
                        if player.cards:
                            player.cards[0].flip()
                    continue

                #display result of the war, set up next round
                
                for player in self.players:
                    print("\n")
                    print(player)

                    #someone's out of cards, reset game

                    if not player.cards:
                        self.deck.clear()
                        self.deck.populate()
                        self.deck.shuffle()
                        self.players[0].clear()
                        self.players[1].clear()
                        print("\nReshuffling...\n")
                        return player.name
                    else:
                        player.cards[0].flip()

            input("\nAnd back to the game...")

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
        gameover = game.play()
        print(gameover, "loses...sorry", gameover)
        again = Games.ask_yes_no("\nDo you want to play again? (Y/N): ")

main()
input("\n\nPress the enter key to exit.")
        
