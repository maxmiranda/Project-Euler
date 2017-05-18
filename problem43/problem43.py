divisors = [2,3,5,7,11,13,17]

def generate_pandigs(start, end):
    sorted_pandigs=[]
    for i in range(start,end):
        pandig = ''
        for j in range(i):
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

pandigs = generate_pandigs(10,11) # just gonna test one by one

def subst_is_div(pandig):
    digitLst =[]
    for i in range(7):
        digitLst.append(int(''.join(pandig[i+1:i+4])))
    for i in range(7):
        if not digitLst[i] % divisors[i]==0:
            return False
    return True

pandigs = [int(''.join(pandig)) for pandig in pandigs if subst_is_div(pandig)]

print(sum(pandigs))
