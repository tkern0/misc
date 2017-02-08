import timeit

def is_prime(n):
    for i in range(2, int(n**0.5+1)):
        if n % i == 0: return False
    return n > 1

# Not sure at what point this is faster than is_prime, but for really high numbers it should definitly be
def fast_prime(n):
    i, rt = 2, int(n**0.5 + 1)
    while i < rt:
        if n % i == 0: return False
        i += 1
    return n > 1

# Just to prove I can do it
def short_prime(n): return 0 not in [n % i for i in range(2, int(n**0.5+1))] and n > 1

# for i in range(100):
    # if is_prime(i): print(i)
    # if fast_prime(i): print(i)
    # if short_prime(i): print(i)

# print(timeit.timeit("is_prime(1000)", setup="from __main__ import is_prime"))
# print(timeit.timeit("fast_prime(1000)", setup="from __main__ import fast_prime"))
# print(timeit.timeit("short_prime(1000)", setup="from __main__ import short_prime"))