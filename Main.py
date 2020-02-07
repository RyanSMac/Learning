import Board, Units
import pgzrun


def on_mouse_down(pos):
    for x in range(board_x):
        for y in range(board_y):
            if board[x][y].collidepoint(pos):
                board[x][y] = Actor('move_square')
                board[x][y].pos = (x * 68) + 54, (y * 68) + 54


WIDTH = 1280
HEIGHT = 720

board_x = 10
board_y = 10

board = [[0] * board_x for i in range(board_y)]
board_occupied = [[0] * board_x for i in range(board_y)]

print(board)

Board.white_board(board, board_x, board_y)

player1 = Units.set_up_rebel()
player2 = Units.set_up_imperial()

player1[0][0].pos = board[2][0].pos
board_occupied[2][0] = 1
player1[1][0].pos = board[4][0].pos
board_occupied[4][0] = 1
player1[2][0].pos = board[7][0].pos
board_occupied[7][0] = 1

player2[0][0].pos = board[2][9].pos
board_occupied[2][9] = 1
player2[1][0].pos = board[4][9].pos
board_occupied[4][9] = 1
player2[2][0].pos = board[7][9].pos
board_occupied[7][9] = 1


def draw():
    screen.clear()
    for row in range(board_x):
        for col in range(board_y):
            board[row][col].draw()

    for each in player1:
        each[0].draw()

    for each in player2:
        each[0].draw()


pgzrun.go()
