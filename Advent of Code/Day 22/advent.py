import random
bossRaw = [i.strip().split() for i in open("Advent of Code/Day 22/boss.txt").readlines()]
boss, player = {"H":int(bossRaw[0][1]), "D":int(bossRaw[1][1]), "E":[]}, {"H":50, "M":500, "A": 0, "E":[], "T":0}

def magic_missile(boss, player):
    player["M"] -= 53
    boss["H"] -= 4
    return boss, player

def drain(boss, player):
    player["M"] -= 73
    player["T"] += 73
    player["H"] += 2
    boss["H"] -= 2
    return boss, player

def shield(player):
    player["M"] -= 113
    player["T"] += 113
    player["E"].append({"T": 6, "N":"S"})
    return player

def poison(boss, player):
    player["M"] -= 173
    player["T"] += 173
    boss["E"].append({"T":6, "N":"P"})
    return boss, player

def recharge(player):
    player["M"] -= 229
    player["T"] += 229
    player["E"].append({"T":5, "N":"R"})
    return player

def effects(char):
    for i in char["E"]:
        i["T"] -= 1
        if i["N"] == "S": char["A"] = 0 if i["T"] == 0 else 7
        elif i["N"] == "P": char["H"] -= 3
        elif i["N"] == "R": char["M"] += 101
        if i["T"] == 0: char["E"].remove({"N":i["N"], "T":0})
    return char

def validCast(spell, boss, player):
    if spell == "M" and player["M"] < 53: return False
    elif spell == "D" and player["M"] < 73: return False
    elif spell == "S" and player["M"] < 113: return False
    elif spell == "S" and player["M"] < 173 and True in [i["N"] == "S" for i in player["E"]]: return False
    elif spell == "P" and player["M"] < 173 and True in [i["N"] == "P" for i in boss["E"]]: return False
    elif spell == "R" and player["M"] < 229 and True in [i["N"] == "R" for i in player["E"]]: return False
    return True

def fight(boss, player, rSeed):
    random.seed(rSeed)
    spells, pTurn = ["M", "D", "S", "P", "R"], False
    while player["H"] > 0 and boss["H"] > 0:
        if pTurn:
            player["H"] -= max(boss["D"] - player["A"], 1)
        else:
            if player["M"] >= 53: return False
            vCast = False
            while not vCast:
                cast = random.choice(spells)
                vCast = validCast(cast, boss, player)
            if cast == "M": boss, player = magic_missile(boss, player)
            elif cast == "D": boss, player = drain(boss, player)
            elif cast == "S": player = shield(player)
            elif cast == "P": boss, player = poison(boss, player)
            elif cast == "R": player = recharge(player)
            boss, player = effects(boss), effects(player)
        pTurn = not pTurn
    return pTurn, player["T"]

for i in range(1000000):
    if fight(boss, player, i):
        print(i)
        break
