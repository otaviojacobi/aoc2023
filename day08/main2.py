import math

with open('input.txt') as f:
    lines = list(filter(lambda x: x != '', [line.strip() for line in f.readlines()]))

instructions = lines[0]
tmap = {line.split('=')[0].strip(): [k.strip() for k in line.split('=')[1].strip(' ()').split(',')] for line in lines[1:]}

keys = [key for key in tmap.keys() if key.endswith('A')]


position = 'AAA'
count = 0
finished = False
factors = []
found = {}
while len(found.keys()) != len(keys):
    for instr in instructions:
        new_keys = []
        for key in keys:
            position = key
            if instr == 'R':
                position = tmap[position][1]
            else:
                position = tmap[position][0]
            new_keys.append(position)
        count += 1
        keys = new_keys
        
        for (i, key) in enumerate(keys):
            if key.endswith('Z'):
                if i not in found:
                    found[i] = count

        if len(found.keys()) == len(keys):
            break

lcm_result = math.lcm(*found.values())


print(f'second star {lcm_result}')
