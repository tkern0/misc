dirs = open('Day 01\input.txt').read()
floor = 0
basement = False
for i in range(len(dirs)):
    if dirs[i] == '(':
        floor += 1
    elif dirs[i] == ')':
        floor -= 1
    else:
        print("Incorrect Character")
        break
    if floor == -1 and not basement:
        print("Santa first enters the basement on position", i + 1)
        basement = True
print("Santa is on floor", floor)
