N = 1000000
primes = [1 for i in range(N)]
primes[0] = 0
primes[1] = 0

for num in range(2,N):
    for x in range(num*2, N, num):
        primes[x]= 0

def is_prime(i):
    return primes[i]

def is_trunc(i):
    copy = i
    lst_l =[]#list working towards the left
    counter = -1
    while i> 0:
        lst_l.append(is_prime(i))
        i = i//10
        counter+=1
    lst_r =[] #list working towards the right
    while counter>= 0:
        lst_r.append(is_prime(copy))
        copy = copy % 10**counter
        counter-=1
    return all(lst_r) and all(lst_l)



total = 0
for i in range(N):
    if i>10 and is_trunc(i):
        print(i)
        total += i
print(total)
