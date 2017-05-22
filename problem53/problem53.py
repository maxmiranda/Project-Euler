def combination(n,r):
    return fact(n) / (fact(r) * fact(n-r))

def fact(n):
    if n == 1 or n ==0:
        return 1
    else:
        return n * fact(n-1)

count = 0
for n in range(1,101):
    for r in range(n+1):
        if combination(n,r) >1000000:
            count +=1

print(count)
