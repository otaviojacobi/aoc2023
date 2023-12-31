from typing import List, Tuple, cast 
from math import ceil

with open('input.txt') as f:
    the_map = [l.strip() for l in f.readlines()]


# print(len(the_map))
# print(len(the_map[0]))

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

def children(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    # TODO: consider infinite map

    # c0 = (pos[0]+1 ,pos[1], False) if pos[0] + 1 < len(the_map) else (0, pos[1], True)
    # c1 = (pos[0] ,pos[1]+1, False) if pos[1] + 1 < len(the_map) else (pos[0], 0, True)
    # c2 = (pos[0]-1, pos[1], False) if pos[0] - 1 >= 0 else (len(the_map) - 1, pos[1], True)
    # c3 = (pos[0], pos[1]-1, False) if pos[1] - 1 >= 0 else (pos[0], len(the_map) - 1, True)

    children = [
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
    ]
    return [c for c in children if ((c[0] % len(the_map)), (c[1] % len(the_map))) in valid_positions]


Points = Tuple[Tuple[int,int],...]

def new_steps(current: Points, origins: Points) -> Points:
    origins_set = set(origins)
    new_points = set()
    for p in current:
        for c in children(p):
            if c not in origins_set:
                new_points.add(c)
    # print(new_points)
    return tuple(new_points)

current = (start_pos,)
origins = ()

# dp = defaultdict(lambda: 0)
dp = [0 for _ in range(330)]
gen_steps = []
dp[0] = 1
for i in range(1, 330):
    # print(i, current, origins)
    new_points = new_steps(current, origins)

    gen_steps.append(len(new_points))
    if i - 2 >= 0:
        dp[i] = dp[i-2] + len(new_points)
    else:
        dp[i] = len(new_points)

    origins = current
    current = new_points

def coefficient(x: Tuple[int, int, int], y: Tuple[int, int, int]) -> Tuple[float, float, float]:
    x_1 = x[0]
    x_2 = x[1]
    x_3 = x[2]
    y_1 = y[0]
    y_2 = y[1]
    y_3 = y[2]

    a = y_1/((x_1-x_2)*(x_1-x_3)) + y_2/((x_2-x_1)*(x_2-x_3)) + y_3/((x_3-x_1)*(x_3-x_2))

    b = (-y_1*(x_2+x_3)/((x_1-x_2)*(x_1-x_3))
         -y_2*(x_1+x_3)/((x_2-x_1)*(x_2-x_3))
         -y_3*(x_1+x_2)/((x_3-x_1)*(x_3-x_2)))

    c = (y_1*x_2*x_3/((x_1-x_2)*(x_1-x_3))
        +y_2*x_1*x_3/((x_2-x_1)*(x_2-x_3))
        +y_3*x_1*x_2/((x_3-x_1)*(x_3-x_2)))

    return a,b,c

a,b,c = coefficient((65, 196, 327), (dp[65], dp[196], dp[327]))

print(a, b, c)

f = lambda x: a * x * x + b * x + c

print('frst star', dp[64])
print('second star', ceil(f(26501365)))
