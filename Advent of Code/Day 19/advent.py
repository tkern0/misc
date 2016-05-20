import random
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

# Brute force
# Currently gets stuck in infinite chain of "Ca"s
# Theory:
# It executes itself once but waits for a correct answer befor executing the next once
# Fix by going one step at a time instead of recursion
# Pseudocode
# while molecule not in replaced:
# replaced -> oldreplaced
# replace everything in old replaced
# store in replace

rCount = 0
def find_replacements(replaceString):
    global rCount
    rCount += 1
    replaced = []
    for i in range(len(replaceString)):
        for j in recipe:
            if replaceString[i:].startswith(j):
                if not i == len(replaceString) - 1 and replaceString[i + 1].isupper():
                    for k in recipe[j]:
                        replaced.append(replaceString[:i] + k + replaceString[i + 1:])
                else:
                    for k in recipe[j]:
                        replaced.append(replaceString[:i] + k + replaceString[i + 2:])
    print(replaced)
    if molecule in replaced:
        return rCount
    else:
        for i in replaced:
            return find_replacements(i)

print(find_replacements("e"))
