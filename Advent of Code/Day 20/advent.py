findNum, i = 33100000/10, 90000
def find_presents(n): return sum([i + 1 if n % (i + 1) == 0 else 0 for i in range(n)])
while find_presents(i) < findNum:
    i += 1
    print(i)
