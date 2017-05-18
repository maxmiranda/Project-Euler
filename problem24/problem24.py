
"""
Type out what you want to happen in getPermuations, a recursive function
meant to take in a list of numbers and return a permutation of every possible
combination of those numbers:

First: let's have first call create len(lst)-1 calls for every single

"""


def permutation(lst):
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
       digit  = lst[i]
       partLst = lst[:i] + lst[i+1:]
       for p in permutation(partLst):
           l.append([digit] + p)
    return l


perms = permutation([i for i in range(10)])
perms.sort()
print(perms[999999])
