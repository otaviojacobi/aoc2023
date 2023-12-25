from typing import List, Tuple, Set, Dict
from heapq import heappush, heappop
from collections import defaultdict

with open('input.txt') as f:
    the_map = [[int(n) for n in f.strip('\n')] for f in f.readlines()]

UP=0
DOWN=1
LEFT=2
RIGHT=3

MIN_MOVES = 1
MAX_MOVES = 3

class Node:
    def __init__(self, x: int, y: int, dir: int, steps: int):
        self.x = x
        self.y = y
        self.dir = dir
        self.steps = steps

    def __hash__(self):
        return int(f'{self.x}{self.y}{self.dir}{self.steps}')
    
    # just so minheap triebeak is not annoyed
    def __lt__(self, _other):
        return True
        
    def __eq__(self, other):
        return (self.x, self.y, self.dir, self.steps) == (other.x, other.y, other.dir, other.steps)

    def __repr__(self):
        direction = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        return str((self.x, self.y, direction[self.dir], self.steps))

    def is_valid(self):
        if self.x == 0 and self.y == 0:
            return False

        return self.x >= 0 and self.y >= 0 and self.x < len(the_map[0]) and self.y < len(the_map) and self.steps <= MAX_MOVES

    def desloc(self, other: "Node") -> int:
        if self.x == other.x:
            if self.y > other.y: # moving right add up to me if I am 4 and they are 3, add just me
                return sum([the_map[self.x][k] for k in range(other.y, self.y)])
            else: # moving left, add up to them if I am 4 and they are 3, add just them
                return sum([the_map[self.x][k] for k in range(self.y+1, other.y+1)])
            
        elif self.y == other.y:
            if self.x > other.x:
                return sum([the_map[k][self.y] for k in range(other.x, self.x)])
            else:
                return sum([the_map[k][self.y] for k in range(self.x+1, other.x+1)])
        else:
            print('something is not right')
            return 0


    def generate_neibs(self, visited: Set["Node"]):

        if self.dir == UP:
            if self.steps < MIN_MOVES:
                print('Algo errado no UP')
            up = Node(self.x, self.y - 1, UP, self.steps + 1 if self.dir == UP else 1)
            right = Node(self.x + MIN_MOVES, self.y, RIGHT, MIN_MOVES)
            left = Node(self.x - MIN_MOVES, self.y, LEFT, MIN_MOVES)
            starting_set = [up, right, left]
        elif self.dir == DOWN:
            if self.steps < MIN_MOVES:
                print('Algo errado no DOWN')
            down = Node(self.x, self.y + 1, DOWN, self.steps + 1 if self.dir == DOWN else 1)
            right = Node(self.x + MIN_MOVES, self.y, RIGHT, MIN_MOVES)
            left = Node(self.x - MIN_MOVES, self.y, LEFT, MIN_MOVES)
            starting_set = [down, right, left]
        elif self.dir == RIGHT:
            if self.steps < MIN_MOVES:
                print('Algo errado no RIGHT')
            right = Node(self.x + 1, self.y, RIGHT, self.steps + 1 if self.dir == RIGHT else 1)
            up = Node(self.x, self.y - MIN_MOVES, UP, MIN_MOVES)
            down = Node(self.x, self.y + MIN_MOVES, DOWN, MIN_MOVES)
            starting_set = [right, up, down]
        else:#  self.dir == LEFT:
            if self.steps < MIN_MOVES:
                print('Algo errado no LEFT')
            left = Node(self.x - 1, self.y, LEFT, self.steps + 1 if self.dir == LEFT else 1)
            up = Node(self.x, self.y - MIN_MOVES, UP, MIN_MOVES)
            down = Node(self.x, self.y + MIN_MOVES, DOWN, MIN_MOVES)
            starting_set = [left, up, down]

        return [n for n in starting_set if n.is_valid() and n not in visited]

def solve():
    queue: List[Tuple[int, Node]] = []
    nd1 = Node(0, MIN_MOVES, DOWN, MIN_MOVES)
    nd2 = Node(MIN_MOVES, 0, RIGHT, MIN_MOVES)
    dist: Dict[Node, int] = defaultdict(lambda: 999999999999999)
    dist[nd1] = sum(the_map[0][k] for k in range(1, MIN_MOVES+1))
    dist[nd2] = sum(the_map[k][0] for k in range(1, MIN_MOVES+1))
    prev: Dict[Node, Node]= {}
    inqueued: Set[Node] = set([nd1, nd2])

    # print(dist)

    heappush(queue, (dist[nd1], nd1))
    heappush(queue, (dist[nd2], nd2))
    while len(queue) > 0:
        (weight, u) = heappop(queue)

        # print(u)
        neibs = u.generate_neibs(inqueued)
        # print('neibs', neibs)
        for v in neibs:
            inqueued.add(v)
            
            to_add = u.desloc(v)

            # print('add', v, to_add, the_map[v.x][v.y])
            alt = dist[u] + to_add
            heappush(queue, (alt, v))

            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    min_v = 999999999
    for (k, v) in dist.items():
        if k.x == len(the_map[0]) - 1 and k.y == len(the_map) - 1:
            # print(k, v)
            min_v = min(min_v, v)

    return min_v

print('first star', solve())
MIN_MOVES = 4
MAX_MOVES = 10
print('second star', solve())

