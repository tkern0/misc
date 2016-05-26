findNum, i = 33100000/10, 0
def find_presents(num): return sum([i + 1 if num % (i + 1) == 0 else 0 for i in range(num )])
while find_presents(i) < findNum: i += 1
print(i)
