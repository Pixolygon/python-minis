from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(v, s) for v in values for s in suits]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def _deal(self, num):
        dealt = min([self.count(), num])
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        hand = self.cards[-dealt:]
        self.cards = self.cards[:-dealt]
        return hand

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")
        else:
            shuffle(self.cards)
            return self.cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)
