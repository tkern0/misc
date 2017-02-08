def pascal(n, l = [[1], [1, 1]]):
    for i in range(1, n):
        x = [1]
        for j in range(len(l)): x.append(1) if j == len(l) - 1 else x.append(l[i][j] + l[i][j + 1])
        l.append(x)
    return l

def print_centered(n):
  l = []
  for i in n: l.append(str(i))
  m = len(l[-1])
  for i in l:
    print(" " * int((m - len(i))/2) + i + " " * (int((m - len(i))/2) + 1))

print_centered(pascal(5))
