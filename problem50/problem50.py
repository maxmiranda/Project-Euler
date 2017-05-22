import operator

N = 1000000
primes = [1 for i in range(N)]
primes[0] = 0
primes[1] = 0

for num in range(2,N):
    for x in range(num*2, N, num):
        primes[x]= 0

def is_prime(i):
    return primes[i]

real_primes = [n for n in range(1000000) if is_prime(n)]

set_primes = set(real_primes)
def generate_sum_primes():
    sum_primes = []
    for i in range(2,len(real_primes)):
        for consec in range(500,600):
            if not i + consec > len(real_primes):
                sum_prime = sum(real_primes[i:i+consec])
                if sum_prime in set_primes:
                    sum_primes.append([sum_prime, consec])
    return max(sum_primes, key = operator.itemgetter(1))

print(generate_sum_primes())
