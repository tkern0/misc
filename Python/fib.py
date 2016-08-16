def fib(c, n = [1, 1]):
    for i in range(c-2): n.append(n[-1] + n[-2])
    return n[:c]
print(fib(5))
