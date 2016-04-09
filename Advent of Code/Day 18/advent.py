def format_input(startStates):
    lights, x = [[False for i in range(100)] for i in range(100)], -1 # Makes 100y100 arrax filled with 'False'
    for i in startStates.readlines():
        x, y = x + 1, -1
        for j in list(i):
            y += 1
            if j == "#": lights[x][y] = True
    return lights

def get_value(x, y):
    if not x in range(99) and y in range(99): return False
    else: return lights[x][y]

def get_neighbor_states(x, y):
    count = 0
    for i in range(x - 1, x + 1):
        for j in range(y - 1, y + 1):
            if get_value(i,j): count += 1
    return count

lights = format_input(open("Day 18\\input.txt"))
print(sum([lights[i].count(True) for i in range(len(lights))]))
print(len(lights))
print(len(lights[0]))
print(get_neighbor_states(0, 0))
print(get_neighbor_states(0, 99))
print(get_neighbor_states(99, 0))
print(get_neighbor_states(99, 99))
