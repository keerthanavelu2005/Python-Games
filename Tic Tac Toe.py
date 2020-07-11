
board = ["*", "*", "*",
         "*", "*", "*",
         "*", "*", "*"]
game_still_on = True
winner = None
current_player = "H"
def play_game():
    display_board()
    while game_still_on:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()
    if winner == "H" or winner == "I":
        print(winner + " won")
    elif winner == None:
        print("Tie")

def display_board():
    print("\n")
    print(board[0] + " --" + board[1] + " -- " + board[2] + "     1 -- 2 -- 3")
    print(board[3] + " --" + board[4] + " -- " + board[5] + "     4 -- 5 -- 6")
    print(board[6] + " -- " + board[7] + " -- " + board[8] + "     7 -- 8 -- 9")
    print("\n")

def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a correct from 1-9: ")
        position = int(position) - 1
        if board[position] == "*":
            valid = True
        else:
            print("Invalid number.choose another one.")
    board[position] = player
    display_board()

def check_if_game_over():
    checks_for_winner()
    checks_for_tie()

def checks_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():

    global game_still_on
    row_1 = board[0] == board[1] == board[2] != "*"
    row_2 = board[3] == board[4] == board[5] != "*"
    row_3 = board[6] == board[7] == board[8] != "*"
    if row_1 or row_2 or row_3:
        game_still_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_columns():

    global game_still_on

    column_1 = board[0] == board[3] == board[6] != "*"
    column_2 = board[1] == board[4] == board[7] != "*"
    column_3 = board[2] == board[5] == board[8] != "*"

    if column_1 or column_2 or column_3:
        game_still_on = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None

def check_diagonals():

    global game_still_on

    diagonal_1 = board[0] == board[4] == board[8] != "*"
    diagonal_2 = board[2] == board[4] == board[6] != "*"

    if diagonal_1 or diagonal_2:
        game_still_on = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None

def checks_for_tie():
    global game_still_on
    if "-" not in board:
        game_still_on = False
        return True
    else:
        return False

def flip_player():
    global current_player
    if current_player == "H":
        current_player = "I"
    elif current_player == "I":
        current_player = "H"
play_game()