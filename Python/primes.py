def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return n > 1

# More inefficent, but 1-liner
def prime(n): return True not in [n % i == 0 for i in range(2, int(n**0.5) + 1)] and n > 1

for i in range(100):
    if is_prime(i): print(i)
