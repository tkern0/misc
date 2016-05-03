import itertools

def format_input(inputfile):
    # *Sprinkles:* capacity *2,* durability *0,* flavor *-2,* texture *0,* calories *3*
    #     0                   2               4            6            8           10
    info = {}
    for line in inputfile:
        sline = line.split()
        info[sline[0][:-1]] = [int(sline[2][:-1]), int(sline[4][:-1]), int(sline[6][:-1]), int(sline[8][:-1]), int(sline[10])]
        # {Name: [Capacity, Durability, Flavor, Texture, Calories]}
    return info

def get_stat(ingr, stat):
    # Stat values:
    # Capacity: 0
    # Durability: 1
    # Flavor : 2
    # Texture: 3
    # Calories: 4
    return info[ingr][stat] # This wans't working in the other function so I made it it's own function

def get_score(ingr, amount):
    fullIngrStats = []
    for i in range(4): # Iterate through all ingredient stats exept calories
        ingrStat = []
        for j in range(len(ingr)): ingrStat.append(get_stat(ingr[j], i) * amount[j])
        # Iterate through ingredients, adding 'stat * amount' to 'ingrStat'
        if sum(ingrStat) < 1: return 0
        fullIngrStats.append(sum(ingrStat))
    final = fullIngrStats[0]
    for i in fullIngrStats[1:]: final *= i
    return final

def get_calories(ingr, amount):
    ingrStat = []
    for j in range(len(ingr)): ingrStat.append(get_stat(ingr[j], 4) * amount[j])
    # Iterate through ingredients, adding 'calories * amount' to 'ingrStat'
    return 0 if sum(ingrStat) < 1 else sum(ingrStat)

info = format_input(open("Day 15\\input.txt"))
keys = [key for key in info] # Because info.keys() doesn't work properly
highest = 0
calorieHighest = 0
for i in itertools.combinations_with_replacement(keys, 100): # Iterates through all possible combinations of the ingredients (4^100 or 1.6 x 10^60)
    amount = []
    for j in range(len(keys)): amount.append(i.count(keys[j])) # Count how many of each ingredient is used
    score = get_score(keys, amount)
    calorieScore = get_calories(keys, amount)
    if score > highest: highest = score
    if  calorieScore == 500 and score > calorieHighest: calorieHighest = score
print("Highest score:", highest)
print("Highest score with 500 calories:", calorieHighest)
