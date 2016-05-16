# Turns the input into a bunch of useful vars
replacements, recipe, reverseRecipe, splitMolecule, replace = open("Advent of Code/Day 19/input.txt"), {}, {}, [], []
for line in replacements: # Determines recipes and the molecule
    splitLine = line.strip().split(" ")
    if len(splitLine) == 3:
        reverseRecipe[splitLine[2]] = splitLine[0]
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
            join = ""
            for element in newMolecule: join += str(element)
            if not join in replaced: replaced.append(join)
print("Part 1:", len(replaced))
# recursive function:
# does 1 reverse replacement everywhere possible
# calls itself on new molecule
# count steps somehow
#
# get min + max len of outputs
# start at [0:], check if following chars, from min --> max len, are possible recipe output
# if so, replace with input, go on to next one
# then start at [1:]
# repeat
for i in range(len(molecule)):
