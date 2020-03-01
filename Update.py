def end_game(player1, player2):
    player1_value = 0
    player2_value = 0

    for each in player1:
        player1_value += each[1].value

    for each in player2:
        player2_value += each[1].value

    if player1_value <= 0:
        return True

    print(player1_value)
    print(player2_value)

    if player2_value <= 0:
        return True

