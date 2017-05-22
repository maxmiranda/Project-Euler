N = 1000000
primes = [1 for i in range(N)]
primes[0] = 0
primes[1] = 0

for num in range(2,N):
    for x in range(num*2, N, num):
        primes[x]= 0

def is_prime(i):
    return primes[i]

real_primes  = [n for n in range(N) if is_prime(n)]
set_primes = set(real_primes)
digit_primes = [[digit for digit in str(prime)] for prime in real_primes]
#real primes is now a two d array it is a list of the digits of all of the prime numbers
# if at least two digits are the same in a prime, replace those digits with another digit and see if it's in the set of primes
def repeating_digit(n):
    # returns the repeating digit if one exists in a number, if not returns []
    repeating_digs =[]
    for i in range(10):
        count = str.count(''.join(n), str(i))
        if count >1:
            repeating_digs.append(i)
    return repeating_digs


def replace(lst_digits, digit, i):
    '"takes in a list of digits, and converts it to a full scale numbe"'
    lst_digits = str.replace(''.join(lst_digits), digit, i)
    return int(''.join(lst_digits))

def problem51():
    for prime in digit_primes:
        if repeating_digit(prime):
            for rep_dig in repeating_digit(prime):
                count = 1
                for i in [digit for digit in range(10) if digit!= rep_dig]:
                    new_prime = replace(prime, str(rep_dig), str(i))
                    if new_prime in set_primes and len(str(new_prime))== len(prime):
                        count +=1
                        if count ==8:
                            return ''.join(prime)

print(problem51())
