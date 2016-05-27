# Example num: 24
# All Factors:
# 1 2 3 4 6 12 24
# Sum = 60
# Prime factors:
# 2 * 2 * 2 * 3
# 2^3 * 3^1
# Sum = (2^0 + 2^1 + 2^2 + 2^3) * (3^0 + 3^1) = 60

def prime_factor(n, p):
    f = []
    for i in p:
        if n % i == 0:
            if n / i == 1: return n
            else: f.append(prime_factor(n/i, p))
    else: return f

print(prime_factor(12, [2, 3, 5, 7]))
