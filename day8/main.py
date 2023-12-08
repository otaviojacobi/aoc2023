with open('input.txt') as f:
    lines = list(filter(lambda x: x != '', [line.strip() for line in f.readlines()]))

instructions = lines[0]
tmap = {line.split('=')[0].strip(): [k.strip() for k in line.split('=')[1].strip(' ()').split(',')] for line in lines[1:]}

position = 'AAA'
count = 0
while position != 'ZZZ':
    for instr in instructions:
        if instr == 'R':
            position = tmap[position][1]
        else:
            position = tmap[position][0]
        count += 1
        if position == 'ZZZ':
            break
print('first star', count)
