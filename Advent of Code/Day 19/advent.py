# Turns the input into a bunch of useful vars
replacements, recipe, splitMolecule, replace = open("Advent of Code/Day 19/input.txt"), {}, [], []
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
for element in splitMolecule: replace.append(element in recipe) # Finds what molecules can be replaced
