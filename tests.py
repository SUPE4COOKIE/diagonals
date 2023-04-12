from game import Game
def test1() -> bool:
    '''
    Just test if the Pawns are going to the right place
    '''
    b = Game(5)
    b.InputPawn(0,0)
    b.InputPawn(1,1)
    b.InputPawn(2,2)
    b.InputPawn(3,3)
    b.InputPawn(4,4)
    return b.board == [['X ', '. ', '. ', '. ', '. '], ['. ', 'O ', '. ', '. ', '. '], ['. ', '. ', 'X ', '. ', '. '], ['. ', '. ', '. ', 'O ', '. '], ['. ', '. ', '. ', '. ', 'X ']]

def test2() -> bool:
    '''
    Test if corners aren't counted as diagonals
    '''
    b = Game(5)
    b.InputPawn(0,0)
    b.InputPawn(0,4)
    b.InputPawn(4,0)
    b.InputPawn(4,4)
    return (b.player1score == 0 and b.player2score == 0)

def test3() -> bool:
    '''
    Test if the score is right for a simple diagonal
    '''
    b = Game(5)
    b.InputPawn(0,1)
    b.InputPawn(1,2)
    b.InputPawn(2,3)
    b.InputPawn(3,4)

    return (b.player1score == 0 and b.player2score == 2)

def test4() -> bool:
    '''
    Test collision between 2 diagonals
    '''
    b = Game(5)
    #first diagonal
    b.InputPawn(0,0)
    b.InputPawn(1,1)
    b.InputPawn(2,2)
    b.InputPawn(3,3)
    b.InputPawn(4,4)
    #second diagonal
    b.InputPawn(0,4)
    b.InputPawn(1,3)
    b.InputPawn(3,1)
    b.InputPawn(4,0)
    return (b.player1score == 6 and b.player2score == 0)

if __name__ == "__main__":
    print("Test 1: " + str(test1()))
    print("Test 2: " + str(test2()))
    print("Test 3: " + str(test3()))
    print("Test 4: " + str(test4()))

