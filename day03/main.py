with open('input.txt') as f:
    lines = f.readlines()

linelen = len(lines[0])

schematic = ''.join(lines)

def is_special(c):
    return c != '.' and c != '\n' and not c.isnumeric()

def has_char_near(pos: int, size: int, schematic: str):

    if is_special(schematic[pos]) or is_special(schematic[pos-size-1]):
        return True

    before_start = max(pos-size-linelen-1, 0)
    before_end = max(pos-linelen+1, 0)
    after_start = max(pos-size+linelen-1, 0)
    after_end = max(pos+linelen+1, 0)
    try:
        for c in schematic[before_start:before_end]:
            if is_special(c):
                return True
        for c in schematic[after_start:after_end]:
            if is_special(c):
                return True
            
    except IndexError:
        print("index out")
    return False

cur_str = ''
valid_numbers = []
for (i, char) in enumerate(schematic):
    if char.isnumeric():
        cur_str += char
    else:
        if cur_str != '':
            if has_char_near(i, len(cur_str), schematic):
                valid_numbers.append(int(cur_str))
        cur_str = ''

second_star = 0
for (i, char) in enumerate(schematic):

    if char == '*':
        factors = []
        nr = ''
        left_idx = max(i-1, 0)
        if schematic[left_idx].isnumeric():
            nr = schematic[left_idx]
            aux = max(i-2, 0)
            while aux != 0 and schematic[aux].isnumeric():
                nr = f'{schematic[aux]}{nr}'
                aux = aux - 1
        if nr != '':
            factors.append(int(nr))

        nr = ''
        right_idx = i + 1
        if schematic[right_idx].isnumeric():
            nr = schematic[right_idx]
            aux = i + 2
            while schematic[aux].isnumeric():
                nr = f'{nr}{schematic[aux]}'
                aux = aux + 1

        if nr != '':
            factors.append(int(nr))

        start_lookup = i-linelen-1
        end_lookup = i-linelen+1

        while schematic[start_lookup].isnumeric() and start_lookup > 0:
            start_lookup -= 1
        while schematic[end_lookup].isnumeric():
            end_lookup += 1

        results = list(filter(lambda x: x != '', schematic[start_lookup:end_lookup].split('.')))
        for result in results:
            factors.append(int(result))

        start_lookup = i+linelen-1
        end_lookup = i+linelen+1

        while schematic[start_lookup].isnumeric() and start_lookup > 0:
            start_lookup -= 1
        while schematic[end_lookup].isnumeric():
            end_lookup += 1

        results = list(filter(lambda x: x != '', schematic[start_lookup:end_lookup].split('.')))
        for result in results:
            factors.append(int(result))
        

        if len(factors) == 2:
            second_star += factors[0] * factors[1]

print('first star', sum(valid_numbers))
print('second star', second_star)