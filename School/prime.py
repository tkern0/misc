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

# 43 Characters
p=lambda x:1<x*all(x%i for i in range(2,x))

# for i in range(100):
    # if is_prime(i): print(i)
    # if fast_prime(i): print(i)
    # if p(i): print(i)

# print(timeit.timeit("is_prime(1000)", setup="from __main__ import is_prime"))
# print(timeit.timeit("fast_prime(1000)", setup="from __main__ import fast_prime"))
# print(timeit.timeit("p(1000)", setup="from __main__ import p"))