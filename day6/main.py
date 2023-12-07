with open('input.txt') as f:
    lines = f.readlines()

times = list(map(lambda x: int(x), lines[0].split(':')[-1].strip().split()))
distances = list(map(lambda x: int(x), lines[1].split(':')[-1].strip().split()))

result = 1
for (i, time) in enumerate(times):
    distance = distances[i]

    beats = []
    for test_time in range(1, time):
        travel_distance = (time - test_time) * test_time
        if travel_distance > distance:
            beats.append(test_time)
    result *= len(beats)

print(f'first star {result}')

distance = int(lines[1].split(':')[-1].replace(' ', ''))
time = int(lines[0].split(':')[-1].replace(' ', ''))

result = 1


for test_time in range(1, time):
    travel_distance = (time - test_time) * test_time
    if travel_distance > distance:
        beats_start = test_time
        break

print(f'second star {time - 2 * beats_start + 1}')