with open('input.txt') as f:
    [workflows, ratings] = f.read().split('\n\n')

workflows = workflows.split('\n')
ratings = ratings.split('\n')
workflows = {wf.split('{')[0]: wf.split('{')[-1].strip('}').split(',') for wf in workflows}

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
