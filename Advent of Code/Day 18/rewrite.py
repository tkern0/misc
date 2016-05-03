size = 6
steps = 100
path = "Day 18\\test.txt"

def format_input(startState):
    state, x = [[False for _ in range(size + 2)] for _ in range(size + 2)], 0 # 0, 0 is in Top Left, 0, 99 in Top Right
    for ix in startState.readlines():
        x, y = x + 1, 0 # Could be done better
        for iy in list(ix):
            y += 1
            if iy == "#": state[x][y] = True
    return state

def formated(state): # Used for debugging, returns string in same format as input
    formatedList = ["" for _ in range(size)]
    formatedString = ""
    trimmed = []
    for i in state[1:-1]: trimmed.append(i[1:-1]) # Removes always-false border
    for ix in range(size):
        for iy in trimmed[ix]:
            formatedList[ix] += "#" if iy else "."
    for i in formatedList: formatedString += "\n" + i
    return formatedString

def count_neighbors(x, y, state):
    count = 0
    for ix in range(x - 1, x + 2):
        for iy in range(y - 1, y + 2):
            if not (ix == x and iy == y) and state[ix][iy]: count += 1
    return count

def advance(state):
    newState = list(state)
    for ix in range(1, size + 1):
        for iy in range(1, size + 1):
            neighbors = count_neighbors(ix, iy, state)
            if state[ix][iy]:
                if not neighbors in (2, 3): newState[ix][iy] = False
            else:
                if neighbors == 3: newState[ix][iy] = True
    return newState

state = format_input(open("Day 18\\test.txt"))
# for _ in range(steps): state = advance(state)
print(formated(state))
print()
state = advance(state)
print(formated(state))
