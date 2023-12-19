with open('input.txt') as f:
    inputs = f.read().replace('\n', '').split(',')

def run_hash(value: str) -> int:
    current_value = 0
    for chr in value:
        current_value += ord(chr)
        current_value *= 17
        current_value = current_value % 256

    return current_value

first_star = sum([run_hash(ipt) for ipt in inputs])
print('first star', first_star)

boxes = [[] for _ in range(256)]
boxes_labels = [{} for _ in range(256)]
for instruction in inputs:
    # print(instruction)

    if '-' in instruction and '=' in instruction:
        print('ERROR')
        exit(1)

    if '-' in instruction:
        label = instruction.strip('-')
        boxi = run_hash(label)
        if label in boxes_labels[boxi].keys():
            del boxes[boxi][boxes_labels[boxi][label]]
            del boxes_labels[boxi][label]

            new_labels = {}
            for (k, v) in boxes_labels[boxi].items():
                new_labels[k] = [label for (label, _) in boxes[boxi]].index(k)
            boxes_labels[boxi] = new_labels
    elif '=' in instruction:
        [label, ctrl] = instruction.split('=')
        boxi = run_hash(label)
        if label not in boxes_labels[boxi].keys():
            boxes[boxi].append((label, int(ctrl)))
            boxes_labels[boxi][label] = len(boxes[boxi]) - 1
        else:
            boxes[boxi][boxes_labels[boxi][label]] = (label, int(ctrl))

    else:
        print('error 2')
        exit(1)
    # print([(idx, b) for (idx, b) in enumerate(boxes) if b != []])

total = 0
for (boxi, box) in enumerate(boxes):
    for (leni, lens) in enumerate(box):
        total += (boxi + 1) * (leni + 1) * lens[1]

print('second star', total)