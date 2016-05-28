findNum, i = 33100000/10, 0

def sum_factors(n):
    f, i, s = [], 2, 1
    while i ** 2 <= n: # Prime factors
        if n % i == 0:
            n //= i
            f.append(i)
        else: i += 1
    if n > 1: f.append(n)
    while len(f) > 0: # Factor sum calculation using prime factors
        s *= sum([f[0] ** i for i in range(f.count(f[0]) + 1)])
        f = f[f.count(f[0]):]
    return s

while sum_factors(i) < findNum: i += 1
print(i)
