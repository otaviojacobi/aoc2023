from typing import Tuple
from functools import lru_cache

with open('input.txt') as f:
    lines = f.readlines()

lines = [{'map': line.split()[0], 'pos': tuple(int(nr) for nr in line.split()[1].split(','))} for line in lines]

@lru_cache
def count(the_map: str, positions: Tuple[int]) -> int:
    # print(the_map, positions)
    if the_map == '':
        return 1 if positions == () else 0
    
    if positions == ():
        return 1 if not '#' in the_map else 0

    result = 0

    # considers ? is .
    if the_map[0] in ".?":
        result += count(the_map[1:], positions)

    # considers ? is #
    if the_map[0] in "#?":
        # if there are enough characters to be consumed
        if positions[0] <= len(the_map):
            if '.' not in the_map[:positions[0]]:
                if len(the_map) == positions[0] or the_map[positions[0]] != '#':
                    result += count(the_map[positions[0]+1:], positions[1:])
    return result

total_matches = 0
for line in lines:
    total_matches += count(line['map'], line['pos'])

print('first star', total_matches)

second_lines = []
total_matches = 0
for line in lines:
    second_lines.append({'map': '?'.join([line['map'] for _ in range(5)]), 'pos': line['pos']*5})
for line in second_lines:
    total_matches += count(line['map'], line['pos'])

print('second star', total_matches)


