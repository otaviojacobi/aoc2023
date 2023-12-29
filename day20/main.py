from typing import List, Tuple, Literal, Dict
from copy import deepcopy
from math import lcm

with open('input.txt') as f:
    lines = f.readlines()

def clean(elements: List[str]) -> List[str]:
    return [x.strip() for x in elements]

broadcaster = [clean(line.split('->')[-1].strip().split(',')) for line in lines if 'broadcaster' in line][0]
flipflops = {line.split('->')[0].strip().strip('%'): {'status': 'off', 'output': clean(line.split('->')[-1].strip().split(','))}  for line in lines if line.startswith('%')}
conjunctions = {line.split('->')[0].strip().strip('&'): {'memory': {}, 'output': clean(line.split('->')[-1].strip().split(','))}  for line in lines if line.startswith('&')}


for (k, ff) in flipflops.items():
    for output in ff['output']:
        if output in conjunctions.keys():
            conjunctions[output]['memory'][k] = 'off'

for (k, con) in flipflops.items():
    for output in con['output']:
        if output in conjunctions.keys():
            conjunctions[output]['memory'][k] = 'off'



# who feeds into rx?
conjunctions_into_rx = [c for (c, v) in conjunctions.items() if 'rx' in v['output']]
ff_into_rx = [ff for (ff, v) in flipflops.items() if 'rx' in v['output']]

assert len(conjunctions_into_rx) == 1
assert len(ff_into_rx) == 0
feeds_into = conjunctions_into_rx[0]
conjunctions_into_feeds = [c for (c, v) in conjunctions.items() if feeds_into in v['output']]
ff_into_feeds = [ff for (ff, v) in flipflops.items() if feeds_into in v['output']]

assert len(conjunctions_into_feeds) > 0
assert len(ff_into_feeds) == 0

conjunctions_into_feeds_values: Dict[str, None | int] = {c: None for c in conjunctions_into_feeds}

# we know have conjunctions_into_feeds which contains 4 conjunctions
# In order for a low pulse to be sent into rx, all 4 conjunctions need to be high
# The idea here is that every N button pushes each one of the conjunctions_into_feeds
# will be high, so the LCM should output when the first pulse is sent...

# print(broadcaster)
# print('flip', flipflops)
# print('conj', conjunctions) 


Node = Tuple[str, Literal['low'] | Literal['high'], str]

high_pulses = 0
low_pulses = 0

def run_all(signals):
    global high_pulses, low_pulses, i, conjunctions_into_feeds_values, done
    while len(signals) > 0:
        (origin, pulse, destination) = signals.pop(0)

        # gather some statistics about conjunctions_into_feeds
        if origin in conjunctions_into_feeds and pulse == 'high':
            if conjunctions_into_feeds_values[origin] == None:
                conjunctions_into_feeds_values[origin] = i

            if all(conjunctions_into_feeds_values.values()):
                done = True

        if destination in flipflops.keys(): # going into a flipflop
            if pulse == 'low':
                if flipflops[destination]['status'] == 'off':
                    flipflops[destination]['status'] = 'on'
                    for child in flipflops[destination]['output']:
                        high_pulses += 1
                        signals.append((destination, 'high', child))
                elif flipflops[destination]['status'] == 'on':
                    flipflops[destination]['status'] = 'off'
                    for child in flipflops[destination]['output']:
                        low_pulses += 1
                        signals.append((destination, 'low', child))

        elif destination in conjunctions.keys(): # going into a conjunction
            conjunctions[destination]['memory'][origin] = pulse
            new_signal = 'high'
            if list(set(dict(conjunctions[destination]['memory']).values())) == ['high']:
                new_signal = 'low'
            for child in conjunctions[destination]['output']:
                if new_signal == 'low':
                    low_pulses += 1
                elif new_signal == 'high':
                    high_pulses += 1
                signals.append((destination, new_signal, child))

    #else:
    #    print('deadend') # do nothing
signals: List[Node] = [('broadcaster', 'low', element) for element in broadcaster]
i = 0

done = False
while not done:
    low_pulses += len(signals) + 1
    run_all(deepcopy(signals))
    if i == 999:
        print('first star', low_pulses * high_pulses)

    i += 1

values: List[int] = [v+1 for v in conjunctions_into_feeds_values.values()]  # type: ignore
print('second star', lcm(*values))



