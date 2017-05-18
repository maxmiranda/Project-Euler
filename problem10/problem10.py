def problem10(n):
    print(sum([i for i in range(n) if is_prime(i)]))

def is_prime(n):
    if n ==1: return False
    if n ==2 or n==3: return True
    if n%2 ==0 or n%3 == 0:
        return False
    square_root = int(n**0.5)
    f = 5
    while f <= square_root:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f +=6
    return True

problem10(2000000)
