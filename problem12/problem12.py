def problem12():
    arr = [i for i in range(2,1000000)]
    i=1
    while arr:
        if numbOfFactors(i):
            return i
        i+= arr.pop(0)

def numbOfFactors(n):
    count = 2
    for i in range(2,int(n**.5)):
        if n/i == i:
            count +=1
        elif n%i ==0:
            count +=2
    return count > 500

print(problem12())
