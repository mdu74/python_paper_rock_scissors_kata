class GameValidator:
    def conditionsForLoss(myMove, opponentsMoves):
        return (myMove == "Sciccors" and opponentsMoves == "Rock") or (myMove == "Paper" and opponentsMoves == "Sciccors") or (myMove == "Rock" and opponentsMoves == "Paper")

    def conditionsForWin(myMove, opponentsMoves):
        return (myMove == "Rock" and opponentsMoves == "Sciccors") or (myMove == "Sciccors" and opponentsMoves == "Paper") or (myMove == "Paper" and opponentsMoves == "Rock")
    
    def conditionsForDraw(myMove, opponentsMoves):
        return (myMove == "Rock" and opponentsMoves == "Rock") or (myMove == "Paper" and opponentsMoves == "Paper") or (myMove == "Sciccors" and opponentsMoves == "Sciccors")