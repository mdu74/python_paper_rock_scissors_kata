import unittest
from paperRockScissors import PaperRockScissors

class TestPaperRockScissors(unittest.TestCase):
    def test_Play_GivenEmptyString_ShouldReturnEmptyString(self):
        # Arrange
        moves = ""
        # Act
        result = PaperRockScissors.Play(moves)
        # Assert
        expected = ""
        self.assertEqual(result, expected)