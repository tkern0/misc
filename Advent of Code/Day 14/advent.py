def create_info(reindeer):
    info = {}
    for line in reindeer:
        sline = line.split()
        # *Vixen* can fly *19* km/s for *7* seconds, but then must rest for *124* seconds.
        #    0              3            6                                    13
        info[sline[0]] = [int(sline[3]), int(sline[6]), 1 - int(sline[13])] # 0 is counted as resting, so 1 second needs to be added
        # Name: Speed, Time, Rest
    return info

def olympics(time, info):
    currentPlace, points = {}, {}
    for i in info: currentPlace[i], points[i] = [0, info[i][1]], 0
    # 'currentPlace' Format: {Name: [Distance, Travel/Rest Time]}
    for _ in range(time):
        for key in currentPlace:
            if currentPlace[key][1] > 0:
            # TravelRest
                currentPlace[key][0] += info[key][0]
                # Distance + Speed
                currentPlace[key][1] -= 1
                # TravelRest
            elif currentPlace[key][1] == info[key][2]: currentPlace[key][1] = info[key][1]
            # TravelRest == Rest: TravelRest = Time
            else: currentPlace[key][1] -= 1
        highest, furthest = 0, []
        for i in currentPlace:
            if currentPlace[i][0] > highest:
                highest = currentPlace[i][0]
                furthest = [i]
            elif currentPlace[i][0] == highest:
                furthest.append(i)
        for i in furthest: points[i] += 1
    highest = 0
    for i in currentPlace: highest = currentPlace[i][0] if currentPlace[i][0] > highest else highest
    return highest, max(points.values())

# r1, r2 = olympics(1000, create_info(open("Day 14\\test.txt")))
r1, r2 = olympics(2503, create_info(open("Day 14\\input.txt")))
print("The winner in Race 1 traveled", r1, "km")
print("The winner in Race 2 scored", r2, "points")
