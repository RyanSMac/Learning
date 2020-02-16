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

# Active tiles for scanning
active_tile = []


# A function to determine if a click token can be moved,
# and how far they are able to move
def start_movement(player, pos):
    # Declares global variables for function,
    # and resets functions lock state
    global actor_pos
    global last_move_x
    global last_move_y
    lock_state = False

    # Loops though player tokens
    for each in player:
        # Check if this token is locked and it has actions left
        if each[1].locked is True and each[1].action_taken != 0:
            # Change the functions lock state to stop any other token from being activated
            lock_state = True

            movement_check(pos, each)

    # Check if there is no locked tokens
    if lock_state is False:
        # Loops though player tokens
        for each in player:

            movement_check(pos, each)


def movement_check(pos, each):
    global actor_pos
    global last_move_x
    global last_move_y

    # Create function from here
    # Check if this token collides with the mouse click
    if each[0].collidepoint(pos):

        # check number of actions is equal to or less than total action,
        # but more than zero actions
        if each[1].action_value >= each[1].action_taken > 0:
            # Loop though the boards x axis
            for x in range(board_x):
                # Loop though the board y axis
                for y in range(board_y):

                    # After check to make sure right token is selected,
                    # store the active tokens actor position
                    actor_pos = each[0].pos

                    # Check which board tile this token collides with
                    if each[0].collidepoint(board[x][y].pos):
                        # Loop though this tokens move range

                        last_move_x = x
                        last_move_y = y

                        scan_x = each[1].movement_value
                        scan_range = each[1].movement_value * 2 + 1

                        for row in range(scan_range):
                            scan_y = each[1].movement_value
                            for col in range(scan_range):
                                move_scan(x, y, scan_x, scan_y)
                                scan_y -= 1
                            scan_x -= 1


# A function to check if a valid move has been made,
# execute move selected,
# reset movement scan,
# and update game state
def end_movement(player, pos):
    # Set global states for function
    global game_state
    swap_turn = False

    # Loop though all active tiles
    for item in active_tile:
        # Check mouse pos collides with an active tile
        if item.collidepoint(pos):
            # Loop though all token in current players turn
            for token in player:
                # Check token matches active actor pos
                if token[0].pos == actor_pos:
                    # Update board occupation,
                    # remove token from current pos
                    board_occupied[last_move_x][last_move_y] = 0
                    # Move active token to clicked tile
                    token[0].pos = item.pos
                    # Loop though x axis
                    for x in range(board_x):
                        # Loop though y axis
                        for y in range(board_y):
                            # Check which board tile was clicked on
                            if item.collidepoint(board[x][y].pos):
                                # Update occupied space
                                board_occupied[x][y] = 1
                    # Set the lock state to true
                    token[1].locked = True
                    # Decrease the number of action for this token by one
                    token[1].action_taken -= 1
                    # Check if this token has used all its actions
                    if token[1].action_taken == 0:
                        # Change the swap_turn state to true
                        swap_turn = True
                        # Change the token lock state to False
                        token[1].locked = False

    # Loop though all tiles in active tiles
    for item in active_tile:
        # Loop though the boards x axis
        for x in range(board_x):
            # Loop though boards y axis
            for y in range(board_y):
                # Check if click collided with this tile
                if item.collidepoint(board[x][y].pos):
                    # Remove board scan from this pos
                    un_move_scan(item.pos, x, y)

    # Check swap state and change game state if true
    if swap_turn is True:
        if game_state == 2:
            game_state = 3
        elif game_state == 3:
            game_state = 2

    # Set reset value
    reset = True
    # Loop though player 1 token
    for each in player1:
        # Check if token has action left
        if each[1].action_taken > 0:
            # Update reset
            reset = False
    # Loop though player 2 token
    for each in player2:
        # Check if token has action left
        if each[1].action_taken > 0:
            # Update reset
            reset = False

    # If all token have used all there moves reset the phase
    if reset is True:
        # Loop though token in player 1
        for each in player1:
            # Reset action value and unlock token
            each[1].action_taken = each[1].action_value
            each[1].locked = False
        # Loop though token in player 2
        for each in player2:
            # Reset action value and unlock token
            each[1].action_taken = each[1].action_value
            each[1].locked = False


# Function to check range of movement and if there are any collisions
def move_scan(x, y, rang_x, rang_y):
    # Set global variables for function
    global board_occupied
    global move_state
    move_state = True
    try:
        # Check if tile is occupied first
        if board_occupied[x + rang_x][y + rang_y] == 0:
            # Added select tile to list if tile is empty
            active_tile.append(board[x + rang_x][y + rang_y])
            # print(active_tile[-1]) Debug

            # Change the last tile added to active tile list to green
            active_tile[-1] = Actor('move_square')
            active_tile[-1].pos = (((x + rang_x) * 68) + 54, ((y + rang_y) * 68) + 54)
            # Check if this tile is on the board
            if active_tile[-1].collidepoint(board[x + rang_x][y + rang_y].pos):
                # Update board with new tile
                board[x + rang_x][y + rang_y] = active_tile[-1]
            else:
                active_tile.pop()
    except:
        print("")


# Function to remove drawn movement area
def un_move_scan(pos, x, y):
    # Set global states for function
    global move_state
    # reset move state to False
    move_state = False

    # replace green tile with blank tile
    board[x][y] = Actor('blank_token')
    board[x][y].pos = pos


# Function to determine what to do on a mouse click
def on_mouse_down(pos):
    # Set global variables
    global actor_pos
    global last_move_x
    global last_move_y
    global active_tile
    global move_state

    # Check if there is a token selected
    if move_state is False:
        # Check who's turn it is
        if game_state == 2:
            # Start movement
            start_movement(player1, pos)
        elif game_state == 3:
            start_movement(player2, pos)
    else:
        if game_state == 2:
            end_movement(player1, pos)
        elif game_state == 3:
            end_movement(player2, pos)

        active_tile = []


# Display size
WIDTH = 1280
HEIGHT = 720

# Display title
TITLE = "Star Wars Legion Lite"

# The boards size
board_x = 9
board_y = 9

# Generate the board and occupied board list
board = [[0] * board_x for i in range(board_y)]
board_occupied = [[0] * board_x for i in range(board_y)]

# Asigns white tiles to all board spaces
Board.white_board(board, board_x, board_y)

# Builds armys for player 1 and 2
player1 = Units.set_up_rebel()
player2 = Units.set_up_imperial()

# Places tokens on the board and occupies those spaces
player1[0][0].pos = board[1][0].pos
board_occupied[1][0] = 1
player1[1][0].pos = board[7][0].pos
board_occupied[7][0] = 1
player1[2][0].pos = board[4][0].pos
board_occupied[4][0] = 1

player2[0][0].pos = board[1][8].pos
board_occupied[1][8] = 1
player2[1][0].pos = board[7][8].pos
board_occupied[7][8] = 1
player2[2][0].pos = board[4][8].pos
board_occupied[4][8] = 1


# Funtion to draw to the screen
def draw():
    # Clear the screen
    screen.clear()
    # Loop though board
    for row in range(board_x):
        for col in range(board_y):
            # Draw each board tile
            board[row][col].draw()

    # Draw all players tokens
    for each in player1:
        each[0].draw()

    for each in player2:
        each[0].draw()


pgzrun.go()
