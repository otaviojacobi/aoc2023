from typing import List, Tuple, cast 
from functools import lru_cache

with open('input.txt') as f:
    the_map = f.readlines()

start_pos: Tuple[int, int] | None = None
valid_positions = set()
for i in range(len(the_map)):
    for j in range(len(the_map[0])):
        
        try:
            if the_map[i][j] in '.S':
                valid_positions.add((i,j))
            if the_map[i][j] == 'S':
                start_pos = (i, j)
        except IndexError:
            pass

start_pos = cast(Tuple[int, int], start_pos)
queue: List[Tuple[int, int, int]] = [(start_pos[0], start_pos[1], 0)]
in_queue = set(queue)
# visited = set()


def children(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    children = [(pos[0]+1,pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1)]
    return [c for c in children if c in valid_positions]

total_at_64 = 0
counts = [0 for k in range(100)]
while True:

    element = queue.pop(0)
    in_queue.remove(element)

    # print(element[2])

    if element[2] == 65:
        break
    if element[2] == 64:
        total_at_64 += 1

    cds = children((element[0], element[1]))

    for child in cds:
        if (child[0], child[1], element[2]+1) not in in_queue:
            counts[element[2]] += 1
            in_queue.add((child[0], child[1], element[2]+1))
            queue.append((child[0], child[1], element[2]+1))
print(counts)
print('first star', total_at_64)