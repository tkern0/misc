strings = open('input.txt')
count = 0
ocount = 0
for line in strings:
    count += len(line) - len(eval(line)) - 1
    ocount += line.count("\\") + line.count('"') + 2
print("The strings use", count + 1, "characters to define themselves")
print("The strings use an additional ", ocount, "characters to define themselves within new strings")

