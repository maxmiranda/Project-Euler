def problem4():
    arr = []
    for i in range(999, 900,-1):
        for j in range(999,900, -1):
            arr.append(i*j)
    arr = sorted(arr,reverse = True)
    for k in arr:
        if is_palindrome(k):
            return k

def is_palindrome(n):
    i=n
    backwards = 0
    while i>0:
        backwards*= 10
        j = i %10
        i = i//10
        backwards+=j
    if backwards == n:
        return True
    return False

print(problem4())
