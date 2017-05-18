def spiral(n):
    total = 1
    for i in range(3,n+1,2):
        total += i**2 + (i**2-(i-1)) +(i**2-2*(i-1)) + ((i**2)-3*(i-1))
    print(total)

spiral(1001)
