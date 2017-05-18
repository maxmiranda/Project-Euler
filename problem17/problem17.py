import inflect

p = inflect.engine()


def numbersToStrings(n):
    print(sum([special_len(p.number_to_words(i)) for i in range(1,n+1)]))

def special_len(string):
    count = 0
    for i in string:
        if i == ' ' or i == '-':
            count+= 1
    return len(string) - count

numbersToStrings(1000)
