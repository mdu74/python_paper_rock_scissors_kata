import unittest
from paperRockScissors import PaperRockScissors

class TestPaperRockScissors(unittest.TestCase):
    def test_Play_GivenChosenRock_WhenOpponentChooseSciccors_ShouldReturnWin(self):
        # Arrange
        myMoves = "Rock"
        opponentsMoves = "Sciccors"
        # Act
        result = PaperRockScissors.Play(myMoves, opponentsMoves)
        # Assert
        expected = "Win"
        self.assertEqual(result, expected)