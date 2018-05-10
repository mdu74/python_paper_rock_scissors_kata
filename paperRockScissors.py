class PaperRockScissors(object):
    def Play(myMove, opponentsMoves):
        if (myMove == "Sciccors" and opponentsMoves == "Rock") or (myMove == "Paper" and opponentsMoves == "Sciccors") or (myMove == "Rock" and opponentsMoves == "Paper"):
            return "Loose"
        elif (myMove == "Rock" and opponentsMoves == "Sciccors") or (myMove == "Sciccors" and opponentsMoves == "Paper") or (myMove == "Paper" and opponentsMoves == "Rock"):
            return "Win"
        elif (myMove == "Rock" and opponentsMoves == "Rock") or (myMove == "Paper" and opponentsMoves == "Paper") or (myMove == "Sciccors" and opponentsMoves == "Sciccors"):
            return "Draw"