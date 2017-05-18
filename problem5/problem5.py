def problem5():
    j= 2520*2
    while j> 5000:
        if evenly_div(j):
            return j
        j= j+16

def evenly_div(n):
    for i in range(2,20):
        if n%i:
            return False
    return True

print(problem5())
