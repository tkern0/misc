# Turns the input into a bunch of useful vars
replacements, recipe, reverseRecipe, splitMolecule, replaced = open("Advent of Code/Day 19/input.txt"), {}, {}, [], []
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

# Works, but not to reduce to "e"
rCount = 0
def replaceMolecule(molecule):
    for i in range(len(molecule)):
        for j in reverseRecipe:
            if molecule[i:].startswith(j):
                global rCount
                rCount += 1
                molecule, _ = replaceMolecule(reverseRecipe[j] + molecule[i + len(j):])
    return molecule, rCount

print(replaceMolecule(molecule))
