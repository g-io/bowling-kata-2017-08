from unittest import TestCase
from kata.game import Game


class TestGame(TestCase):
    def test_zero_pins_returns_zero(self):
        game = Game()
        for i in range(0, 20):
            game.roll(0)
        assert(game.score() == 0)

    def test_arbitrary_pins_without_spares_and_strikes_returns_correct_sum(self):
        game = Game()
        for i in range(0, 20):
            game.roll(1)
        assert game.score() == 20, "score should be 20 but its {}".format(game.score())

    def test_calculation_of_spare_bonus(self):
        game = Game()
        game.roll(6)
        game.roll(4)
        game.roll(1)
        assert game.score() == 12, "score should be 12 but its {}".format(game.score())

    #def test_arbitrary_pins_without_spares_and_strikes_returns_correct_sum(self):
    #    game = Game()
    #    for i in range(0, 19):
    #        game.roll(1)
    #    assert(game.score() == 20)

