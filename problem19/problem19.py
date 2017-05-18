
def months(year):
    if year %100 == 0 and year %400 != 0:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 ==0:
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def gen():
    day = 0
    while True:
        for i in range(2,9):
            yield i

day = gen()

def run_century():
    count = 0
    year = 1901
    while year<2001:
        for month in range(12):
            days_in_month = months(year)[month]
            date=1
            while date <= days_in_month:
                if next(day) ==7 and date == 1: 
                    count +=1
                date+=1
        year +=1
    print(count)


run_century()
