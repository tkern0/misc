# https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4cu5b
from random import shuffle

reps = [] # My code
for line in open("Advent of Code/Day 19/input.txt"):
    splitLine = line.strip().split(" ")
    if len(splitLine) == 3: reps.append((splitLine[0], splitLine[2]))
    elif not line == "": mol = line.strip()

# /u/What-A-Baller's code
# reps = [('Al', 'ThF), ...]
# mol = "CRnCaCa..."

target = mol
part2 = 0

while target != 'e':
    tmp = target
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    if tmp == target:
        target = mol
        part2 = 0
        shuffle(reps)

print part2
