dirs = open('input.txt').read()
x = 0
y = 0
houses = []
for i in range(0,len(dirs)):
    if (x, y) not in houses: houses.append((x, y))
    if dirs[i] == "^": y += 1
    elif dirs[i] == ">": x += 1
    elif dirs[i] == "v": y -= 1
    elif dirs[i] == "<": x -= 1
    else:
        print("Invalid Character")
        break
print("Santa visited", len(houses), "houses in the first year")

x = 0
y = 0
houses = [(x, y)]
rx = 0
ry = 0
for i in range(0,len(dirs)):
    if i % 2 == 0:
        if dirs[i] == "^": y += 1
        elif dirs[i] == ">": x += 1
        elif dirs[i] == "v": y -= 1
        elif dirs[i] == "<": x -= 1
        else:
            print("Invalid Character")
            break
    else:
        if dirs[i] == "^": ry += 1
        elif dirs[i] == ">": rx += 1
        elif dirs[i] == "v": ry -= 1
        elif dirs[i] == "<": rx -= 1
        else:
            print("Invalid Character")
            break
    if (x, y) not in houses: houses.append((x, y))
    if (rx, ry) not in houses: houses.append((rx, ry))
print("Santa and Robo-Santa visited", len(houses), "houses in the second year")

