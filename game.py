class Game:
    def __init__(self, size: int) -> None:
        # generate board as a 2d array of dimension size*size containing only ". "
        self.board = [[". " for i in range(size)] for i in range(size)]
        self.size = size  # size of the board
        self.player = 1  # player turn
        self.player1score = 0
        self.player2score = 0

    def DisplayBoard(self) -> None:
        '''
        Display the board
        '''
        s = "\n"  # start with a new line
        for i in range(len(self.board)):  # for each row
            # add the row number and the row
            s += str(i+1)+" | " + " ".join(self.board[i]) + "\n"
        s += "  " + "-"*(len(self.board)*3) + "\n"  # add the bottom line
        # add the column numbers
        s += "    " + "  ".join([str(i+1) for i in range(len(self.board))])
        print(s)  # display the board

    def SwitchPlayerTurn(self) -> None:
        '''
        switch player turn
        '''
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def AskCoords(self) -> str:
        '''
        Ask the player for coordinates and return them
        '''
        return input("Player %d enter your move (x <space> y): " % self.player)

    def AddPoints(self, posx: int, posy: int) -> None:
        '''
        This function detects the diagonals and adds the number of pawn (of the player) in diagonals to the player score
        '''

        if posx > posy:            #
            root = (posx-posy, 0)  # here we get the root of every ↖ diagonal
        else:                      #
            root = (0, posy-posx)  #

        if posx+posy < self.size:                          #
            root2 = (posx+posy, 0)  # here we get the root of every ↙ diagonal
        else:                                              #
            root2 = (self.size-1, posx+posy-(self.size-1))

        # out is used to store every pawn of the ↖ diagonal in a list
        # for that we use a list comprehension which put every y +i and x +i in the list until we reach the end of the board
        out = [self.board[root[1] + i][root[0] + i]
               for i in range(self.size - max(root))]

        # out2 is used to store every pawn of the ↙ diagonal in a list
        # for that we use a list comprehension which put every y +i and x -i in the list until we reach the end of the board
        out2 = [self.board[root2[1] + i][root2[0] - i]
                for i in range(self.size) if root2[0] - i >= 0 and root2[1] + i < self.size]

        for i in [out, out2]:  # check for every diagonal
            # if the diagonal is complete and not a corner (the lenght of a corner diagonal is 1)
            if not ". " in i and len(i) > 1:
                if self.player == 1:
                    # we add the number of pawns of the player to the score
                    self.player1score += i.count("X ")
                else:
                    # we add the number of pawns of the player to the score
                    self.player2score += i.count("O ")

    def DisplayScore(self) -> None:
        '''
        Display the score
        '''
        print("Player 1: %d" % self.player1score)
        print("Player 2: %d" % self.player2score)

    def IsMovePossible(func):
        '''
        Decorator to check if the move is possible
        '''

        def inner(self, posx: int, posy: int):

            if type(posx) != int or type(posy) != int:
                return False                           # check if the input is an integer

            # check if the input is in the board and if the position is empty
            elif posx < 0 or posx >= self.size or posy < 0 or posy >= self.size or self.board[posy][posx] != ". ":
                return False
            return func(self, posx, posy)
        return inner

    @IsMovePossible
    def InputPawn(self, posx: int, posy: int) -> None:
        '''
        input a pawn in the board at the given position
        posx: x position
        posy: y position
        '''
        if self.player == 1:              #
            self.board[posy][posx] = "X "
        else:                             # use the appropriate pawn
            self.board[posy][posx] = "O "

        self.AddPoints(posx, posy)  # add the points
        self.SwitchPlayerTurn()  # switch player turn

    def Play(self) -> None:
        '''
        Play the game
        '''
        self.DisplayBoard()
        while any(". " in row for row in self.board) == True:  # while there is an empty position

            coords = self.AskCoords()  # ask the player for coordinates
            # convert the coordinates to index of the board array
            posx, posy = int(coords.split(
                " ")[0]) - 1, int(coords.split(" ")[1]) - 1

            # while the move is not possible the coordinates are asked again
            while self.InputPawn(posx, posy) == False:
                print("Invalid input/position please try again")
                coords = self.AskCoords()
                posx, posy = int(coords.split(
                    " ")[0]) - 1, int(coords.split(" ")[1]) - 1

            self.DisplayBoard()
            self.DisplayScore()
        # Just a check to see which player won
        if self.player1score > self.player2score:
            print("Player 1 wins!")
        elif self.player1score < self.player2score:
            print("Player 2 wins!")
        else:
            print("It's a tie!")
