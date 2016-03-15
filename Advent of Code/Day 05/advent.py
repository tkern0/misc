strings = open("input.txt")
ncount = 0
nncount = 0
for line in strings:
    vcount = 0
    dletter = False
    pletter = False
    sletter = False
    autofail = False
    if "ab" not in line and "cd" not in line and "pq" not in line and "xy" not in line:
        for i in range(0,len(line)):
            if line[i:i+1] in "aeiou": vcount += 1
            if line[i-1:i] == line[i:i+1]: dletter = True
        if dletter and vcount > 2: ncount += 1
        #part 2
    for i in range(0,len(line)):
        if line[i-2:i-1] == line[i:i+1]:
            if line[i-1:i] == line[i:i+1]: autofail = True #opmopgyabjjjoygt sknufchjdvccccta cyypypveppxxxfuq fail this one but pass others
            sletter = True
        if line[i:i+2] in line[i+2:]: pletter = True
    if sletter and pletter and not autofail: nncount += 1
print("There are", ncount, "nice strings and", 1000 - ncount, "naughty strings using the first set of rules")
print("There are", nncount, "nice strings and", 1000 - nncount, "naughty strings using the second set of rules")
