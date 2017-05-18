
N = 10000
primes = [1 for i in range(N)]
primes[0] = 0
primes[1] = 0

for num in range(2,N):
    for x in range(num*2, N, num):
        primes[x]= 0

def is_prime(i):
    return primes[i]

actual_primes = [i for i in range(10000) if is_prime(i)]
squares = [n**2 for n in range(1,1000)]
goldbach =[]

for prime in actual_primes:
    for square in squares:
        goldbach.append(prime + 2*square)

print(goldbach)
goldbach = set(goldbach)

def goldbach_false():
    for odd in range(3,10000000,2):
        if odd not in goldbach and not is_prime(odd):
            return odd

print(goldbach_false())
