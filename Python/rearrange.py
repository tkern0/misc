import enchant, itertools
a = enchant.Dict("en_US")
b = enchant.Dict("en_GB")
# for i in itertools.permutations("ANGEL"):
#     if a.check("".join(i)) or b.check("".join(i)):
#         print("".join(i))

f = set()
for i in itertools.permutations((["A", "V"], ["N", "Z"], ["G", "D"], ["L", "T"], ["E", "M", "W"])):
    for j in itertools.product(range(3), repeat=5):
        s = ""
        for k in range(5):
            s += i[k][j[k]%len(i[k])]
        if (a.check(s) or b.check(s)) and s not in f:
            print(s)
            f.add(s)
# ANGLE
# ANGEL
# ANTED
# AGENT
# ALDEN
# NELDA
# ZELDA
# DANTE
# GALEN
# GLAZE
# GLEAN
# LANGE
# LAZED
# LADEN
# TWANG
# ELAND