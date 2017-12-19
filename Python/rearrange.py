import enchant, itertools
a = enchant.Dict("en_US")
b = enchant.Dict("en_GB")
c = enchant.Dict("en_AU")
d = enchant.Dict("de_DE")
# for i in itertools.permutations("ANGEL"):
#     if a.check("".join(i)) or b.check("".join(i)):
#         print("".join(i))

f = set()
for i in itertools.permutations(([["A", "V"], [""]], [["N", "Z"], [""]], [["G", "D"], [""]], [["L", "T"], ["E", "M", "W"]], [["E", "M", "W"], ["."]])):
    for j in itertools.product(range(2), repeat=5):
        for k in itertools.product(range(3), repeat=5):
            s = ""
            for l in range(5):
                s += i[l][j[l]][k[l]%len(i[l][j[l]])]
            if "." in s:
                continue
            if (a.check(s) or b.check(s) or c.check(s)) and s not in f:
                print(s)
                f.add(s)

with open("rearrange_output.txt", "w") as file:
    for s in sorted(list(f)):
        if d.check(s):
            file.write("**" + s +"**\n")
        else:
            file.write(s + "\n")