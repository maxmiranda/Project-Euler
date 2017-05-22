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

def is_arith_seq(lst):
    lst.sort()
    for large in range(len(lst)):
        for medium in range(large):
            for small in range(medium):
                if lst[large] - lst[medium] == lst[medium] - lst[small]:
                    return [lst[small],lst[medium],lst[large]]
    return []


arith =[]
for n in range(1000,10000):
    if is_prime(n):
        count =1
        perm_primes = [n]
        for perm in list(generate(str(n))):
            permutation = int(''.join(perm))
            if is_prime(permutation) and permutation >= 1000 and permutation != n and not permutation in perm_primes:
                count +=1
                perm_primes.append(permutation)
                if count >=3 and is_arith_seq(perm_primes):
                    arith.append(is_arith_seq(perm_primes))

output = []
for x in arith:
    if x not in output:
        output.append(x)

print(output)
