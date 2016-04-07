# Take input and formats it into a dict
def format_input(instr):
    wires = {}
    for line in instr:
        temp = line.split()
        # Possible values:
        # kg OR kf -> kh
        # NOT dq -> dr
        # 44430 -> b
        if "AND" in temp or "OR" in temp or "LSHIFT" in temp or "RSHIFT" in temp:
            wires[temp[4].strip()] = [temp[1], temp[0], temp[2]]
            # wires["kh"] = ["OR", "kg", "kf"]
        elif "NOT" in temp:
            wires[temp[3].strip()] = ["NOT", temp[1]]
            # wires["dr"] = ["NOT", "dq"]
        else:
            wires[temp[2].strip()] = ["EQUALS", temp[0]]
            # wires["b"] = ["EQUALS", "44430"]
    return wires
# Finds the value of a certain variable
def find_value(var):
    if var in solved: return solved[var]
    if var.isdigit(): return var # This shouldn't need to be here but 'find_value()'' was sometimes being called with an int
    # Recursivly solves 'var' and puts it's value into sorted
    # This is done so that multiple refrences to the same variable do not need to recalculate it each time
    if wires[var][0] == "AND":
        solved[var] = int(find_value(wires[var][1])) & int(find_value(wires[var][2]))
    elif wires[var][0] == "OR":
        solved[var] = int(find_value(wires[var][1])) | int(find_value(wires[var][2]))
    elif wires[var][0] == "LSHIFT":
        solved[var] = int(find_value(wires[var][1])) << int(find_value(wires[var][2]))
    elif wires[var][0] == "RSHIFT":
        solved[var] = int(find_value(wires[var][1])) >> int(find_value(wires[var][2]))
    elif wires[var][0] == "NOT":
        solved[var] = ~int(find_value(wires[var][1]))
    else: # "EQUALS"
        if wires[var][1].isdigit(): solved[var] = int(wires[var][1])
        else: solved[var] = int(find_value(wires[var][1]))
    return solved[var]

wires = format_input(open("Day 07\input.txt"))
solved = {}
a1 = find_value("a")
wires["b"] = ["EQUALS", str(a1)]
solved = {}
a2 = find_value("a")
print(a1, a2)
