import random

#BOARD_WIDTH = get_int("What is the width of the grid? ")
#BOARD_HEIGHT = get_int("What is the height of the grid? ")
BOARD_WIDTH, BOARD_HEIGHT = 8, 5
ANSI = False
DIRECTIONS = (("W", "A", "S", "D"), ("8", "4", "2", "6"),
              ("U", "L", "D", "R"), ("^", "<", "V", ">"))
INPUT_TYPE = 0
# The different acceptable inputs types, change the constant to switch
# 0: WASD
# 1: 8426 (numpad)
# 2: ULDR
# 3: ^<v>

# Gets a Width/Height Value for the program
# Can handle invalid inputs
def get_int(prompt):
    while True:
        try:
            result = int(input(prompt))
            if result <= 0: raise ValueError
        except ValueError:
            print("Please enter a positive number")
        else:
            return result

# Returns a set of coordinates 1 square in each cardinal direction from 'coords'
def get_neighbours(coords):
    return set(((coords[0] + 1, coords[1]), (coords[0] - 1, coords[1]),
                (coords[0], coords[1] + 1), (coords[0], coords[1] - 1)))

# Prints the current state of the board
# This includes each player's visited cells
# Top left is (0,0), x increaces to the right and y increaces downwards
# Can provide a set of squares to highlight
# Specify ansi=True to enable colours on terminals that support it
# Will colour "A" red and "B" cyan, and make a square bold if it is highlighted
# Specify 'bg' as an ansi code to colour the table background
# This does nothing if ansi=False
def print_board(board, path_a, path_b, highlights=set(), ansi=False, bg="\033[0;0m"):
    print(("", bg)[ansi] + "+-----" * BOARD_WIDTH + "+")
    for y in range(BOARD_HEIGHT):
        row1 = row2 = row3 = "|"
        for x in range(BOARD_WIDTH):
            if (x, y) in highlights:
                row1 += ("", "\033[1;1m")[ansi] + str(board[(x, y)]) + ("", "\033[1;21m")[ansi] + "....|"
                if (x, y) in path_a:
                    row2 += ("..A..|", "..\033[1;1m\033[1;31mA\033[1;21m" + bg + "..|")[ansi]
                else:
                    row2 += ".....|"
                if (x, y) in path_b:
                    row3 += ("....B|", "....\033[1;1m\033[1;36mB\033[1;21m" + bg + "|")[ansi]
                else:
                    row3 += ".....|"
            else:
                row1 += str(board[(x, y)]) + "    |"
                if (x, y) in path_a:
                    row2 += ("  A  |", "  \033[1;31mA" + bg + "  |")[ansi]
                else:
                    row2 += "     |"
                if (x, y) in path_b:
                    row3 += ("    B|", "    \033[1;36mB" + bg + "|")[ansi]
                else:
                    row3 += "     |"
        print(("", bg)[ansi] + row1)
        print(row2)
        print(row3)
        print("+-----" * BOARD_WIDTH + ("+", "+\033[0;0m")[ansi])

# Creates a random game board
# Specify ensure_solveable=False to disable checking if the board is solveable
# This speeds up creation, but may return impossible boards
def create_board(ensure_solveable=True):
    board = {}
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if x == y == 0:
                board[(0, 0)] = random.choice(range(6))
            else:
                if y == 0:
                    # Inelegant weighted average
                    # Cells of similar height to their neighbours are twice as
                    #  likely to be picked
                    board[(x, y)] = random.choice(list(filter(lambda x: x in range(6),
                                          list(range(6))
                                          + [board[(x-1, 0)]]
                                          + [board[(x-1, 0)] - 1]
                                          + [board[(x-1, 0)] + 1])))
                elif x == 0:
                    board[(x, y)] = random.choice(list(filter(lambda x: x in range(6),
                                          list(range(6))
                                          + [board[(0, y-1)]]
                                          + [board[(0, y-1)] - 1]
                                          + [board[(0, y-1)] + 1])))
                else:
                    # Need to use a set here to not duplicate values
                    # The previous two only check one cell, so there is never
                    #  going to be any overlap
                    board[(x, y)] = random.choice(list(filter(lambda x: x in range(6),
                                          list(range(6))
                                          + list(set(
                                            [board[(x-1, y)]]
                                          + [board[(x-1, y)] - 1]
                                          + [board[(x-1, y)] + 1]
                                          + [board[(x, y-1)]]
                                          + [board[(x, y-1)] - 1]
                                          + [board[(x, y-1)] + 1])))))
    if ensure_solveable:
        # Useing A* to try find a path, to work out if the board is solveable
        # Only defining these vars here incase ensure_solveable=False, to save a
        #  bit of RAM
        closed_set = set()
        open_set = set([(0, 0)])
        goal = (BOARD_WIDTH - 1, BOARD_HEIGHT - 1)
        # BOARD_WIDTH*BOARD_HEIGHT is the worst case scenario
        g_score = {(x, y):BOARD_WIDTH*BOARD_HEIGHT for x in range(BOARD_WIDTH)
                                                   for y in range(BOARD_HEIGHT)}
        f_score = {(x, y):BOARD_WIDTH*BOARD_HEIGHT for x in range(BOARD_WIDTH)
                                                   for y in range(BOARD_HEIGHT)}
        g_score[(0, 0)] = 0
        f_score[(0, 0)] = BOARD_WIDTH + BOARD_HEIGHT
        current = (0, 0)
        while open_set:
            if current == goal:
                return board
            open_set.remove(current)
            closed_set.add(current)
            neighbours = get_neighbours(current)
            for neighbour in neighbours:
                if (neighbour in board and
                    board[current] - 1 <= board[neighbour] and
                    board[current] + 1 >= board[neighbour] and
                    neighbour not in closed_set):
                    if neighbour not in open_set:
                        open_set.add(neighbour)
                    new_g_score = (g_score[current]
                                   + abs(current[0] - neighbour[0])
                                   + abs(current[1] - neighbour[1]))
                    if new_g_score < g_score[neighbour]:
                        g_score[neighbour] = new_g_score
                        f_score[neighbour] = (new_g_score
                                              + abs(neighbour[0] - goal[0])
                                              + abs(neighbour[1] - goal[1]))
            # There's probably a nicer way to do this
            min_f_score = BOARD_WIDTH*BOARD_HEIGHT
            next_square = current
            for coord in open_set:
                if min_f_score >= f_score[coord]:
                    next_square = coord
                    min_f_score = f_score[coord]
            current = next_square
        # Should only get here if open_set empties without getting to goal, only
        #  if the board is impossible to solve
        return create_board()
    # If ensure_solveable=False
    return board

board = create_board()
coord_a, coord_b = (0, 0), (BOARD_WIDTH - 1, BOARD_HEIGHT - 1)
path_a, path_b = set([coord_a]), set([coord_b])
score_a = score_b = 0
turn_a = True
winner = set()
while True:
    # First find the current player's valid moves
    # This is done here so that we can print them, and used later to check if
    #  someone lost
    valid_moves = set()
    for neighbour in get_neighbours((coord_b, coord_a)[turn_a]):
            if (neighbour in board and
                neighbour not in (path_b, path_a)[turn_a]):
                # This needs to be here incase 'neighbour' is off the board
                if (board[(coord_b, coord_a)[turn_a]] - 1 <= board[neighbour] and
                    board[(coord_b, coord_a)[turn_a]] + 1 >= board[neighbour]):
                    valid_moves.add(neighbour)
    print_board(board, path_a, path_b, valid_moves, ansi=ANSI)
    # First check if anyone finished
    # This is just here for a nicer printing order
    if coord_a == (BOARD_WIDTH - 1, BOARD_HEIGHT - 1) and "A" not in winner:
        print("Player A finished")
        winner.add("A")
    if coord_b == (0, 0) and "B" not in winner:
        print("Player B finished")
        winner.add("B")
    if winner == set(("A", "B")):
        break
    # If there are no valid moves then the current player must have lost
    # This is always different to the last player, who might just have won, so
    #  the same player cannot win and lose in the same turn
    if not valid_moves:
        print("Player " + ("B", "A")[turn_a] + " can't move")
        break
    # Now, if there is still a player, print the score and ask for a move
    print("Player A: " + str(score_a))
    print("Player B: " + str(score_b))
    print("Player " + ("B", "A")[turn_a] + ", where would you like to move? ["
          + "".join(DIRECTIONS[INPUT_TYPE]) +"]")
    # A bunch of error checking
    while True:
        try:
            result = input("> ")
            if result.upper() not in DIRECTIONS[INPUT_TYPE]:
                print("Invalid input")
                raise ValueError
            direction = DIRECTIONS[INPUT_TYPE].index(result.upper())
            current_coords = (coord_b, coord_a)[turn_a]
            if direction == 0: # Up
                move = (current_coords[0], current_coords[1] - 1)
            elif direction == 1: # Left
                move = (current_coords[0] - 1, current_coords[1])
            elif direction == 2: # Down
                move = (current_coords[0], current_coords[1] + 1)
            elif direction == 3: # Right
                move = (current_coords[0] + 1, current_coords[1])
            if move not in board:
                print("Can't move off the board to " + str(move))
                raise ValueError
            if move in (path_b, path_a)[turn_a]:
                print("Can't move into a visited square at " + str(move))
                raise ValueError
            if (board[current_coords] - 1 > board[move] or
                board[current_coords] + 1 < board[move]):
                print("Can't move from height " + str(board[current_coords])
                       + " to " + str(board[move]))
                raise ValueError
        except ValueError:
            pass
        else:
            break
    # Yay valid move
    if turn_a:
        score_a += 1
        if board[move] > board[coord_a]:
            score_a += 1
        path_a.add(move)
        coord_a = move
    else:
        score_b += 1
        if board[move] > board[coord_b]:
            score_b += 1
        path_b.add(move)
        coord_b = move
    # If someone has finished they no longer need their turn
    if not winner:
        turn_a = not turn_a
# At this point the game is over
print("")
print("Game Over")
print("Final Scores:")
print("Player A: " + str(score_a))
print("Player B: " + str(score_b))
if score_a == score_b:
    print("Draw")
else:
    print("Player " + ("B", "A")[score_a > score_b] + " wins")