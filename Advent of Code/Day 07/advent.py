instructions = open("Day 07\input.txt")
wires, solved, values = [], [], []
# HOW DOES THIS EVEN WORK????
for line in instructions:
    temp = line.split(" ")
    if "AND" in temp or "OR" in temp or "LSHIFT" in temp or "RSHIFT" in temp:
        wires.append([temp[4].strip(), temp[1], temp[0], temp[2]])
    elif "NOT" in temp:
        wires.append([temp[3].strip(), "NOT", temp[1]])
    else:
        wires.append([temp[2].strip(), "EQUALS", temp[0]])
for i in range(len(wires)):
    if wires[i][1] == "EQUALS" and wires[i][2].isdigit():
        values.append([wires[i][0], int(wires[i][2])])
        solved.append(wires[i][0])
while "a" not in solved:
    for i in range(len(wires)):
        if wires[i][0] not in solved and wires[i][1] == "EQUALS" and wires[i][2] in solved:
            for j in range(len(values)):
                if values[j][0] == wires[i][2]: values.append([wires[i][0], values[j][1]])
            solved.append(wires[i][0])
        if wires[i][0] not in solved and wires[i][1] == "NOT":
            if wires[i][2] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]: values.append([wires[i][0], ~ values[j][1]])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit():
                values.append([wires[i][0], ~ int(wires[i][2])])
                solved.append(wires[i][0])
        if wires[i][0] not in solved and wires[i][1] == "AND":
            if wires[i][2] in solved and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]:
                        for k in range(len(values)):
                            if values[k][0] == wires[i][3]:
                                values.append([wires[i][0], values[j][1] & values[k][1]])
                solved.append(wires[i][0])
            elif wires[i][2] in solved and wires[i][3].isdigit():
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]: values.append([wires[i][0], values[j][1] & int(wires[i][3])])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][3]: values.append([wires[i][0], int(wires[i][2]) & values[j][1]])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3].isdigit():
                values.append([wires[i][0], int(wires[i][2]) & int(wires[i][3])])
                solved.append(wires[i][0])
        if wires[i][0] not in solved and wires[i][1] == "OR":
            if wires[i][2] in solved and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]:
                        for k in range(len(values)):
                            if values[k][0] == wires[i][3]:
                                values.append([wires[i][0], values[j][1] | values[k][1]])
                solved.append(wires[i][0])
            elif wires[i][2] in solved and wires[i][3].isdigit():
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]: values.append([wires[i][0], values[j][1] | int(wires[i][3])])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][3]: values.append([wires[i][0], int(wires[i][2]) | values[j][1]])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3].isdigit():
                values.append([wires[i][0], int(wires[i][2]) | int(wires[i][3])])
                solved.append(wires[i][0])
        if wires[i][0] not in solved and wires[i][1] == "LSHIFT":
            if wires[i][2] in solved and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]:
                        for k in range(len(values)):
                            if values[k][0] == wires[i][3]:
                                values.append([wires[i][0], values[j][1] << values[k][1]])
                solved.append(wires[i][0])
            elif wires[i][2] in solved and wires[i][3].isdigit():
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]: values.append([wires[i][0], values[j][1] << int(wires[i][3])])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][3]: values.append([wires[i][0], int(wires[i][2]) << values[j][1]])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3].isdigit():
                values.append([wires[i][0], int(wires[i][2]) << int(wires[i][3])])
                solved.append(wires[i][0])
        if wires[i][0] not in solved and wires[i][1] == "RSHIFT":
            if wires[i][2] in solved and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]:
                        for k in range(len(values)):
                            if values[k][0] == wires[i][3]:
                                values.append([wires[i][0], values[j][1] >> values[k][1]])
                solved.append(wires[i][0])
            elif wires[i][2] in solved and wires[i][3].isdigit():
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]: values.append([wires[i][0], values[j][1] >> int(wires[i][3])])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][3]: values.append([wires[i][0], int(wires[i][2]) >> values[j][1]])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3].isdigit():
                values.append([wires[i][0], int(wires[i][2]) >> int(wires[i][3])])
                solved.append(wires[i][0])
for i in range(len(values)):
    if values[i][0] == "a":
        print("The original value of 'a' is", values[i][1])
        for j in range(len(wires)):
            if wires[j][0] == "b": wires[j][2] = str(values[i][1])
solved = []
values = []
for i in range(len(wires)):
    if wires[i][1] == "EQUALS" and wires[i][2].isdigit():
        values.append([wires[i][0], int(wires[i][2])])
        solved.append(wires[i][0])
while "a" not in solved:
    for i in range(len(wires)):
        if wires[i][0] not in solved and wires[i][1] == "EQUALS" and wires[i][2] in solved:
            for j in range(len(values)):
                if values[j][0] == wires[i][2]: values.append([wires[i][0], values[j][1]])
            solved.append(wires[i][0])
        if wires[i][0] not in solved and wires[i][1] == "NOT":
            if wires[i][2] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]: values.append([wires[i][0], ~ values[j][1]])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit():
                values.append([wires[i][0], ~ int(wires[i][2])])
                solved.append(wires[i][0])
        if wires[i][0] not in solved and wires[i][1] == "AND":
            if wires[i][2] in solved and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]:
                        for k in range(len(values)):
                            if values[k][0] == wires[i][3]:
                                values.append([wires[i][0], values[j][1] & values[k][1]])
                solved.append(wires[i][0])
            elif wires[i][2] in solved and wires[i][3].isdigit():
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]: values.append([wires[i][0], values[j][1] & int(wires[i][3])])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][3]: values.append([wires[i][0], int(wires[i][2]) & values[j][1]])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3].isdigit():
                values.append([wires[i][0], int(wires[i][2]) & int(wires[i][3])])
                solved.append(wires[i][0])
        if wires[i][0] not in solved and wires[i][1] == "OR":
            if wires[i][2] in solved and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]:
                        for k in range(len(values)):
                            if values[k][0] == wires[i][3]:
                                values.append([wires[i][0], values[j][1] | values[k][1]])
                solved.append(wires[i][0])
            elif wires[i][2] in solved and wires[i][3].isdigit():
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]: values.append([wires[i][0], values[j][1] | int(wires[i][3])])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][3]: values.append([wires[i][0], int(wires[i][2]) | values[j][1]])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3].isdigit():
                values.append([wires[i][0], int(wires[i][2]) | int(wires[i][3])])
                solved.append(wires[i][0])
        if wires[i][0] not in solved and wires[i][1] == "LSHIFT":
            if wires[i][2] in solved and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]:
                        for k in range(len(values)):
                            if values[k][0] == wires[i][3]:
                                values.append([wires[i][0], values[j][1] << values[k][1]])
                solved.append(wires[i][0])
            elif wires[i][2] in solved and wires[i][3].isdigit():
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]: values.append([wires[i][0], values[j][1] << int(wires[i][3])])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][3]: values.append([wires[i][0], int(wires[i][2]) << values[j][1]])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3].isdigit():
                values.append([wires[i][0], int(wires[i][2]) << int(wires[i][3])])
                solved.append(wires[i][0])
        if wires[i][0] not in solved and wires[i][1] == "RSHIFT":
            if wires[i][2] in solved and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]:
                        for k in range(len(values)):
                            if values[k][0] == wires[i][3]:
                                values.append([wires[i][0], values[j][1] >> values[k][1]])
                solved.append(wires[i][0])
            elif wires[i][2] in solved and wires[i][3].isdigit():
                for j in range(len(values)):
                    if values[j][0] == wires[i][2]: values.append([wires[i][0], values[j][1] >> int(wires[i][3])])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3] in solved:
                for j in range(len(values)):
                    if values[j][0] == wires[i][3]: values.append([wires[i][0], int(wires[i][2]) >> values[j][1]])
                solved.append(wires[i][0])
            elif wires[i][2].isdigit() and wires[i][3].isdigit():
                values.append([wires[i][0], int(wires[i][2]) >> int(wires[i][3])])
                solved.append(wires[i][0])
for i in range(len(values)):
    if values[i][0] == "a": print("The second value of 'a' is", values[i][1])
