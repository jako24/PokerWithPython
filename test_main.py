import unittest
from main import Card, Deck, Player, PokerGame, HAND_RANKINGS

class TestPokerGame(unittest.TestCase):
    def setUp(self) -> None:
        self.game = PokerGame(4,5)

    def test_players(self):
        self.assertEqual(len(self.game.players),4)
        self.assertIsInstance(self.game.players[0], Player)

    def test_deal_cards(self):
        self.game.deal_cards()
        self.assertEqual(len(self.game.deck.cards), 32)
        self.assertEqual(len(self.game.players[0].hand),5)

    def test_determine_winner(self):
        self.game.players[0].hand = [Card(2, 'Hearts'), Card(3, 'Spades'),
                                     Card(4, 'Hearts'), Card(5, 'Hearts'),
                                     Card(6, 'Diamonds')]
        self.game.players[1].hand = [Card(2, 'Diamonds'), Card(3, 'Diamonds'),
                                     Card(4, 'Diamonds'), Card(5, 'Diamonds'),
                                     Card(6, 'Diamonds')]
        self.game.players[2].hand = [Card(10, 'Hearts'), Card(10, 'Spades'),
                                     Card(10, 'Clubs'), Card(5, 'Clubs'),
                                     Card(5, 'Spades')]
        self.game.players[3].hand = [Card(14, 'Hearts'), Card(13, 'Hearts'),
                                     Card(12, 'Hearts'), Card(11, 'Hearts'),
                                     Card(10, 'Hearts')]
        self.game.determine_winner()
        self.assertEqual(self.game.winner, [self.game.players[3]])

    def test_hand_rankings(self):
        self.assertGreater(HAND_RANKINGS['Royal Flush'],
                           HAND_RANKINGS['Straight Flush'])
        self.assertGreater(HAND_RANKINGS['Full House'],
                           HAND_RANKINGS['Flush'])
        self.assertGreater(HAND_RANKINGS['Two Pair'],
                           HAND_RANKINGS['One Pair'])
        self.assertGreater(HAND_RANKINGS['High Card'], 0)


if __name__ == '__main__':
    # create a test suite with all your test cases
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokerGame)

    # create a test runner with the desired number of repetitions
    runner = unittest.TextTestRunner(repeat=100)

    # run the test suite with the runner
    runner.run(suite)