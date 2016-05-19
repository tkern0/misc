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

# Brute force:
# 1. Start with string ("e")
# 2. Find every possible replacement
# 3. Keep these stored
# 4. If one replacement == molecule break loop
# 5. Goto 1 with each replacement as string

rCount = 0
def find_replacements(replaceString):
    global rCount
    rCount += 1
    replaced = []
    for i in range(len(replaceString)):
        for j in reverseRecipe
            if replaceString[i:].startswith(j):
                if molecule[i + 1].isupper(): replaced.append(molecule[:i] + reverseRecipe[j] + molecule[i+1:])
                else: replcaed.append(molecule[:i] + reverseRecipe[j] + molecule[i+2])
    if molecule in replaced: return rCount


# Reverse engineering (Doesn't Work)
# rCount = 0
# def replaceMolecule(molecule, shuffled):
#     for i in range(len(molecule)):
#         for j in shuffled:
#             if molecule[i:].startswith(j):
#                 global rCount
#                 rCount += 1
#                 if molecule[i + 1].isupper(): newMolecule = molecule[:i] + reverseRecipe[j] + molecule[i+1:]
#                 else: newMolecule = molecule[:i] + reverseRecipe[j] + molecule[i+2:]
#                 molecule = replaceMolecule(newMolecule, shuffled)
#     return molecule
#
# # out = ""
# # keys = list(reverseRecipe.keys())
# # while not out == "e":
# #     rCount = 0
# #     random.shuffle(keys)
# #     out = replaceMolecule(molecule, keys)
# #     print(out, rCount)
#
# print(replaceMolecule(molecule, reverseRecipe), rCount)
