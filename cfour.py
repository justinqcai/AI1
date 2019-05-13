EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'Black', WHITE: 'White'}

# To refer to neighbor squares we can add a direction to a square.
UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

class ConnectCore:
    def squares(self):
        """List all the valid squares on the board."""
        return [i for i in range(11, 68) if 1 <= (i % 10) <= 6]

    def initial_board(self):
        """Create a new board with the initial black and white positions filled."""
        board = [EMPTY] * 80
        for i in self.squares():
            board[i] = EMPTY
        return board
    def print_board(self,board):
        """Get a string representation of the board."""
        rep = ''
        rep += '  %s\n' % ' '.join(map(str, list(range(1, 8))))
        for row in range(1, 7):
            begin, end = 10 * row + 1, 10 * row + 8
            rep += '%d %s\n' % (row, ' '.join(board[begin:end]))
        return rep

    def is_valid(self, move):
        """Is move a square on the board?"""
        if move in self.squares():
        	return True
        return False
        
    def opponent(self, player):
        """Get player's opponent piece."""
        if player is BLACK:
            return WHITE
        elif player is WHITE:
            return BLACK

    def find_bracket(self, square, player, board, direction):
        """
        Find a square that forms a bracket with `square` for `player` in the given
        `direction`.  Returns None if no such square exists.
        Returns the index of the bracketing square if found
        """
        count = 0
        while(board[square] == player):
            square = square + direction
            count = count+1
        if(count>=4):
            return True
        return False
    
    def terminal_test(self, board):
        if self.any_legal_move(board) == False:
            return "TIE"
        for i in self.squares():
            for j in DIRECTIONS:
                if self.find_bracket(i, BLACK, board, j):
                    return BLACK
                if self.find_bracket(i, WHITE, board, j):
                    return WHITE
        return None
    
    def is_legal(self, move, board):
        """Is this a legal move for the player?"""
        if move not in range(1, 8):
            return False
        if board[move+10] != EMPTY:
            return False
        return True
    
    ### Making moves

    # When the player makes a move, we need to update the board and flip all the
    # bracketed pieces.

    def make_move(self, move, player, board):
        """Update the board to reflect the move by the specified player."""
        row = 60
        while(board[row+move] != EMPTY):
            row -= 10
        board[row + move] = player
        return board

    def legal_moves(self, board):
        """Get a list of all legal moves for player, as a list of integers"""
        moveList = []
        for i in range(1, 8):
            if self.is_legal(i, board):
                movesList.append(i)
        return moveList

    def any_legal_move(self, board):
        """Can player make any moves? Returns a boolean"""
        for i in range(1, 8):
            if board[10 + i] == EMPTY:
                return True
        return False
    
    def human_strategy(self):
        return lambda player, board: self.human(player, board)
    
    def human(self, player, board):
        s = input("What column (1-7)?")
        while(self.is_legal(s, board) == False):
            s = input("Invalid column, try again")
        return s
    class IllegalMoveError(Exception):
        def __init__(self, player, move, board):
            self.player = player
            self.move = move
            self.board = board

        def __str__(self):
            return '%s cannot move to square %d' % (PLAYERS[self.player], self.move)
            
test = ConnectCore()
board =  test.initial_board()
print(test.print_board(board))
player = WHITE
while test.terminal_test(board) is None:
    move = test.human_strategy()(player, board)
    test.make_move(move, player, board)
    player = test.opponent(player)
    print(test.print_board(board))
print test.terminal_test(board)
