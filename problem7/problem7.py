def problem7(n):
    i = 0
    j =0
    while i <= n:
        if is_prime(j):
            i +=1
        j+=1
    print(j-1)



def is_prime(n):
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

problem7(10001)
