class PaperRockScissors(object):
    def Play(myMove, opponentsMoves):
        if myMove == "Sciccors" and opponentsMoves == "Rock":
            return "Loose"
        elif myMove == "Paper" and opponentsMoves == "Sciccors":
            return "Loose"
        elif myMove == "Rock" and opponentsMoves == "Sciccors":
            return "Win"
        elif myMove == "Sciccors" and opponentsMoves == "Paper":
            return "Win"