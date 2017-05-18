def problem2(prev, curr):
    total = 0
    while curr< 4000000:
        prev, curr = curr, prev + curr
        if curr %2 == 0:
            total+= curr
    print(total)

problem2(1,1)
