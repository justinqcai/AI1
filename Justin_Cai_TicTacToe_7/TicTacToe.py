import random

def printb(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
#    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def inletter():
    letter = input("Do you want to be X or O? ").upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def again():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def move(board, letter, x):
    board[x] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def get_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def random_move(board, movesList):
    possible = []
    for i in movesList:
        if isSpaceFree(board, i):
            possible.append(i)

    if len(possible) != 0:
        return random.choice(possible)
    else:
        return None

def post_move(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            move(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            move(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    x = random_move(board, [1, 3, 7, 9])
    if x != None:
        return x

    if isSpaceFree(board, 5):
        return 5

    return random_move(board, [2, 4, 6, 8])

def full(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

while True:
    board = [' '] * 10
    playerLetter, computerLetter = inletter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            printb(board)
            x = get_move(board)
            move(board, playerLetter, x)

            if isWinner(board, playerLetter):
                printb(board)
                print('You won!')
                gameIsPlaying = False
            else:
                if full(board):
                    printb(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            x = post_move(board, computerLetter)
            move(board, computerLetter, x)

            if isWinner(board, computerLetter):
                printb(board)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if full(board):
                    printb(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    break