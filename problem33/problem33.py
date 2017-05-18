from operator import mul
from functools import reduce

nums_denoms =[]

for num in range(11, 100):
    for denom in range(11,100):
        if str(num)[1] == str(denom)[0] and str(num)[0] != str(num)[1] and num < denom and int(str(denom)[1]) != 0 and num/denom == int(str(num)[0]) / int(str(denom)[1]):
            nums_denoms.append([num, denom])

for i in range(len(nums_denoms)):
    nums_denoms[i] = nums_denoms[i][0]/nums_denoms[i][1]

multiplied = reduce(mul, nums_denoms, 1)

print(multiplied)
