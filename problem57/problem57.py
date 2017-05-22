def expansion(n): # num is just the number that we're trying to expand on
    count = 0
    num = 1 + n
    denom = n
    for i in range(999):
        num, denom = num + n*denom, num + (n-1)*denom
        if len(str(num)) > len(str(denom)):
            count+=1
    return count
print(expansion(2))
