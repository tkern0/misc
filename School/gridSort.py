import random

# Gets a Width/Height Value for the program
# Can handle invalid inputs
def getInt(prompt):
    while True:
        try:
            result = int(input(prompt))
            if result < 2 or result % 2 == 1: raise ValueError
        except ValueError:
            print("Please enter an even, positive number")
        else:
            break
    return result

# Prints an ascii representation of the grid
# Top-left is (0, 0)
# Colours "A" red, "B" cyan and "C" green
# Specify ansi=False to disable colours for terminals that do not support it
def print_grid(grid, ansi=True):
    if ansi: print("  " + " " * GRID_W + "\033[1;36mB\033[0;0m")
    else: print("  " + " " * GRID_W + "B")
    print("  " + "+-" * GRID_W + "+")
    for row in range(GRID_H):
        currentRow = "  |"
        for value in grid[row]:
            if ansi:currentRow += {"A":"\033[1;31m", "B":"\033[1;36m", "C":"\033[0;32m"}.get(value, "") + str(value) + "\033[0;0m|"
            else: currentRow += str(value) + "|"
        print(currentRow)
        if row == GRID_H / 2 - 1:
            if ansi: print("\033[1;31mA\033[0;0m " + "+-" * GRID_W + "+ \033[0;32mC\033[0;0m")
            else: print("A " + "+-" * GRID_W + "+ C")
        else:
            print("  " + "+-" * GRID_W + "+")
    print("")

# Gets the distance from cell (x, y) to either A, B or C
def get_distance(x, y, goal):
    if goal == "A":
        if x >= GRID_H / 2:
            return int(x - GRID_H / 2 + y)
        else:
            return int(GRID_H / 2 - x - 1 + y)
    elif goal == "B":
        if y >= GRID_W / 2:
            return int(x + y - GRID_W / 2)
        else:
            return int(x + GRID_W / 2 - y - 1)
    elif goal == "C":
        if x >= GRID_H / 2:
            return int(x - GRID_H / 2 + GRID_W - y - 1)
        else:
            return int(GRID_H / 2 - x - 1 + GRID_W - y - 1)
    else: raise ValueError

# Sorts the grid
# By default will iterate until no more improvements are found or 1000 iterations
# Iterations can be specifed (set to 0 for default behaviour)
# If verbose mode is enabled shows each swap and the reasons for it
# On average, O(w, h) = 2(wh)^2
def sort_grid(grid, iterations=0, verbose=False):
    # Setup the master loop so we will sort multiple times if necessary
    for _ in range(iterations if iterations > 0 else 1000):
        fails = 0
        # Loop through each cell (c1)
        for x in range(GRID_H):
            for y in range(GRID_W):
                bx, by = x, y
                bImprove = 0
                # Loop through each cell again (c2)
                for cx in range(GRID_H):
                    for cy in range(GRID_W):
                        # Work out the improvement if we swap c1 with c2, and if it's the best so far record it
                        improve = get_distance(x, y, grid[x][y]) + get_distance(cx, cy, grid[cx][cy]) - get_distance(x, y, grid[cx][cy]) - get_distance(cx, cy, grid[x][y])
                        if bImprove < improve:
                            bImprove = improve
                            bx, by = cx, cy
                if bImprove == 0: fails += 1
                # Swap c1 with the best c2, if they are not the same cell
                if not x == bx and not y == by:
                    swap=grid[x][y]
                    grid[x][y]=grid[bx][by]
                    grid[bx][by]=swap
                # If necessary print debug info
                if verbose:
                    if bImprove == 0:
                        print("No possible improvements for ({}, {})".format(x, y))
                    else:
                        print("Swapping ({},{}), {}, with ({}, {}), {}".format(x, y, grid[bx][by], bx, by, grid[x][y]))
                        print("Before: {} + {}, After: {} + {}".format(get_distance(x, y, grid[bx][by]), get_distance(bx, by, grid[x][y]), get_distance(x, y, grid[x][y]), get_distance(bx, by, grid[bx][by])))
                        print_grid(grid, False)
        # If we didn't find any improvements break out of the master loop
        if fails == GRID_H * GRID_W: break
        if verbose: print("Looping")
    return grid

GRID_W, GRID_H = getInt("What is the width of the grid? "), getInt("What is the height of the grid? ")

# for _ in range(10): print_grid(sort_grid([[random.choice("ABC") for _ in range(GRID_W)] for _ in range(GRID_H)]), False)
grid = [[random.choice("ABC") for _ in range(GRID_W)] for _ in range(GRID_H)]
print_grid(grid, False)
grid = sort_grid(grid, 0, True)
print_grid(grid, False)
