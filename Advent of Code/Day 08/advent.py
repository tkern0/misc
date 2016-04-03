strings = open('Day 08\input.txt')
count, ocount = 0, 0
for line in strings:
    # Thanks to the subreddit for teaching me about eval()
    count += len(line) - len(eval(line)) - 1
    ocount += line.count("\\") + line.count('"') + 2
print("The strings use", count + 1, "characters to define themselves")
print("The strings use an additional ", ocount, "characters to define themselves within new strings")
