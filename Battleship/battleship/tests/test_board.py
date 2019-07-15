import unittest
from app.gameboard import GameBoard

class TestBoard(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_grid_created(self):
        game = GameBoard()
        self.assertIsInstance(game.grid, list, "grid property is a list")
