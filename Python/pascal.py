def pascal(n, l = [[1], [1, 1]]):
    for i in range(1, n):
        x = [1]
        for j in range(len(l)): x.append(1) if j == len(l) - 1 else x.append(l[i][j] + l[i][j + 1])
        l.append(x)
    return l

def pascal_print(l): print("\n".join((" ".join(str(j) for j in i) for i in l)))

pascal_print(pascal(5))
