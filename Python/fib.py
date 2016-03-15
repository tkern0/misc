def fib(c, x = 1, y = 1):
    n = [x, y]
    for i in range(c-2):
        n.append(n[-1] + n[-2])
    return n[:c]
print(fib(5))
