#poker plays
# @author: Schkliba
import random

import numpy as np

class Card:

    def __init__(self, color, rank, mark):
        self.color = color
        self.rank = rank
        self.mark = mark

    def is_suited(self, other_card):
        return other_card.color == self.color

    def __eq__(self, other):
        return other.mark == self.mark

    def __lt__(self, other):
        return other.rank < self.rank

    def __str__(self):
        return "C-"+str(self.rank) +"-"+str(self.color)+"("+str(self.mark)+")"

    def __repr__(self):
        return self.mark

class Deck:

    cards = "23456789TJQKA"
    colors = "dhsc"

    def __init__(self):
        self.deck = []
        self.refresh()

    def refresh(self):
        self.deck = []
        for c in range(len(self.colors)):
            for r in range(len(self.cards)):
                self.deck += [Card(c, r, self.cards[r]+self.colors[c])]

    def shuffle(self):
        shuffled = []
        while len(self.deck) > 0:
            choice = random.randint(0,len(self.deck)-1)
            card = self.deck.pop(choice)
            shuffled.append(card)
        self.deck = shuffled

    def tuck_card(self, mark):
        i = self.deck.index(Card(0,0, mark))
        return self.deck.pop(i)

    def deal_card(self):
        return self.deck.pop()

    def __repr__(self):
        return self.deck.__str__()

def game_walk(hero_cards, villains_cnt: int):
    hero = []
    deck = Deck()
    villains = []
    for v in range(villains_cnt):
        villains.append([])
    for m in hero_cards:
        hero.append(deck.tuck_card(m))
    deck.shuffle()
    for v in range(2*villains_cnt):
        villains[v % villains_cnt].append(deck.deal_card())
    table_cards = [deck.deal_card() for _ in range(5)]

    return hero, villains, table_cards

class Patterns:
    @staticmethod
    def flush(hand):
        colors = list(map(lambda x: x.color, hand))
        colors, counts = np.unique(colors, return_counts=True)
        print(counts >= 5)
        return np.any(counts >= 5)

    @staticmethod
    def royal_flush(hand):
        sorted_hand = sorted(hand)
        return sorted_hand[0] > 11, sorted_hand[1] > 10


def did_hero_win(hero, villains, table_cards):
    hero_hand = hero + table_cards
    villain_hands = [v + table_cards for v in villains]
    f = Patterns.flush(hero_hand)
    print(f)



if __name__ == '__main__':
    h, vs, tbl = game_walk(["Qh", "Kh"], 2)
    did_hero_win(h, vs, tbl)

