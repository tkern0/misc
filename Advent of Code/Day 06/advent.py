instructions = open('input.txt')
lcount = 0
bcount = 0
lights = [[False for i in range(1000)] for i in range(1000)]
blights = [[0 for i in range(1000)] for i in range(1000)]
for line in instructions:
    sline = line.split()
    if len(sline) == 4:
        func = "not"
        coords = [sline[1].split(","), sline[3].split(",")]
    elif len(sline) == 5:
        func = sline[1]
        coords = [sline[2].split(","), sline[4].split(",")]
    else: print("Error, incorrect line length:", sline)
    if func == "on":
        for x in range(min(int(coords[0][0]),int(coords[1][0])),max(int(coords[0][0]),int(coords[1][0])) + 1):
            for y in range(min(int(coords[0][1]),int(coords[1][1])),max(int(coords[0][1]),int(coords[1][1])) + 1):
                lights[x][y] = True
                blights[x][y] += 1
    elif func == "off":
       for x in range(min(int(coords[0][0]),int(coords[1][0])),max(int(coords[0][0]),int(coords[1][0])) + 1):
            for y in range(min(int(coords[0][1]),int(coords[1][1])),max(int(coords[0][1]),int(coords[1][1])) + 1):
                lights[x][y] = False
                blights[x][y] -= 1
                if blights[x][y] < 0: blights[x][y] = 0
    elif func == "not":
        for x in range(min(int(coords[0][0]),int(coords[1][0])),max(int(coords[0][0]),int(coords[1][0])) + 1):
            for y in range(min(int(coords[0][1]),int(coords[1][1])),max(int(coords[0][1]),int(coords[1][1])) + 1):
                lights[x][y] = not lights[x][y]
                blights[x][y] += 2
    else: print("Error, incorrect function:", func)
for x in range(0,1000):
    for y in range(0,1000):
        if lights[x][y]: lcount += 1
        bcount += blights[x][y]
print(lcount, "lights are on")
print("The total brightness is", bcount)
