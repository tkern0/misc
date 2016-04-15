def format_input(startStates):
    lights, x = [[False for _ in range(100)] for _ in range(100)], -1 # Makes 100y100 arrax filled with 'False', 0, 0 is in Top Left, 0, 99 in Top Right
    for ix in startStates.readlines(): # Iterates through lines
        x, y = x + 1, -1 # Could be done better
        for iy in list(ix): # Splits each line into a list and iterates through it
            y += 1
            if iy == "#": lights[x][y] = True
    return lights

def get_value(x, y, state): return state[x][y] if x > -1 and x < 100 and y > -1 and y < 100 else False
# This is it's own function because it was being weird in the other one
# Also because I get to make it a one-liner this way
# It uses > and < because using 'in range(100)'' was twice as slow

def get_neighbor_states(x, y, state):
    count = 0
    for ix in range(x - 1, x + 2): # +2 because range goes from arg1 to arg2 - 1
        for iy in range(y - 1, y + 2):
            if not (ix == x and iy == y) and get_value(ix, iy, state): count += 1
    return count

def advance_step(state):
    newLights = list(state)
    for x in range(100):
        for y in range(100):
            nstate = get_neighbor_states(x, y, state) # Slightly faster
            if state[x][y]:
                if not nstate in (2, 3): newLights[x][y] = False
            else:
                if nstate == 3: newLights[x][y] = True
    return newLights

def formated(state): # Used for debugging, prints in same formaat as input
    formatedList = ["" for _ in range(100)]
    formatedString = ""
    for x in range(len(state)):
        for y in state[x]:
            formatedList[x] += "#" if y else "."
    for i in formatedList: formatedString += "\n" + i
    return formatedString
lights = format_input(open("Day 18\\input.txt"))
print(get_neighbor_states(1, 0, lights))
# print(formated(lights))
# print()
# print(formated(advance_step(lights)))
#for _ in range(100): lights = advance_step(lights)
print(sum([lights[i].count(True) for i in range(len(lights))])) # Counts each line, stores that in a list, counts the list
