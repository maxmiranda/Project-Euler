
def circulars(n):
    circulars = []
    n = str(n)
    for digit in range(len(n)):
        n = n[-1] + n[0:len(n)-1]
        circulars.append(int(n))
    return circulars

N = 1000000
primes = [1 for i in range(N)]
primes[0] = 0
primes[1] = 0

for num in range(2,N):
    for x in range(num*2, N, num):
        primes[x]= 0

def is_prime(i):
    return primes[i]

def circ_primes(N):
    count = 0
    for numb in range(N):
        Truthiness =[is_prime(circ) for circ in circulars(numb)]
        if all(Truthiness):
            count+=1

    print(count)

circ_primes(1000000)
