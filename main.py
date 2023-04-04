# POKER
import random

HAND_RANKINGS = {
    "Royal Flush": 10,
    "Straight Flush": 9,
    "Four of a Kind": 8,
    "Full House": 7,
    "Flush": 6,
    "Straight": 5,
    "Three of a Kind": 4,
    "Two Pair": 3,
    "One Pair": 2,
    "High Card": 1
}

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        value_str = str(self.value)
        if self.value == 11:
            value_str = "Jack"
        elif self.value == 12:
            value_str = "Queen"
        elif self.value == 13:
            value_str = "King"
        elif self.value == 14:
            value_str = "Ace"
        suit_str = self.suit.capitalize()
        return "{} of {}".format(value_str, suit_str)

class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        self.cards = []
        for suit in ["Spades", "Hearts", "Diamonds", "Clubs"]:
            for value in range(2, 15):
                self.cards.append(Card(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            raise Exception("No cards left in the deck!")
        return self.cards.pop(0)

class Player():
    def __init__(self, name):
        self.name = name
        self.hand =[]

    def add_cards(self, card):
        self.hand.append(card)

    def remove_cards(self, index):
        self.hand.pop(index)

    def show_hand(self):
        for card in self.hand:
            print(card)

class PokerGame():
    def __init__(self, num_players, num_cards):
        self.num_players = num_players
        self.num_cards = num_cards
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        self.create_players()
        self.winner = []

    def create_players(self):
        for i in range(self.num_players):
            name = "Player {}".format(i + 1)
            self.players.append(Player(name))

    def deal_cards(self):
        for i in range(self.num_cards):
            for player in self.players:
                card = self.deck.draw()
                player.add_cards(card)

    def play(self):
        self.deal_cards()
        for player in self.players:
            print("{}:".format(player.name))
            player.show_hand()
            print()
        self.determine_winner()

    def compare_cards(self, card1, card2):
        max_card = max([card1, card2], key=lambda card: (card[1], card[0]))
        return max_card

    def determine_winner(self):
        hand_scores = []
        for player in self.players:
            hand_score = 0
            hand = player.hand
            hand.sort(key=lambda card: card.value, reverse=True)
            values = [card.value for card in hand]
            suits = [card.suit for card in hand]
            is_flush = all(suit == suits[0] for suit in suits)
            is_straight = all(values[i] == values[i+1]+1 for i in range(len(values)-1))
            if is_flush and is_straight and values[0] == 14:
                hand_score = HAND_RANKINGS["Royal Flush"]
            elif is_flush and is_straight:
                hand_score = HAND_RANKINGS["Straight Flush"]
            else:
                value_counts = {value: values.count(value) for value in values}
                max_count = max(value_counts.values())
                if max_count == 4:
                    hand_score = HAND_RANKINGS["Four of a Kind"]
                elif max_count == 3:
                    if 2 in value_counts.values():
                        hand_score = HAND_RANKINGS["Full House"]
                    else:
                        hand_score = HAND_RANKINGS["Three of a Kind"]
                elif max_count == 2:
                    if list(value_counts.values()).count(2) == 2:
                        hand_score = HAND_RANKINGS["Two Pair"]
                    else:
                        hand_score = HAND_RANKINGS["One Pair"]
                else:
                    if is_flush:
                        hand_score = HAND_RANKINGS["Flush"]
                    elif is_straight:
                        hand_score = HAND_RANKINGS["Straight"]
                    else:
                        hand_score = HAND_RANKINGS["High Card"]
            hand_scores.append(hand_score)
        max_score = max(hand_scores)

        # check for draw
        if hand_scores.count(max_score) > 1:
            for i, score in enumerate(hand_scores):
                if score == max_score:
                    # get the highest card in the hand
                    highest_card = max(self.players[i].hand, key=lambda card: card.value)
                    # compare the highest cards
                    for j, player in enumerate(self.players):
                        if player.hand[-1].value == highest_card.value:
                            self.winner.append(player)
                            break
        else:
            for i, score in enumerate(hand_scores):
                if score == max_score:
                    self.winner.append(self.players[i])
        if len(self.winner) == 1:
            print("{} wins with a {}!".format(self.winner[0].name, list(HAND_RANKINGS.keys())[list(HAND_RANKINGS.values()).index(max_score)]))
        else:
            print("Players {} tie!".format(", ".join(p.name for p in self.winner)))


game = PokerGame(4, 5)
print(game.play())