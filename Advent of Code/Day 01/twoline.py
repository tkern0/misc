a = [1 if open('Advent of Code/Day 01/input.txt').read()[i] == "(" else -1 for i in range(len(open('Advent of Code/Day 01/input.txt').read()))]
print(sum(a), [i for i in range(len(a)) if sum(a[:i]) == -1][0])
