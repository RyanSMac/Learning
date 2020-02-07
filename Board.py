from pgzero.builtins import Actor


def white_board(board, board_x, board_y):
    for x in range(board_x):
        for y in range(board_y):
            # print("Assigning: Board X:" + str(x) + " Y: " + str(y))
            board[x][y] = Actor('blank_token')
            board[x][y].pos = (x * 68) + 54, (y * 68) + 54


def token_setup(board, board_x, board_y):
    board[0][2]
