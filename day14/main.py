from copy import deepcopy
with open('input.txt') as f:
    the_map = [l.strip() for l in f.readlines()]

def replace_str(the_str: str, pos: int, value: str):
    list_str = list(the_str)
    list_str[pos] = value
    return ''.join(list_str)

def tilt_north(the_map):
    for i in range(1, len(the_map)):
        for j in range(len(the_map[i])):
            if the_map[i][j] == 'O':
                # print(i,j)
                next_i = i - 1

                if the_map[next_i][j] == 'O' or the_map[next_i][j] == '#':
                    continue

                while next_i - 1 >= 0 and the_map[next_i-1][j] == '.':
                    next_i -= 1

                the_map[i] = replace_str(the_map[i], j, '.')
                the_map[next_i] = replace_str(the_map[next_i], j, 'O')

    return the_map

def rotate_cw(the_map):
    the_map = [list(line) for line in the_map]
    the_map = list(zip(*the_map[::-1]))
    return [''.join(line) for line in the_map]

def rotate_ccw(the_map):
    the_map = [list(line) for line in the_map]
    the_map = list(reversed(list(zip(*the_map))))
    return [''.join(line) for line in the_map]

def tilt_west(the_map):
    return rotate_ccw(tilt_north(rotate_cw(the_map)))

def tilt_south(the_map):
    return rotate_ccw(rotate_ccw(tilt_north(rotate_cw(rotate_cw(the_map))))) 

def tilt_east(the_map):
    return rotate_cw(tilt_north(rotate_ccw(the_map)))


tilted_map = tilt_north(deepcopy(the_map))
power = len(tilted_map)
total = 0
for line in tilted_map:
    total += line.count('O') * power
    power -= 1

print('first star', total)

# results = []
# for k in range(200):

#     total = 0
#     power = len(tilted_map)
#     for line in the_map:
#         total += line.count('O') * power
#         power -= 1

#     results.append((k, total))

#     # print(k, total)
#     the_map = tilt_north(the_map)
#     the_map = tilt_west(the_map)
#     the_map = tilt_south(the_map)
#     the_map = tilt_east(the_map)


# start_pos = 3
# repeating_cycle = [69, 69, 65, 64,65, 63, 68]


start_pos = 108
repeating_cycle = [96014,96003,95985,95971,95962,95961,95981,96001,96020]

pos = 1000000000

print('second star', repeating_cycle[(pos - start_pos) % len(repeating_cycle)])


