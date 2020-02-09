# Import required modules
import pgzrun, pygame, pgzero
from pgzero.builtins import *

# Import from python files
import Board
import Units

# Game states and global variables
# 0 menu, 1 game over, 2 player1, 3 player2
game_state = 2
move_state = False
actor_pos = 0
last_move_x = 0
last_move_y = 0


active_tile = []


def start_movement(player, pos):
    global actor_pos
    global last_move_x
    global last_move_y
    lock_state = False

    for each in player:
        if each[1].locked is True and each[1].action_taken != 0:
            lock_state = True
            if each[0].collidepoint(pos):

                if each[1].action_value >= each[1].action_taken > 0:
                    for x in range(board_x):
                        for y in range(board_y):
                            # storing actor position
                            actor_pos = each[0].pos

                            if each[0].collidepoint(board[x][y].pos):
                                for rang in range(1, each[1].movement_value + 1):
                                    last_move_x = x
                                    last_move_y = y
                                    print(x, y)

                                    move_scan(x, y, rang, 0)
                                    move_scan(x, y, -rang, 0)
                                    move_scan(x, y, 0, rang)
                                    move_scan(x, y, 0, -rang)
                                    move_scan(x, y, rang, rang)
                                    move_scan(x, y, rang, -rang)
                                    move_scan(x, y, -rang, rang)
                                    move_scan(x, y, -rang, -rang)

                                    move_scan(x, y, rang, 1)
                                    move_scan(x, y, -rang, 1)
                                    move_scan(x, y, rang, -1)
                                    move_scan(x, y, -rang, -1)

                                    move_scan(x, y, 1, rang)
                                    move_scan(x, y, 1, -rang)
                                    move_scan(x, y, -1, rang)
                                    move_scan(x, y, -1, -rang)

    if lock_state is False:
        for each in player:
            if each[0].collidepoint(pos):

                if each[1].action_value >= each[1].action_taken > 0:
                    for x in range(board_x):
                        for y in range(board_y):
                            # storing actor position
                            actor_pos = each[0].pos

                            if each[0].collidepoint(board[x][y].pos):
                                for rang in range(1, each[1].movement_value + 1):
                                    last_move_x = x
                                    last_move_y = y
                                    print(x, y)

                                    move_scan(x, y, rang, 0)
                                    move_scan(x, y, -rang, 0)
                                    move_scan(x, y, 0, rang)
                                    move_scan(x, y, 0, -rang)
                                    move_scan(x, y, rang, rang)
                                    move_scan(x, y, rang, -rang)
                                    move_scan(x, y, -rang, rang)
                                    move_scan(x, y, -rang, -rang)

                                    move_scan(x, y, rang, 1)
                                    move_scan(x, y, -rang, 1)
                                    move_scan(x, y, rang, -1)
                                    move_scan(x, y, -rang, -1)

                                    move_scan(x, y, 1, rang)
                                    move_scan(x, y, 1, -rang)
                                    move_scan(x, y, -1, rang)
                                    move_scan(x, y, -1, -rang)


def end_movement(player, pos):
    global game_state
    swap_turn = False

    for item in active_tile:
        if item.collidepoint(pos):
            for token in player:
                if token[0].pos == actor_pos:
                    board_occupied[last_move_x][last_move_y] = 0
                    token[0].pos = item.pos
                    for x in range(board_x):
                        for y in range(board_y):
                            if item.collidepoint(board[x][y].pos):
                                board_occupied[x][y] = 1
                    token[1].locked = True
                    token[1].action_taken -= 1
                    if token[1].action_taken == 0:
                        swap_turn = True
                        token[1].locked = False

    for item in active_tile:
        for x in range(board_x):
            for y in range(board_y):
                if item.collidepoint(board[x][y].pos):
                    un_move_scan(item.pos, x, y)

    if swap_turn is True:
        if game_state == 2:
            game_state = 3
        elif game_state == 3:
            game_state = 2

    reset = True
    for each in player1:
        if each[1].action_taken > 0:
            reset = False
    for each in player2:
        if each[1].action_taken > 0:
            reset = False

    if reset is True:
        for each in player1:
            each[1].action_taken = each[1].action_value
            each[1].locked = False
        for each in player2:
            each[1].action_taken = each[1].action_value
            each[1].locked = False

    print(str(player1[0][1].name) + "1" + "Moves Remaining: " + str(player1[0][1].action_taken) + "/" + str(player1[0][1].action_value))
    print(str(player1[1][1].name) + "2" + "Moves Remaining: " + str(player1[1][1].action_taken) + "/" + str(player1[1][1].action_value))
    print(str(player1[2][1].name) + "1" + "Moves Remaining: " + str(player1[2][1].action_taken) + "/" + str(player1[2][1].action_value))

    print(str(player2[0][1].name) + "1" + "Moves Remaining: " + str(player2[0][1].action_taken) + "/" + str(player2[0][1].action_value))
    print(str(player2[1][1].name) + "2" + "Moves Remaining: " + str(player2[1][1].action_taken) + "/" + str(player2[1][1].action_value))
    print(str(player2[2][1].name) + "1" + "Moves Remaining: " + str(player2[2][1].action_taken) + "/" + str(player2[2][1].action_value))


# Function to check range of movement and if there are any collisions
def move_scan(x, y, rang_x, rang_y):
    global board_occupied
    global move_state
    move_state = True
    try:
        # Check if tile is occupied first
        if board_occupied[x + rang_x][y + rang_y] == 0:
            # Added select tile to list if tile is empty
            active_tile.append(board[x + rang_x][y + rang_y])
            # print(active_tile[-1]) Debug

            active_tile[-1] = Actor('move_square')
            active_tile[-1].pos = (((x + rang_x) * 68) + 54, ((y + rang_y) * 68) + 54)
            if active_tile[-1].collidepoint(board[x + rang_x][y + rang_y].pos):
                board[x + rang_x][y + rang_y] = active_tile[-1]
            else:
                active_tile.pop()
    except:
        print("")


def un_move_scan(pos, x, y):
    global move_state
    move_state = False

    board[x][y] = Actor('blank_token')
    board[x][y].pos = pos


def on_mouse_down(pos):
    global actor_pos
    global last_move_x
    global last_move_y
    global active_tile
    global move_state

    if move_state is False:
        if game_state == 2:
            start_movement(player1, pos)
        elif game_state == 3:
            start_movement(player2, pos)
    else:
        if game_state == 2:
            end_movement(player1, pos)
        elif game_state == 3:
            end_movement(player2, pos)

        active_tile = []


WIDTH = 720
HEIGHT = 720

board_x = 10
board_y = 10

board = [[0] * board_x for i in range(board_y)]
board_occupied = [[0] * board_x for i in range(board_y)]

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
