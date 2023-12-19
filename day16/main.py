from typing import List, Tuple, Set
with open('input.txt') as f:
    the_map = [l.strip() for l in f.readlines()]

LEFT = 0
UP = 1
DOWN = 2
RIGHT = 3

Node = Tuple[int, int, int]


def add_bfs(queue: List[Node], visited: Set[Node], child: Node) -> List[Node]:
    if child not in visited:
        queue.append(child)
    return queue

def get_initial_queue(the_map: List[str], i: int, j: int, initial_direction: int) -> List[Node]:
        char = the_map[i][j]
        if char == '.':
            return [(i, j, initial_direction)]
        elif char == '|':
            if initial_direction == RIGHT or initial_direction == LEFT:
               return [(i,j,UP), (i,j,DOWN)]
            else:
               return [(i,j,initial_direction)]
        elif char == '-':
            if initial_direction == UP or initial_direction == DOWN:
                return [(i,j,LEFT), (i,j,RIGHT)]
            else:
                return [(i,j,initial_direction)]
        elif char == '/':
            if initial_direction == RIGHT:
               return [(i,j,UP)]
            elif initial_direction == LEFT:
               return [(i,j,DOWN)]
            elif initial_direction == UP:
               return [(i,j,RIGHT)]
            elif initial_direction == DOWN:
               return [(i,j,LEFT)]
        elif char == '\\':
            if initial_direction == RIGHT:
               return [(i,j,DOWN)]
            elif initial_direction == LEFT:
               return [(i,j,UP)]
            elif initial_direction == UP:
               return [(i,j,LEFT)]
            elif initial_direction == DOWN:
               return [(i,j,RIGHT)]
            
        print('error')
        return []


def bfs(the_map: List[str], i: int, j: int, initial_direction: int):

    queue: List[Node] = get_initial_queue(the_map, i, j, initial_direction)

    visited = set()
    uniques = set()
    while len(queue) != 0:
        move = queue.pop()
        visited.add(move)

        (i, j, direction) = move
        uniques.add((i,j))

        if direction == RIGHT:
            next = [i, j+1]
        elif direction == LEFT:
            next = [i, j-1]
        elif direction == UP:
            next = [i-1, j]
        else:# direction == DOWN:
            next = [i+1, j]

        if (next[0] > len(the_map) - 1) or (next[0] < 0) or (next[1] > len(the_map[0])-1) or (next[1] < 0):
            continue

        next_char = the_map[next[0]][next[1]]
        if next_char == '.':
            child = (next[0], next[1], direction)
            queue = add_bfs(queue, visited, child)
        elif next_char == '|':
            if direction == RIGHT or direction == LEFT:
                queue = add_bfs(queue, visited, (next[0], next[1], UP))
                queue = add_bfs(queue, visited, (next[0], next[1], DOWN))
            else:
                queue = add_bfs(queue, visited, (next[0], next[1], direction))
        elif next_char == '-':
            if direction == UP or direction == DOWN:
                queue = add_bfs(queue, visited, (next[0], next[1], LEFT))
                queue = add_bfs(queue, visited, (next[0], next[1], RIGHT))
            else:
                queue = add_bfs(queue, visited, (next[0], next[1], direction))
        elif next_char == '/':
            if direction == RIGHT:
                queue = add_bfs(queue, visited, (next[0], next[1], UP))
            elif direction == LEFT:
                queue = add_bfs(queue, visited, (next[0], next[1], DOWN))
            elif direction == UP:
                queue = add_bfs(queue, visited, (next[0], next[1], RIGHT))
            elif direction == DOWN:
                queue = add_bfs(queue, visited, (next[0], next[1], LEFT))
        elif next_char == '\\':
            if direction == RIGHT:
                queue = add_bfs(queue, visited, (next[0], next[1], DOWN))
            elif direction == LEFT:
                queue = add_bfs(queue, visited, (next[0], next[1], UP))
            elif direction == UP:
                queue = add_bfs(queue, visited, (next[0], next[1], LEFT))
            elif direction == DOWN:
                queue = add_bfs(queue, visited, (next[0], next[1], RIGHT))
    return len(uniques)

print('first star', bfs(the_map, 0, 0, RIGHT))

initial_pos = [
    *[(0, j, DOWN) for j in range(len(the_map[0]))],
    *[(len(the_map)-1, j, UP) for j in range(len(the_map[0]))],
    *[(i, 0, RIGHT) for i in range(len(the_map))],
    *[(i, len(the_map[0])-1, LEFT) for i in range(len(the_map))],
]

print('second star', max([bfs(the_map, *pos) for pos in initial_pos]))