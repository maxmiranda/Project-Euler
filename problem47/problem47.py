class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

N = 1000000
primes = [1 for i in range(N)]
primes[0] = 0
primes[1] = 0

for num in range(2,N):
    for x in range(num*2, N, num):
        primes[x]= 0

def is_prime(i):
    return primes[i]

def prime_factors(n):
    count = 0
    for i in range(2,int(n**.5)):
        if n%i ==0 and is_prime(i) and is_prime(int(n/i)):
            count +=2
        if (n%i ==0 and is_prime(i)) or n%i ==0 and is_prime(int(n/i)):
            count +=1
    return count ==4

prime_factors = Memoize(prime_factors)

for n in range(647,1000000):
    if prime_factors(n) and prime_factors(n+1) and prime_factors(n+2) and prime_factors(n+3):
        print(n)
