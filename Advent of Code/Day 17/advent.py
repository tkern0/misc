import itertools
containers, count = [], [0, 150, 0] # [Total combinations, Minimum containers, Minimum container combinations]
for i in open("Day 17\\input.txt"): containers.append(int(i))
for i in range(len(containers)):
    for j in itertools.combinations(containers, i):
        if sum(j) == 150: count[0] += 1
        if sum(j) == 150 and i < count[1]: count = [count[0], i, 0]
        if sum(j) == 150 and i == count[1]: count[2] += 1
print("There are", count[0], "ways to fit 150 liters")
print("There are", count[2], "ways to fit 150 liters into just", count[1] + 1, "containers")
