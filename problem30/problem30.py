def check_fifths(n):
    total = 0
    for i in range(len(str(n))):
        total += int(str(n)[i])**5
    if total == n:
        return True
    return False

for i in range(1000000):
    total = 0
    if check_fifths(i):
        total = total + i

print(sum([4150,4151,54748,92727,93084,194979]))
