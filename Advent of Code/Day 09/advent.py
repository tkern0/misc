from itertools import permutations
cities = open("Day 09\input.txt")
distance, names = [], []
shortest, longest = 0, 0
for line in cities: distance.append(line.split())
for i in range(len(distance)):
    if distance[i][0] not in names: names.append(distance[i][0])
    if distance[i][2] not in names: names.append(distance[i][2])
    shortest += int(distance[i][4])
perms = permutations(names, len(names))
for order in perms:
    length = 0
    for i in range(len(order) - 1):
        for j in range(len(distance)):
            if distance[j][0] == order[i]:
                if distance[j][2] == order[i + 1]: length += int(distance[j][4])
            if distance[j][2] == order[i]:
                if distance[j][0] == order[i + 1]: length += int(distance[j][4])
    if length < shortest: shortest = length
    if length > longest: longest = length
print("The shortest path is", shortest, "units long")
print("The longest path is", longest, "units long")
