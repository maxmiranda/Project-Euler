def generate(s):
    if len(s) <= 1:
        yield [s]
    else:
        for perm in generate(s[1:]):
            for i in range(len(s)):
                yield perm[:i] + [s[0:1]] + perm[i:]

N = 10000
primes = [1 for i in range(N)]
primes[0] = 0
primes[1] = 0

for num in range(2,N):
    for x in range(num*2, N, num):
        primes[x]= 0

def is_prime(i):
    return primes[i]

def constant_diff(lst):
    lst.sort(reverse = True)
    for i in range(lst-1):
        if lst[i] - lst[i+1]

for n in range(1000,10000):
    if is_prime(n):
        count =1
        perm_primes = [n]
        for perm in list(generate(str(n))):
            permutation = int(''.join(perm))
            if is_prime(permutation) and permutation >1000 and permutation != n:
                count +=1
                perm_primes.append(permutation)
                if count ==3 and constant_diff(perm_primes):
                    print(perm_primes)
