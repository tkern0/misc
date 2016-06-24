from itertools import combinations
bossRaw, armor, rings, weapons = [i.split() for i in open("Advent of Code/Day 21/boss.txt").readlines()], [i.split() for i in open("Advent of Code/Day 21/armor.txt").readlines()], [i.split() for i in open("Advent of Code/Day 21/rings.txt").readlines()], [i.split() for i in open("Advent of Code/Day 21/weapons.txt").readlines()]
boss, shop = {"H":int(bossRaw[0][1]), "D":int(bossRaw[1][1]), "A":int(bossRaw[2][1])}, {"A":[{"C":int(i[1]), "D":int(i[2]), "A":int(i[3])} for i in armor], "R":[{"C":int(i[1]), "D":int(i[2]), "A":int(i[3])} for i in rings], "W":[{"C":int(i[1]), "D":int(i[2]), "A":int(i[3])} for i in weapons]}
shop["A"].append({"A":0, "D": 0, "C":0})
shop["R"].extend([{"A":0, "D": 0, "C":0}, {"A":0, "D": 0, "C":0}])

def fight(boss, player):
    pTurn = False
    while boss["H"] > 0 and player["H"] > 0:
        if pTurn: player["H"] -= boss["D"] - player["A"]
        else: boss["H"] -= player["D"] - boss["A"]
        pTurn = not pTurn
    return pTurn

minGold, maxGold = 400, 0
for a in shop["A"]:
    for r in combinations(shop["R"], 2):
        for w in shop["W"]:
            gold = a["C"] + r[0]["C"] + r[1]["C"] + w["C"]
            if fight(dict(boss), {"H":100, "D": r[0]["D"] + r[1]["D"] + w["D"], "A":r[0]["A"] + r[1]["A"] + a["A"]}):
                if gold < minGold: minGold = gold
            elif gold > maxGold: maxGold = gold
print(minGold, maxGold)
