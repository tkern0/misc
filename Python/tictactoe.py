def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def get_square(board, player):
    print("Player {} please select a square".format(player))
    while True:
        try:
            choice = int(input("> "))
            if not choice in range(1, 10):
                raise ValueError
            if not board[choice - 1] == " ":
                raise ValueError
        except ValueError:
            print("Please enter a valid input")
        else:
            break
    return choice - 1

def check_winner(board):
    if board[0] == board[1] == board[2]:
        if not board[0] == " ":
            return board[0]
    if board[3] == board[4] == board[5]:
        if not board[3] == " ":
            return board[3]
    if board[6] == board[7] == board[8]:
        if not board[6] == " ":
            return board[6]
    if board[0] == board[3] == board[6]:
        if not board[0] == " ":
            return board[0]
    if board[1] == board[4] == board[7]:
        if not board[1] == " ":
            return board[1]
    if board[2] == board[5] == board[8]:
        if not board[2] == " ":
            return board[2]
    if board[0] == board[4] == board[8]:
        if not board[0] == " ":
            return board[0]
    if board[2] == board[4] ==  board[6]:
        if not board[2] == " ":
            return board[2]
    return not " " in board 

board = [" "]*9
player_X = True

while True:
    print_board(board)
    if player_X:
        board[get_square(board, "X")] = "X"
    else:
        board[get_square(board, "O")] = "O"
    winner = check_winner(board)
    if winner:
        break
    player_X = not player_X
print_board(board)
if winner == True:
    print("Draw")
else:
    print("{} wins".format(winner))