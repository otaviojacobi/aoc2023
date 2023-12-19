from copy import deepcopy
with open('input.txt') as f:
    lines = [[int(x) for x in line.split()] for line in f.readlines()]


def build_diffs(nrs):
    diffs = []
    for i in range(len(nrs)-1):
        diffs.append(nrs[i+1] - nrs[i])

    return diffs

first_star = 0
second_star = 0
for line in lines:
    diff = build_diffs(line)
    history_diffs = [deepcopy(diff)]
    while diff != [0 for _ in range(len(diff))]:
        diff = build_diffs(diff)
        history_diffs.append(deepcopy(diff))

    total = 0
    total_2 = 0
    for hist in history_diffs:
        total += hist[-1]

    history_diffs.reverse()
    for hist in history_diffs:
        total_2 = hist[0] - total_2
    total += line[-1]
    total_2 = line[0] - total_2
    first_star += total
    second_star += total_2

print('first star', first_star)
print('second star', second_star)