# Import required modules
import pgzrun, pygame, pgzero
from pgzero.builtins import *

# Import from python files
import Board
import Units
import Dice

# Game states and global variables
# 0 menu, 1 game over, 2 player1, 3 player2
game_state = 2
move_state = False
actor_pos = 0
last_move_x = 0
last_move_y = 0

# Active tiles for scanning
active_move_tile = []
active_shoot_tile = []


# A function to determine if a click token can be moved,
# and how far they are able to move
def start_action(player, pos):
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
            shoot_check(pos, each)

    # Check if there is no locked tokens
    if lock_state is False:
        # Loops though player tokens
        for each in player:

            movement_check(pos, each)
            shoot_check(pos, each)


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


def shoot_check(pos, each):
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

                        scan_x = each[1].weapons.max_range
                        scan_range = scan_x * 2 + 1

                        for row in range(scan_range):
                            scan_y = each[1].weapons.max_range
                            for col in range(scan_range):
                                if game_state == 2:
                                    shoot_scan(x, y, scan_x, scan_y, player2)
                                elif game_state == 3:
                                    shoot_scan(x, y, scan_x, scan_y, player1)
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
    for item in active_move_tile:
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
    for item in active_move_tile:
        # Loop though the boards x axis
        for x in range(board_x):
            # Loop though boards y axis
            for y in range(board_y):
                # Check if click collided with this tile
                if item.collidepoint(board[x][y].pos):
                    # Remove board scan from this pos
                    un_move_scan(item.pos, x, y)

    end_turn(swap_turn)


def end_attack(atk_player, def_player, pos):
    # Loop though all active tiles
    global game_state
    swap_turn = False

    for item in active_shoot_tile:
        # Check mouse pos collides with an active tile
        if item.collidepoint(pos):
            for token in atk_player:
                if token[0].pos == actor_pos:
                    att_dice = token[1].weapons.atk_colour
                    print(att_dice)
                    att_no = token[1].quantity * token[1].weapons.number_dice
                    print(att_no)
                    for each in def_player:
                        if each[0].collidepoint(pos):
                            print(each[1].name)
                            def_dice = each[1].def_colour
                            print(def_dice)

                            att_outcome = roll_att(att_dice, att_no, def_dice)
                            print(att_outcome)

                            if att_outcome is False:
                                print("Attack Blocked")
                            else:
                                for damage in range(att_outcome):
                                    print("Attack hit")
                                    each[1].hp -= 1
                                    att_outcome -= 1
                                    if each[1].hp <= 0:
                                        each[1].quantity -= 1
                                        if each[1].quantity <= 0:
                                            print(each[1].name + " is killed")
                                            # Loop though the boards x axis
                                            for x in range(board_x):
                                                # Loop though boards y axis
                                                for y in range(board_y):
                                                    # Check if click collided with this tile
                                                    if each[0].collidepoint(board[x][y].pos):
                                                        board_occupied[x][y] = 0
                                            each[1].state = 1
                                            def_player.remove(each)
                                            break

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
    for item in active_shoot_tile:
        # Loop though the boards x axis
        for x in range(board_x):
            # Loop though boards y axis
            for y in range(board_y):
                # Check if click collided with this tile
                if item.collidepoint(board[x][y].pos):
                    # Remove board scan from this pos
                    un_move_scan(item.pos, x, y)

    end_turn(swap_turn)


# Function to check range of movement and if there are any collisions
def move_scan(x, y, rang_x, rang_y):
    # Set global variables for function
    global board_occupied
    global move_state
    global active_move_tile
    move_state = True
    try:
        # Check if tile is occupied first
        if board_occupied[x + rang_x][y + rang_y] == 0:
            # Added select tile to list if tile is empty
            active_move_tile.append(board[x + rang_x][y + rang_y])
            # print(active_tile[-1]) Debug

            # Change the last tile added to active tile list to green
            active_move_tile[-1] = Actor('move_square')
            active_move_tile[-1].pos = (((x + rang_x) * 68) + 54, ((y + rang_y) * 68) + 54)
            # Check if this tile is on the board
            if active_move_tile[-1].collidepoint(board[x + rang_x][y + rang_y].pos):
                # Update board with new tile
                board[x + rang_x][y + rang_y] = active_move_tile[-1]
            else:
                active_move_tile.pop()
    except:
        print("")


def shoot_scan(x, y, scan_x, scan_y, player):
    global board_occupied
    global move_state
    global active_shoot_tile
    move_state = True
    try:
        # Check if tile is occupied first
        if board_occupied[x + scan_x][y + scan_y] == 1:
            # Added select tile to list if tile is empty
            active_shoot_tile.append(board[x + scan_x][y + scan_y])
            # print(active_tile[-1]) Debug

            # Change the last tile added to active tile list to green
            active_shoot_tile[-1] = Actor('shoot_square')
            active_shoot_tile[-1].pos = (((x + scan_x) * 68) + 54, ((y + scan_y) * 68) + 54)
            # Check if this tile is on the board
            if active_shoot_tile[-1].collidepoint(board[x + scan_x][y + scan_y].pos):
                for each in player:
                    if each[0].pos == active_shoot_tile[-1].pos:
                        # Update board with new tile
                        board[x + scan_x][y + scan_y] = active_shoot_tile[-1]
            else:
                active_shoot_tile.pop()
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


def roll_att(att_dice, att_no, def_dice):
    if att_dice == 0:
        att_value = Dice.roll_white_atk_dice(att_no)
    elif att_dice == 1:
        att_value = Dice.roll_black_atk_dice(att_no)
    elif att_dice == 2:
        att_value = Dice.roll_red_atk_dice(att_no)

    if def_dice == 0:
        def_value = Dice.roll_black_def_dice(att_no)
    elif def_dice == 1:
        def_value = Dice.roll_red_def_dice(att_no)

    print("Rolled Attack: " + str(att_value) + " Rolled Defence: " + str(def_value))
    print("Attack Damage: " + str(att_value - def_value))

    if att_value > def_value:
        return att_value - def_value
    else:
        return False


def end_turn(swap_turn):
    global game_state
    global player1
    global player2

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


# Function to determine what to do on a mouse click
def on_mouse_down(pos):
    # Set global variables
    global actor_pos
    global last_move_x
    global last_move_y
    global active_move_tile
    global active_shoot_tile
    global move_state

    # Check if there is a token selected
    if move_state is False:
        # Check who's turn it is
        if game_state == 2:
            # Start movement
            start_action(player1, pos)
        elif game_state == 3:
            start_action(player2, pos)
    else:
        if game_state == 2:
            end_movement(player1, pos)
            end_attack(player1, player2, pos)
        elif game_state == 3:
            end_movement(player2, pos)
            end_attack(player2, player1, pos)

        active_move_tile = []
        active_shoot_tile = []


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


# Function to draw to the screen
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
