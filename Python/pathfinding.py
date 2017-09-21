import random

BOARD_WIDTH, BOARD_HEIGHT = 50, 50
GOAL = (BOARD_WIDTH - 1, BOARD_HEIGHT - 1)
def get_valid_neighbours(coords, board):
    o_coords = set()
    for i in ((coords[0] + 1, coords[1]), (coords[0] - 1, coords[1]),
                   (coords[0], coords[1] + 1), (coords[0], coords[1] - 1)):
        if i in board:
            if not board[i] == "X":
                o_coords.add(i)
    return o_coords

def print_board(board):
    print("+---" * BOARD_WIDTH + "+")
    for y in range(BOARD_HEIGHT - 1, -1, -1):
        row = "|"
        for x in range(BOARD_WIDTH):
            row += board[(x, y)]*3 + "|"
        print(row)
        print(row)
        print("+---" * BOARD_WIDTH + "+")

def get_path(board, p_square, coords):
    if coords == (0, 0):
        board[(0, 0)] = "\033[1;36mS\033[0;0m"
        return board
    else:
        if coords in p_square:
            board[p_square[coords]] = "\033[1;31mO\033[0;0m"
        else:
            print(coords)
        return get_path(board, p_square, p_square[coords])

def distance(c1, c2): return int(((c1[0] - c2[0])**2 +  (c1[1] - c2[1])**2)**0.5)


for _ in range(10):
    board = {(x, y):" " for y in range(BOARD_HEIGHT) for x in range(BOARD_WIDTH)}
    board[(0, 0)] = "\033[1;36mS\033[0;0m"
    board[GOAL] = "\033[1;32mG\033[0;0m"

    for square in board:
        if random.randint(0, 100) < 10:
            board[square] = "X"
    # for y in range(5):
        # board[(1, y)] = "X"
    # for y in range(1, 6):
        # board[(4, y)] = "X"

    closed_set = set()
    open_set = set(((0, 0),))
    p_square = {(x, y):() for y in range(BOARD_HEIGHT) for x in range(BOARD_WIDTH)}
    p_square[(0,0)] = (0,0)

    g_score = {(x, y):BOARD_WIDTH*BOARD_HEIGHT for y in range(BOARD_HEIGHT) for x in range(BOARD_WIDTH)}
    g_score[(0, 0)] = 0
    f_score = {(x, y):BOARD_WIDTH*BOARD_HEIGHT for y in range(BOARD_HEIGHT) for x in range(BOARD_WIDTH)}
    f_score[(0, 0)] = distance((0, 0), GOAL)
    c_coord = (0, 0)

    while open_set:
        min_f_score = BOARD_WIDTH*BOARD_HEIGHT
        next_square = c_coord
        for coord in open_set:
            if min_f_score >= f_score[coord]:
                next_square = coord
                min_f_score = f_score[coord]
        c_coord = next_square
        if c_coord == GOAL:
            break
        open_set.remove(c_coord)
        closed_set.add(c_coord)
        for neighbour in get_valid_neighbours(c_coord, board):
            if not neighbour in closed_set:
                if neighbour not in open_set:
                    open_set.add(neighbour)
                if g_score[c_coord] + 1 < g_score[neighbour]:
                    g_score[neighbour] = g_score[c_coord] + 1
                    p_square[neighbour] = c_coord
                    f_score[neighbour]= g_score[neighbour] + distance(neighbour, GOAL)
    print_board(get_path(board, p_square, GOAL))