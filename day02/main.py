from typing import List
with open('input.txt', 'r') as f:
    lines = f.readlines()

ngames: List[List[str]] = list(map(lambda x: list(map(lambda y : y.strip().split(','), x.split(':')[-1].split(';'))), lines))


maxes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}
first_star = 0
games = []
powers = []
for (i, ngame) in enumerate(ngames):
    id = i + 1
    is_id_viable = True
    game = []

    for nset in ngame:
        set = {}
        for nround in nset:
            parsed = nround.strip().split(' ')
            number = int(parsed[0])
            color = parsed[1]

            if number > maxes[color]:
                is_id_viable = False


            if color in set.keys():
                set[color] += number
            else:
                set[color] = number
        game.append(set)

    max_round = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for s in game:
        for k in s.keys():
            if s[k] > max_round[k]:
                max_round[k] = s[k]
    powers.append(max_round)
    if is_id_viable:
        first_star += id

second_star = 0
for power in powers:
    second_star += power['red'] * power['green'] * power['blue']

print(first_star)
print(second_star)