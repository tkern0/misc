from itertools import permutations
happiest = 0
def format_input(txt):
    happy = {}
    people = []
    for line in txt:
        words = line[:-2].split() # Removes fullstop and newline characters
        words[3] = int(words[3]) if words[2] == "gain" else -int(words[3])
        happy[(words[0], words[10])] = words[3]
        # *Alice* would *lose* *81* happiness units by sitting next to *Carol*
        #   0              2   3                                         10
        if not words[0] in people: people.append(words[0])
    return happy, people

def find_happy(aPerson, bPerson):
    if (aPerson, bPerson) in happy: return happy[(aPerson, bPerson)]
    else: return happy[(bPerson, aPerson)]

happy, people = format_input(open("Day 13\input.txt"))
for perm in permutations(people, len(people)):
    currentHappy = find_happy(perm[0], perm[-1]) #TODO: Make it work
    for i in range(len(perm) - 1):
        currentHappy += find_happy(perm[i], perm[i + 1])
    if currentHappy > happiest: happiest = currentHappy
print("The happiest arangement creates", happiest, "happiness")
