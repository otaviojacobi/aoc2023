from typing import Tuple, List
from shapely.geometry import Polygon


Command = Tuple[str, int, str]
Position = Tuple[int, int]
with open('input.txt') as f:
    commands: List[Command] = [(l.split()[0], int(l.split()[1]), l.split()[2].strip('()')) for l in f.readlines()]


points: List[Position] = [(0,0)]
points2: List[Position] = [(0,0)]
for command in commands:
    (direction, step, hexcode) = command

    if direction == 'R':
        points.append((points[-1][0]+step, points[-1][1]))
    elif direction == 'L':
        points.append((points[-1][0]-step, points[-1][1]))
    elif direction == 'U':
        points.append((points[-1][0], points[-1][1]-step))
    elif direction == 'D':
        points.append((points[-1][0], points[-1][1]+step))


    step, direction = int(hexcode[1:6], 16), hexcode[-1]

    if direction == '0':
        points2.append((points2[-1][0]+step, points2[-1][1]))
    elif direction == '2':
        points2.append((points2[-1][0]-step, points2[-1][1]))
    elif direction == '3':
        points2.append((points2[-1][0], points2[-1][1]-step))
    elif direction == '1':
        points2.append((points2[-1][0], points2[-1][1]+step))

def count_internal(p: Polygon) -> int:
    # pick's theorem area = internal_points + (perimeter_points / 2) - 1
    # internal internal_points = area + 1 - (perimiter_points /2)
    return p.area - (p.length/2) + 1

p = Polygon(points)
print('first star', int(p.length + count_internal(p)))
p = Polygon(points2)
print('second star', int(p.length + count_internal(p)))