from collections import defaultdict 
import math
from shapely.geometry import Point, Polygon


with open('input.txt') as f:
   lines = f.readlines()

the_map = defaultdict(lambda: set())
for (i, line) in enumerate(lines):
    for (j, char) in enumerate(line):
        if char == '-':
            the_map[(i,j)].add((i, j-1))
            the_map[(i,j)].add((i, j+1))
        elif char == 'L':
            the_map[(i,j)].add((i-1, j))
            the_map[(i,j)].add((i, j+1))
        elif char == '|':
            the_map[(i,j)].add((i-1, j))
            the_map[(i,j)].add((i+1, j))
        elif char == 'F':
            the_map[(i,j)].add((i+1, j))
            the_map[(i,j)].add((i, j+1))
        elif char == 'J':
            the_map[(i,j)].add((i-1, j))
            the_map[(i,j)].add((i, j-1))
        elif char == '7':
            the_map[(i,j)].add((i+1, j))
            the_map[(i,j)].add((i, j-1))
        elif char == '.':
            continue
        elif char == 'S':
            the_map['S'].add((i,j))
            the_map[(i,j)].add((i+1,j))
            the_map[(i,j)].add((i-1,j))
            the_map[(i,j)].add((i,j+1))
            the_map[(i,j)].add((i,j-1))

new_map = {}
for k in dict(the_map).keys():
    if k == 'S':
        new_map[k] = list(the_map[k])
        continue
    new_values = []
    for v in the_map[k]:
        if k in the_map[v]:
            new_values.append(v)
    new_map[k] = new_values

the_map = new_map

def backtrack(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

# print(the_map)
start, end = the_map[the_map['S'][0]]
seen = set()
seen.add(the_map['S'][0])
queue = [start]
parent = {}

print(start, end)
while len(queue) != 0:
    element = queue.pop(0)
    seen.add(element)

    adjacents = [e for e in the_map[element] if e not in seen]
    for adjacent in adjacents:
        parent[adjacent] = element
        queue.append(adjacent)

the_loop = backtrack(parent, start, end)
first_star = math.ceil(len(the_loop)/2)

the_loop = [the_map['S'][0]] + the_loop
the_loop.append(the_map['S'][0])
the_loop_set = set(the_loop)

nest = 0
poly = Polygon(the_loop)
for (i, line) in enumerate(lines):
    for (j, char) in enumerate(line):
        if (i,j) not in the_loop_set and  Point(i,j).within(poly):
            nest += 1


print(f'first star {first_star}')
print(f'second star {nest}')