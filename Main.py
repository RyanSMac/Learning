import pgzrun, pygame, pgzero
from pgzero.builtins import *

import Board
import Units

# 0 menu, 1 game over, 2 player1, 3 player2
game_state = 2
move_state = False
actor_pos = 0
last_move_x = 0
last_move_y = 0


active_tile = []


def move_scan(x, y, rang_x, rang_y, board_occupied):
    global move_state
    move_state = True
    try:
        # Check if tile is occupied first
        if board_occupied[x + rang_x][y + rang_y] == 0:
            active_tile.append(board[x + rang_x][y + rang_y])
            # print(active_tile[-1])
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
    if move_state is False:
        for each in player1:
            if each[0].collidepoint(pos):
                if game_state == 2:
                    if each[1].action_taken < each[1].action_value:
                        for x in range(board_x):
                            for y in range(board_y):
                                # storing actor position
                                actor_pos = each[0].pos

                                if each[0].collidepoint(board[x][y].pos):
                                    for rang in range(1, each[1].movement_value + 1):
                                        last_move_x = x
                                        last_move_y = y
                                        print(x, y)

                                        move_scan(x, y, rang, 0, board_occupied)
                                        move_scan(x, y, -rang, 0, board_occupied)
                                        move_scan(x, y, 0, rang, board_occupied)
                                        move_scan(x, y, 0, -rang, board_occupied)
                                        move_scan(x, y, rang, rang, board_occupied)
                                        move_scan(x, y, rang, -rang, board_occupied)
                                        move_scan(x, y, -rang, rang, board_occupied)
                                        move_scan(x, y, -rang, -rang, board_occupied)

                                        move_scan(x, y, rang, 1, board_occupied)
                                        move_scan(x, y, -rang, 1, board_occupied)
                                        move_scan(x, y, rang, -1, board_occupied)
                                        move_scan(x, y, -rang, -1, board_occupied)

                                        move_scan(x, y, 1, rang, board_occupied)
                                        move_scan(x, y, 1, -rang, board_occupied)
                                        move_scan(x, y, -1, rang, board_occupied)
                                        move_scan(x, y, -1, -rang, board_occupied)

        for each in player2:
            if each[0].collidepoint(pos):
                if game_state == 3:
                    if each[1].action_taken < each[1].action_value:
                        for x in range(board_x):
                            for y in range(board_y):
                                # storing actor position
                                actor_pos = each[0].pos
                                last_move_x = x
                                last_move_y = y
                                print(x, y)

                                if each[0].collidepoint(board[x][y].pos):
                                    for rang in range(1, each[1].movement_value + 1):

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

    else:
        global active_tile
        for item in active_tile:
            if item.collidepoint(pos):
                if game_state == 2:
                    for token in player1:
                        if token[0].pos == actor_pos:
                            board_occupied[last_move_x][last_move_y] = 0
                            token[0].pos = item.pos
                            for x in range(board_x):
                                for y in range(board_y):
                                    if item.collidepoint(board[x][y].pos):
                                        board_occupied[x][y] = 1

        for item in active_tile:
            for x in range(board_x):
                for y in range(board_y):
                    if item.collidepoint(board[x][y].pos):
                        un_move_scan(item.pos, x, y)
        active_tile = []


WIDTH = 1280
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
