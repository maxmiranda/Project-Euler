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

def reverse(n):
    backwards = 0
    while n>0:
        backwards*= 10
        digit = n %10
        n = n//10
        backwards += digit
    return backwards

def is_lychrel(n):
    for i in range(50):
        if is_palindrome(n + reverse(n)):
            return False
        else:
            n= n + reverse(n)
    return True

total = 0
for n in range(1,10000):
    if is_lychrel(n):
        total +=1

print(total)
