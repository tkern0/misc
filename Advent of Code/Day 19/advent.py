def join_molecule(split):
    join = ""
    for element in split: join += str(element)
    return join

# Turns the input into a bunch of useful vars
replacements, recipe, splitMolecule, replaced = open("Advent of Code/Day 19/input.txt"), {}, [], []
for line in replacements: # Determines recipes and the molecule
    splitLine = line.strip().split(" ")
    if len(splitLine) == 3:
        if splitLine[0] in recipe: recipe[splitLine[0]].append(splitLine[2])
        else: recipe[splitLine[0]] = [splitLine[2]]
    elif not line == "": molecule = line.strip()
for char in range(len(molecule)): # Splits molecule into each element
    if molecule[char:char + 1].isupper():
        if molecule[char + 1:char + 2].isupper(): splitMolecule.append(molecule[char:char + 1])
        else: splitMolecule.append(molecule[char:char + 2])
for i in range(len(splitMolecule)): # Works out part 1
    if splitMolecule[i] in recipe:
        for replace in recipe[splitMolecule[i]]:
            newMolecule = list(splitMolecule)
            newMolecule[i] = replace
            if not join_molecule(newMolecule) in replaced: replaced.append(join_molecule(newMolecule))
print("Part 1:", len(replaced))
