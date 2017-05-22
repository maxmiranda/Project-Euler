def same_digits(n):
    for i in range(2,7):
        if sorted(str(i*n)) != sorted(str(n)):
            return False
    return True


for n in range(1,1000000):
    if same_digits(n):
        print(n)
