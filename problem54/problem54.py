"""NOTE: Need to update checks so that if they both get it you return 0"""

import operator

f = open('p054_poker.txt','r')
cards = f.read().split()
player1 =[]
player2 =[]

for i in range(0, len(cards),5):
    if i%2 ==0:
        player1.append(cards[i:i+5])
    else:
        player2.append(cards[i:i+5])

card_vals = ['2','3','4','5','6','7','8','9', 'T','J','Q','K','A']
card_suits = ['H','C','S','D']

###################################
def values(hand):
    values = []
    for card in hand:
        values.append(card[0])
    return values

def suits(hand):
    suits = []
    for card in hand:
        suits.append(card[1])
    return suits

def index(card_val):
    for i in range(len(card_vals)):
        if card_vals[i] == card_val:
            return i
    return 0

def count(values):
    # works both for counting pairs and counting if there is a flush or not
    vals = []
    counts = []
    for card in range(5):
        count = 1
        if values[card] not in vals:
            for i in range(1,5):
                if i+card < 5 and values[card] == values[i+card]:
                    count +=1
                    vals.append(values[card])
            counts.append([count, values[card]])
    real_counts = [count for count in counts if count[0] > 1]
    if len(real_counts)>=1:
        return real_counts + [[0,0]] +[[0,0]]
    else:
        return [[0,0],[0,0]]


###################################
def highCard(hand1, hand2):
    values1 = values(hand1)
    values2 = values(hand2)

    indexs1 = []
    indexs2 = []
    for value in values1:
        indexs1.append([index(value), value])
    for value in values2:
        indexs2.append([index(value), value])

    max1  = max(indexs1, key =operator.itemgetter(0))
    max2 = max(indexs2, key =operator.itemgetter(0))
    if max1[0] > max2[0]:
        return 1
    elif max2[0]> max1[0]:
        return 2
    else:
        return highCard(hand1.remove(max1[1]), hand2.remove(max2[1]))

def pairs(hand1, hand2):
    #compares who has one pair or two pairs
    count1 = count(values(hand1))
    count2 = count(values(hand2))

    if len(count1) > len(count2):
        return 1
    if len(count2) > len(count1):
        return 2
    else:
        pair_vals1 = []
        for coun in count1:
            pair_vals1.append(index(coun[1]))
        pair_vals2 = []
        for coun in count2:
            pair_vals2.append(index(coun[1]))

        if max(pair_vals2) > max(pair_vals1):
            return 2
        if max(pair_vals1) > max(pair_vals2):
            return 1
        else:
            return highCard(hand1,hand2)

def threeOfKind(hand1,hand2):
    #compares only who has three of a kind
    count1 = max(count(values(hand1)), key = operator.itemgetter(0))
    count2 = max(count(values(hand2)), key = operator.itemgetter(0))

    if count1[0] ==3 and count2[0] ==3:
        if index(count1[1]) > index(count2[1]):
            return 1
        elif index(count2[1]) > index(count1[1]):
            return 2
        else:
            return highCard(hand1,hand2)

    if count1[0] ==3:
        return 1
    if count2[0] ==3:
        return 2


def straight(hand1,hand2):
    values1 = sorted(values(hand1), key = index)
    values2 = sorted(values(hand2), key = index)
    straight1 =False
    straight2 =False

    for card_val in range(len(values1)-1):
        if index(values1[card_val]) +1 == index(values1[1+card_val]) or index(values1[card_val]) +9 == index(values1[1+card_val]) : #This only works if there is a sequential thing, I need to sort the
            straight1 = True
        else:
            straight1 = False
            break

    for card_val in range(len(values2)-1):
        if index(values2[card_val]) +1 == index(values2[card_val+1]) or index(values2[card_val]) +9 == index(values2[1+card_val]):
            straight2 =True
        else:
            straight2 =False
            break

    if straight1 and straight2:
        return highCard(hand1,hand2)
    if straight1:
        return 1
    if straight2:
        return 2


def flush(hand1, hand2):
    #requires a tiebreak
    count1 = count(suits(hand1))[0][0]
    count2 = count(suits(hand2))[0][0]

    if count1 == 5 and count2 ==5:
        return highCard(hand1,hand2)
    if count1 ==5:
        return 1
    if count2 ==5:
        return 2

def fullHouse(hand1, hand2):
    count1 = count(values(hand1))
    count2 = count(values(hand2))
    if count1[0][0] + count1[1][0] ==5 and count2[0][0] + count1[1][0] ==5:
        return threeOfKind(hand1,hand2) #decide who has the higher three of a kind if both have full houses
    if count1[0][0] + count1[1][0] ==5:
        return 1
    if count2[0][0] + count2[1][0] ==5:
        return 2

def fourOfAKind(hand1, hand2):
    count1 = count(values(hand1))[0]# works on the critical assumption that if there is a four of a kind, then there can only be one pair possible
    count2 = count(values(hand2))[0]

    if count1[0] ==4 and count2[0] ==4:
        if count1[1] >count2[1]:
            return 1
        elif count2[1] > count1[1]:
            return 2
        else:
            return highCard(hand1,hand2)

    if count1[0]==4:
        return 1
    if count2[0] ==4:
        return 2

def straightFlush(hand1,hand2):
    if flush(hand1,hand2) ==1 and straight(hand1,hand2) == 1 and flush(hand1,hand2) ==2 and straight(hand1,hand2) == 2:
        return highCard(hand1,hand2)
    if flush(hand1,hand2) ==1 and straight(hand1,hand2) == 1:
        return 1
    if flush(hand1,hand2) ==2 and straight(hand1,hand2) == 2:
        return 2


################################
def playHand(hand1, hand2):
    #return either a string hand1 or hand2

    if sorted(values(hand1), key = index) == ['A','2','3','4','5']:
        print(hand1, "Weird case Straight")
    if sorted(values(hand2), key = index) == ['A','2','3','4','5']:
        print(hand2, "Weird case Straight")

    if straightFlush(hand1,hand2):
        return straightFlush(hand1,hand2)
    if fourOfAKind(hand1,hand2):
        return fourOfAKind(hand1,hand2)
    if fullHouse(hand1,hand2):
        return fullHouse(hand1,hand2)
    if flush(hand1,hand2):
        return flush(hand1,hand2)
    if straight(hand1,hand2):
        return straight(hand1,hand2)
    if threeOfKind(hand1,hand2):
        return threeOfKind(hand1,hand2)
    if pairs(hand1,hand2):
        return pairs(hand1,hand2)
    if highCard(hand1,hand2):
        return highCard(hand1,hand2)

###########################################

oneWins =0
twoWins = 0

for game in range(1000):
    if playHand(player1[game], player2[game]) == 1:
        oneWins +=1
    if playHand(player1[game], player2[game]) == 2:
        twoWins +=1

print(oneWins)
