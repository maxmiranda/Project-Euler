def problem9():
    for a in range(1,1000):
        for b in range(1,1000):
            for c in range(1,1000):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a*b*c

print(problem9())
