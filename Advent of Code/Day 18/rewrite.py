size = 6
start = open("Advent of Code/Day 18/test.txt")

def format_input(startState):
    lights, x = [[False for _ in range(size + 2)] for _ in range(size + 2)], 0 # 0, 0 is in Top Left, 0, 99 in Top Right
    for ix in startState.readlines():
        x, y = x + 1, 0 # Could be done better
        for iy in list(ix):
            y += 1
            if iy == "#": lights[x][y] = True
    return lights

def formated(state): # Used for debugging, returns string in same format as input
    formatedList = ["" for _ in range(size)]
    formatedString = ""
    for x in range(1, size + 1):
        for y in state[x][1:-1]:
            formatedList[x] += "#" if y else "."
    for i in formatedList: formatedString += "\n" + i
    return formatedString

print(formated(format_input(start)))
