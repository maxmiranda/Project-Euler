from functools import reduce
from operator import mul

def pandig(str1):
    if ''.join(sorted(str1)) == '123456789':
        return True
    return False

maximum = ''
for x in range(1000000):
    for i in range(5):
        lst = [j for j in range(1,i)]
        str1 = ''
        for i in lst:
            str1+= str(i*x)
        if pandig(str1) and maximum<str1:
            maximum = str1

print(maximum)
