# diagonals

Two players compete on a square, bi-dimensional board with n x n squares. The first player has white pieces, and the second player has black pieces. Both players have as many pieces as needed, and the board is empty at the beginning of the game.

The white player goes first, and the players take turns placing one of their pieces on an empty square. When a diagonal of squares becomes full (i.e., no empty squares remain), the player who placed the last piece on that diagonal earns points equal to the number of their pieces on the diagonal. The players accumulate points throughout the game.

The game ends when no more pieces can be placed (i.e., when there are no empty squares left on the board). The player with the most points is declared the winner.

Notes:

-   A "diagonal" does not necessarily refer to the alignments of pieces connecting the top-left corner of the board to the bottom-right corner or connecting the top-right corner to the bottom-left corner, but also includes all rows parallel to these.
-   A player may fill two diagonals by placing a single piece, in which case they accumulate points from both diagonals.
-   A diagonal must contain at least two squares, so the four corners of the board are not considered diagonals.

![enter image description here](https://cdn.discordapp.com/attachments/916017396689555496/1095643747447996507/image.png)

## run the project by launching `__main__.py`