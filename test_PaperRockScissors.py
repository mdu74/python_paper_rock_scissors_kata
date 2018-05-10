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
    
    def test_Play_GivenChosenSciccors_WhenOpponentChooseRock_ShouldReturnLoose(self):
        # Arrange
        myMoves = "Sciccors"
        opponentsMoves = "Rock"
        # Act
        result = PaperRockScissors.Play(myMoves, opponentsMoves)
        # Assert
        expected = "Loose"
        self.assertEqual(result, expected)

    def test_Play_GivenChosenSciccors_WhenOpponentChoosePaper_ShouldReturnWin(self):
        # Arrange
        myMoves = "Sciccors"
        opponentsMoves = "Paper"
        # Act
        result = PaperRockScissors.Play(myMoves, opponentsMoves)
        # Assert
        expected = "Win"
        self.assertEqual(result, expected)

    def test_Play_GivenChosenPaper_WhenOpponentChooseScissors_ShouldReturnLoose(self):
        # Arrange
        myMoves = "Paper"
        opponentsMoves = "Sciccors"
        # Act
        result = PaperRockScissors.Play(myMoves, opponentsMoves)
        # Assert
        expected = "Loose"
        self.assertEqual(result, expected)