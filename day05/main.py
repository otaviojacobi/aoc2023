from copy import deepcopy
from math import inf
from tqdm import tqdm

with open('input.txt') as f:
    lines = f.readlines()

seeds = list(map(lambda x: int(x), lines[0].split(':')[-1].strip().split()))

cur_map = None
maps = {}
map_order = []
for line in lines:
    if line.endswith('map:\n'):
        cur_map = line.split()[0]
        map_order.append(cur_map)
        continue

    if cur_map == None or line == '\n':
        continue

    [dest_range_start, source_range_start, rangelen] = list(map(lambda x: int(x), line.split()))
    if cur_map not in maps:
        maps[cur_map] = [(dest_range_start, source_range_start, rangelen)]
    else:
        maps[cur_map].append((dest_range_start, source_range_start, rangelen))

def get_min(seeds):
    results = []
    for seed in seeds:
        value = seed
        for map_name in map_order:
            for mappings in maps[map_name]:
                if value >= mappings[1] and value < mappings[1] + mappings[2]:
                    diff = abs(value - mappings[1])
                    value = mappings[0] + diff
                    break
        results.append(value)
    return min(results)

def overlaps(r1, r2, m1, m2, diff):
    init = max(r1, m1)
    end =  min(r2, m2)

    # no overlap
    if init > end:
        return [[r1,r2, False]]

    overlaps = []
    if r1 < init:
        overlaps.append([r1, init, False])
    overlaps.append([init+diff, end+diff, True])
    if r2 > end:
        overlaps.append([end, r2, False])

    return overlaps

def get_min_for_range(seed_range):

    ranges = [[seed_range[0], seed_range[0] + seed_range[1], False]]

    mini = inf
    for map_name in map_order:
        for mappings in maps[map_name]:
            m1, m2 = mappings[1], mappings[1] + mappings[2]
            diff = mappings[0] - mappings[1]
            new_rgs = []
            for rg in ranges:
                r1, r2, already_processed = rg

                if already_processed:
                    new_rgs.append([r1, r2, True])
                    continue
                new_rgs += overlaps(r1, r2, m1, m2, diff)
            ranges = new_rgs

        ranges = [[r[0], r[1], False] for r in ranges]

    for rn in ranges:
        if rn[0] < mini:
            mini = rn[0]
    return mini

pairs = []
for i in range(0, len(seeds), 2):
    pairs.append([seeds[i], seeds[i+1]])

second_star = inf
for rns in pairs:
    res = get_min_for_range(rns)
    second_star = min(res, second_star)

print(f'first star {get_min(seeds)}')
print(f'second star {second_star}')

