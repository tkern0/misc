def format_input(sues, csue):
    info, correct = [], {}
    for line in sues:
        sline = line.split()
        tempDict = {}
        for i in range(2, len(sline), 2): # 'i' will be the positions off all the options
            if i + 2 < len(sline): sline[i + 1] = sline[i + 1][:-1]
            tempDict[sline[i][:-1]] = int(sline[i + 1]) # Example: {"children": 3}
        info.append(tempDict)
    for line in csue:
        sline = line.split()
        correct[sline[0][:-1]] = int(sline[1]) # Creates the same type of dict as in 'info', about the correct Sue
    return info, correct

def check_sue(sue, csue, retro = False):
    match = True
    for i in sue:
        if retro:
            if i in ("cats", "trees"): match = False if not sue[i] > csue[i] else match
            elif i in ("pomeranians", "goldfish"): match = False if not sue[i] < csue[i] else match
            else: match = False if not sue[i] == csue[i] else match
        else:
            match = False if not sue[i] == csue[i] else match
    return match

info, csue = format_input(open("Day 16\\input.txt"), open("Day 16\\correctsue.txt"))
for i in range(len(info)):
    if check_sue(info[i], csue): print("The correct Sue is number", i + 1)
    if check_sue(info[i], csue, True): print("The correct Sue, when accounting for an outdated retroencabulator, is number", i + 1)
