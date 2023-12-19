from typing import List

with open('input.txt') as f:
    lines = f.readlines()

def as_listint(nrs: str) -> List[int]:
    return list(map(lambda x: int(x), filter(lambda x: x != '', nrs.strip().split(' '))))

lines = list(map(lambda x: x.split(':')[-1].strip().split('|'), lines))
first_star = 0
for (i, pair) in enumerate(list(lines)):
    results, numbers = set(as_listint(pair[0])), set(as_listint(pair[1]))
    common  = len(results.intersection(numbers))
    if common != 0:
        first_star += 2**(common-1)
print('first star', first_star)


card_count = {}
cur_iter = 0
score = 0
second_star = 0
for i in range(len(lines)):
    game = i + 1
    print(game)
    if game not in card_count.keys():
        card_count[game] = 1
    else:
        card_count[game] += 1

    result_hash = {}
    for _ in range(card_count[game]):
        if game not in result_hash.keys():
            results, numbers = set(as_listint(lines[game-1][0])), set(as_listint(lines[game-1][1]))
            common = len(results.intersection(numbers))
            result_hash[game] = common
        common = result_hash[game]
        for k in range(1, common+1):
            if game+k not in card_count.keys():
                card_count[game+k] = 1
            else:
                card_count[game+k] += 1

    second_star += card_count[game]

print('second star', second_star)

