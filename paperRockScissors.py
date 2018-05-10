from game_validator import GameValidator

class PaperRockScissors(object):
    def Play(myMove, opponentsMoves):
        if GameValidator.conditionsForLoss(myMove, opponentsMoves):
            return "Loose"
        elif GameValidator.conditionsForWin(myMove, opponentsMoves):
            return "Win"
        elif GameValidator.conditionsForDraw(myMove, opponentsMoves):
            return "Draw"