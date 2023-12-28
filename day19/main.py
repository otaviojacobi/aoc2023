from typing import Tuple
from functools import reduce

with open('input.txt') as f:
    [workflows, ratings] = f.read().split('\n\n')

workflows = workflows.split('\n')
ratings = ratings.split('\n')

workflows = {wf.split('{')[0]: wf.split('{')[-1].strip('}').split(',') for wf in workflows}

Range = Tuple[int, int]
Ranges = Tuple[Range, Range, Range, Range]
ranges: Ranges = ((1, 4001), (1, 4001), (1, 4001), (1, 4001))


def possible_combinations(ranges: Ranges) -> int:
    return reduce(lambda x, y: x*y, [r[1] - r[0] if r[1]-r[0] != 0 else 1 for r in ranges ])

def count_combinations(ranges: Ranges, cur_wf: str, cur_wf_count: int):
    if cur_wf == 'A':
        return possible_combinations(ranges)

    if cur_wf =='R':
        return 0

    if ':' not in workflows[cur_wf][cur_wf_count]:
        return count_combinations(ranges, workflows[cur_wf][cur_wf_count], 0)
    
    [instr, next_wf] = workflows[cur_wf][cur_wf_count].split(':')
    if '<' in instr:
        [var, split] = instr.split('<')
        split = int(split)

        if var == 'x':
            if split >= ranges[0][1] - 1: # entire range applies
                return count_combinations(ranges, next_wf, 0)
            if split <= ranges[0][0]: # none of the range applies
                return count_combinations(ranges, cur_wf, cur_wf_count+1)

            # we know split is in the middle of the range
            r1 = ((ranges[0][0], split), ranges[1], ranges[2], ranges[3]) # all the <
            r2 = ((split, ranges[0][1]), ranges[1], ranges[2], ranges[3]) # the remaining >=
            return count_combinations(r1, next_wf, 0) + count_combinations(r2, cur_wf, cur_wf_count=+1)
        elif var == 'm':
            if split >= ranges[1][1] - 1: # entire range applies
                return count_combinations(ranges, next_wf, 0)
            if split <= ranges[1][0]: # none of the range applies
                return count_combinations(ranges, cur_wf, cur_wf_count+1)
            # we know split is in the middle of the range
            r1 = (ranges[0], (ranges[1][0], split), ranges[2], ranges[3]) # all the <
            r2 = (ranges[0], (split, ranges[1][1]), ranges[2], ranges[3]) # the remaining >=
            return count_combinations(r1, next_wf, 0) + count_combinations(r2, cur_wf, cur_wf_count=+1)
        elif var == 'a':
            if split >= ranges[2][1] - 1: # entire range applies
                return count_combinations(ranges, next_wf, 0)
            if split <= ranges[2][0]: # none of the range applies
                return count_combinations(ranges, cur_wf, cur_wf_count+1)
            # we know split is in the middle of the range
            r1 = ( ranges[0], ranges[1], (ranges[2][0], split), ranges[3]) # all the <
            r2 = ( ranges[0], ranges[1], (split, ranges[2][1]), ranges[3]) # the remaining >=
            return count_combinations(r1, next_wf, 0) + count_combinations(r2, cur_wf, cur_wf_count=+1)
        elif var == 's':
            if split >= ranges[3][1] - 1: # entire range applies
                return count_combinations(ranges, next_wf, 0)
            if split <= ranges[3][0]: # none of the range applies
                return count_combinations(ranges, cur_wf, cur_wf_count+1)

            # we know split is in the middle of the range
            r1 = (ranges[0], ranges[1], ranges[2], (ranges[3][0], split)) # all the <
            r2 = (ranges[0], ranges[1], ranges[2], (split, ranges[3][1])) # the remaining >=

            return count_combinations(r1, next_wf, 0) + count_combinations(r2, cur_wf, cur_wf_count=+1)
        else:
            print('wrong var')
            exit(1)


    elif '>' in instr:
        [var, split] = instr.split('>')
        split = int(split)

        if var == 'x':
            if split >= ranges[0][1] - 1: # none of the range applies
                return count_combinations(ranges, cur_wf, cur_wf_count+1)
            if split <= ranges[0][0]: # entire range applies
                return count_combinations(ranges, next_wf, 0)
            # we know split is in the middle of the range

            r1 = ((split+1, ranges[0][1]), ranges[1], ranges[2], ranges[3]) # all the >
            r2 = ((ranges[0][0], split+1), ranges[1], ranges[2], ranges[3]) # the remaining <=

            return count_combinations(r1, next_wf, 0) + count_combinations(r2, cur_wf, cur_wf_count=+1)
        elif var == 'm':
            if split >= ranges[1][1] - 1:
                return count_combinations(ranges, cur_wf, cur_wf_count+1)
            if split <= ranges[1][0]:
                return count_combinations(ranges, next_wf, 0)

            # we know split is in the middle of the range
            r1 = (ranges[0], (split+1, ranges[1][1]), ranges[2], ranges[3])
            r2 = (ranges[0], (ranges[1][0], split+1), ranges[2], ranges[3])

            return count_combinations(r1, next_wf, 0) + count_combinations(r2, cur_wf, cur_wf_count=+1)
        elif var == 'a':
            if split >= ranges[2][1] - 1:
                return count_combinations(ranges, cur_wf, cur_wf_count+1)
            if split <= ranges[2][0]: 
                return count_combinations(ranges, next_wf, 0)
            # we know split is in the middle of the range
            r1 = ( ranges[0], ranges[1], (split+1, ranges[2][1]), ranges[3])
            r2 = ( ranges[0], ranges[1], (ranges[2][0], split+1), ranges[3])
            return count_combinations(r1, next_wf, 0) + count_combinations(r2, cur_wf, cur_wf_count=+1)
        elif var == 's':
            if split >= ranges[3][1] - 1:
                return count_combinations(ranges, cur_wf, cur_wf_count+1)
            if split <= ranges[3][0]:
                return count_combinations(ranges, next_wf, 0)
            # we know split is in the middle of the range
            r1 = (ranges[0], ranges[1], ranges[2], (split+1, ranges[3][1]))
            r2 = (ranges[0], ranges[1], ranges[2], (ranges[3][0], split+1))
            return count_combinations(r1, next_wf, 0) + count_combinations(r2, cur_wf, cur_wf_count=+1)
        else:
            print('wrong var2')
            exit(1)
    else:
        print('deu pau')
        exit(1)


total = 0
for rate in ratings:
    [x, m, a, s] = list(map(lambda x: int(x.split('=')[-1]), rate.strip('{}').split(',')))
    
    cur_wf = 'in'
    cur_wf_count = 0
    while True:
        # print(x,m,a,s)
        instr = workflows[cur_wf][cur_wf_count]
        # print(instr)

        if ':' in instr:
            if  eval(instr.split(':')[0]):
                next_move = instr.split(':')[1]
            else:
                next_move = None
        else:
            next_move = instr

        # print(next_move)
        if next_move == None:
            cur_wf_count += 1
            continue

        if next_move == 'A' or next_move == 'R':
            if next_move == 'A':
                total += sum([x,m,a,s])
            break

        cur_wf = next_move
        cur_wf_count = 0

print('first star', total)
print('second star', count_combinations(ranges, 'in', 0))