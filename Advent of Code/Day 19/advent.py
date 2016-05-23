# Turns the input into a bunch of useful vars
replacements, recipe, splitMolecule, replaced = open("Advent of Code/Day 19/input.txt"), {}, [], []
for line in replacements: # Determines recipes and the molecule
    splitLine = line.strip().split(" ")
    if len(splitLine) == 3:
        if splitLine[0] in recipe: recipe[splitLine[0]].append(splitLine[2])
        else: recipe[splitLine[0]] = [splitLine[2]]
    elif not line == "": molecule = line.strip()
for char in range(len(molecule)): # Splits molecule into each element
    if molecule[char].isupper():
        if molecule[char + 1].isupper(): splitMolecule.append(molecule[char])
        else: splitMolecule.append(molecule[char:char + 2])
for i in range(len(splitMolecule)): # Works out part 1
    if splitMolecule[i] in recipe:
        for replace in recipe[splitMolecule[i]]:
            newMolecule = list(splitMolecule)
            newMolecule[i] = replace
            join = ""
            for element in newMolecule: join += str(element)
            if not join in replaced: replaced.append(join)
print("Part 1:", len(replaced))

# May take weeks to finish
newMolecule = ["e"]
rCount = 0
while True:
    currentMolecule = list(newMolecule)
    newMolecule = []
    if molecule in currentMolecule: break
    rCount += 1
    print(rCount)
    for i in currentMolecule:
        for j in range(len(i)):
            for k in recipe:
                if i[j:].startswith(k):
                    if not j == len(i) - 1 and i[j + 1].isupper():
                        for l in recipe[k]: newMolecule.append(i[:j] + l + i[j + 1:])
                    else:
                        for l in recipe[k]: newMolecule.append(i[:j] + l + i[j + 2:])
print(rCount)
