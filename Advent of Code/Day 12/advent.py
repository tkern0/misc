import json
data = json.loads(open("Day 12\input.txt").read())
def num_sum(fjson):
    if type(fjson) == int: return fjson
    elif type(fjson) == list: return sum(map(num_sum, fjson))
    elif type(fjson) == dict: return sum(map(num_sum, fjson.values()))
    return 0
def redless_sum(fjson):
    if type(fjson) == int: return fjson
    elif type(fjson) == list: return sum(map(redless_sum, fjson))
    elif type(fjson) == dict:
        if "red" in fjson.values(): return 0
        return sum(map(redless_sum, fjson.values()))
    return 0
print("The sum of all numbers in the json is:", num_sum(data))
print("The sum of all numbers, not including \"red\", in the json is:", redless_sum(data))
