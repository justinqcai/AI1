from random import shuffle
from strategy import Strategy

EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'Black', WHITE: 'White'}
SILENT = False

# To refer to neighbor squares we can add a direction to a square.
UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11

DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)
game = Strategy()
board = game.initial_board()
player = WHITE
X_STRATEGY = game.alphabeta_search(3)
O_STRATEGY = game.human_strategy(3)

def play(strategy_X, strategy_O, first=WHITE):
    """
    Plays strategy_X vs. strategy_O, beginning with first
    in one game. Returns X, O or TIE as a result (string)

    The functions make_move, next_player and terminal_test are
    implemented elsewhere (e.g. in core.py). The current implementation
    uses a 9-char string as the state, but that is not exposed at this level.
    """
    global board
    global player
    print(game.print_board(board))
    
    current_strategy = {WHITE: strategy_X, BLACK: strategy_O}
    while player is not None:
        move = current_strategy[player](player, board)
        print(player, move)
        board = game.make_move(move, player, board)
        player = game.next_player(board, player)
        print(game.print_board(board))


    if game.score(WHITE, board) > 0:
        print("WHITE WINS")
    elif game.score(WHITE, board) < 0:
        print("BLACK WINS")
    else:
        print("TIE")

if __name__ == "__main__":
    # board = game.initial_board()
    # player = WHITE
    # while player is not None:
    #     moves = game.legal_moves(player, board)
    #     shuffle(moves)
    #     board = game.make_move(moves[0], player, board)
    #     player = game.next_player(board, player)
    #     print(game.print_board(board))
    # if game.score(WHITE, board) > 0:
    #     print("WHITE WINS")
    # elif game.score(WHITE, board) < 0:
    #     print("BLACK WINS")
    # else:
    #     print("TIE")
    play(X_STRATEGY, O_STRATEGY, first=WHITE)
