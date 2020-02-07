import pgzrun

WIDTH = 1280
HEIGHT = 720

board_x = 10
board_y = 10

board = [[0] * board_x for i in range(board_y)]

print(board)

for x in range(board_x):
    for y in range(board_y):
        print("Assigning: Board X:" + str(x) + " Y: " + str(y))
        board[x][y] = Actor('blank_token')
        board[x][y].pos = (x * 68) + 54, (y * 68) + 54


def draw():
    screen.clear()
    for row in range(board_x):
        for col in range(board_y):
            board[row][col].draw()


pgzrun.go()
