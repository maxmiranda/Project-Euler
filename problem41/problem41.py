def generate_pandigs(start, end):
    sorted_pandigs=[]
    for i in range(start,end):
        pandig = ''
        for j in range(1,i):
            pandig += str(j)
        sorted_pandigs.append(pandig)
    def generate(s):
        if len(s) <= 1:
            yield [s]
        else:
            for perm in generate(s[1:]):
                for i in range(len(s)):
                    yield perm[:i] + [s[0:1]] + perm[i:]

    pandigs = []
    for pandig in sorted_pandigs:
        return list(generate(pandig))

pandigs = generate_pandigs(8,9) # just gonna test one by one

def is_prime(n):
    if n%2 ==0 or n%3 == 0:
        return False
    square_root = int(n**0.5)
    f = 5
    while f <= square_root:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f +=6
    return True

prime_pandigs = [''.join(pandig) for pandig in pandigs if is_prime(int(''.join(pandig)))]
print(max(prime_pandigs))
