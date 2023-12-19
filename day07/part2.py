from functools import cmp_to_key
from copy import deepcopy

with open('input.txt') as f:
    lines = f.readlines()

def keywithmaxval(d):
     v = list(d.values())
     k = list(d.keys())
     return k[v.index(max(v))]

def make_best(hand):
    counts = {}
    for element in hand:
        if element == 'J':
            continue
        if element not in counts.keys():
            counts[element] = 0
        counts[element] += 1

    max_key = keywithmaxval(counts)

    new_hand = ''
    for k in hand:
        if k != 'J':
            new_hand += k
        else:
            new_hand += max_key

    # if score(hand, False) < score(new_hand):
    #     print('aqui', hand, new_hand)
    #     print('score', score(hand, False), score(new_hand))

    return new_hand

def score(hand, improve=True):
    # five of a kind
    if len(set(hand)) == 1:
        return 10

    hand = deepcopy(hand)
    if 'J' in hand and improve:
        hand = make_best(hand)

    # five of a kind
    if len(set(hand)) == 1:
        return 10

    counts = {}
    for element in hand:
        if element not in counts.keys():
            counts[element] = 0
        counts[element] += 1

    max_count = max(counts.values())
    # four of a kind
    if max_count == 4:
        return 9
    
    min_count = min(counts.values())
    if max_count == 3 and min_count == 2:
        return 8
    
    if max_count == 3:
        return 7
    
    amt_of_2s = list(counts.values()).count(2)
    if amt_of_2s == 2:
        return 6
    if amt_of_2s == 1:
        return 5
    return 4

elements = {
            'A': 20, 
            'K': 19,
            'Q': 18, 
            'T': 16, 
            '9': 15, 
            '8': 14, 
            '7': 13, 
            '6': 12, 
            '5': 11, 
            '4': 10, 
            '3': 9, 
            '2': 8,
            'J': 7,
            }
def element_score(elem):
    return elements[elem]

def cmp(hb1, hb2):
    scr1, scr2 = score(hb1['hand']), score(hb2['hand'])

    if scr1 > scr2:
        return 1
    elif scr1 < scr2:
        return -1
    
    # print('tie breaking ', hb1, hb2)
    # tie break
    for k in range(len(hb1['hand'])):
        if element_score(hb1['hand'][k]) > element_score(hb2['hand'][k]):
            return 1
        elif element_score(hb1['hand'][k]) < element_score(hb2['hand'][k]):
            return -1
        
    print('tie!!!')
    return 0

hands_and_bids = []
for line in lines:
    hands_and_bids.append({
        'hand': line.split()[0],
        'bid': int(line.split()[1]),
        'strength': score(line.split()[0])
    })

key = cmp_to_key(cmp)

hands_and_bids.sort(key=key)

total = 0
for i in range(len(hands_and_bids)):
    total += hands_and_bids[i]['bid'] * (i+1)


print('second star', total)
