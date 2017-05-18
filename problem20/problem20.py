def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(sum([int(x) for x in str(fact(100))]))
