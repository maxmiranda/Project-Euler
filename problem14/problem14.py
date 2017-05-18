import operator

def problem14():
    hailstone_lengths = [hailstone_length(i,0) for i in range(1,1000000)]
    index, value = max(enumerate(hailstone_lengths), key=operator.itemgetter(1))
    print(index)

def hailstone_length(n,length):

    if n==1:
        return length +1
    elif n%2 ==0:
        return hailstone_length(n/2, length+1)
    else:
        return hailstone_length(3*n+1, length+1)

problem14()
