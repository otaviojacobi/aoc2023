from copy import deepcopy
from typing import List

with open('input.txt') as f:
    maps = [m.split('\n') for m in f.read().split('\n\n')]

def find_horizontal_symmetry(the_map, debug=False) -> List[int]:
    duplicated = []
    for c in range(len(the_map)-1):
        if the_map[c] == the_map[c+1]:
            duplicated.append(c)
    
    if debug:
        print(duplicated)

    simetries = []
    for k in duplicated:
        v1 = k
        v2 = k+1
        while True:
            if v1 == -1 or v2 == len(the_map):
                simetries.append(k)
                break

            if the_map[v1] == the_map[v2]:
                v1 -= 1
                v2 += 1
            else:
                break

    return simetries

def transpose(the_map):
    new_list = []
    for i in range(len(the_map[0])):
        # maiking a list with its index element and convert it into string.
        new_string = ''.join([ls[i] for ls in the_map])
        # appending the new_string int new_list
        new_list.append(new_string)
    return new_list

def find_vertical_symmetry(the_map, debug=False):
    tmap = transpose(the_map)
    if debug:
        print('\n'.join(the_map))
        print('\n')
        print('\n'.join(tmap))
    return find_horizontal_symmetry(tmap, debug)

def generate_with_change(the_map):
    all_maps = []
    for i in range(len(the_map)):
        for j in range(len(the_map[i])):
            new_map = deepcopy(the_map)
            new_map[i] = list(new_map[i])
            new_map[i][j] = '.' if the_map[i][j] == '#' else '#'
            new_map[i] = ''.join(new_map[i])
            all_maps.append((new_map, (i,j)))

    return all_maps

total_vs = 0
total_hs = 0
for the_map in maps:
    hs = find_horizontal_symmetry(the_map)
    vs = find_vertical_symmetry(the_map)
    hs = hs[0] if len(hs) > 0 else None
    vs = vs[0] if len(vs) > 0 else None
    total_hs += hs+1 if hs != None else 0
    total_vs += vs+1 if vs != None else 0

print('first star', (total_hs * 100) + total_vs)

total_vs = 0
total_hs = 0
for (m, the_map) in enumerate(maps):
    original_hs = find_horizontal_symmetry(the_map)
    original_vs = find_vertical_symmetry(the_map)
    original_hs = original_hs[0] if len(original_hs) > 0 else None
    original_vs = original_vs[0] if len(original_vs) > 0 else None
    for (new_map, ij) in generate_with_change(the_map):
        hs = [k for k in find_horizontal_symmetry(new_map) if k != original_hs]
        vs = [k for k in find_vertical_symmetry(new_map) if k != original_vs]
        hs = hs[0] if len(hs) > 0 else None
        vs = vs[0] if len(vs) > 0 else None
        if hs != None or vs != None:
            total_hs += hs+1 if hs != None else 0
            total_vs += vs+1 if vs != None else 0
            break

print('second star', (total_hs * 100) + total_vs)
