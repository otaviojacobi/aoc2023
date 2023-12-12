with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

lines_without_galaxies = [i for (i,line) in enumerate(lines) if '#' not in line]
columns_without_galaxies = [j for j in range(len(lines[0])) if '#' not in [l[j] for l in lines]]

def expanded(galaxy, factor):
    gi, gj = galaxy[0], galaxy[1]
    gi = gi + (factor-1) * len([cl for cl in lines_without_galaxies if cl < gi])
    gj = gj + (factor-1) * len([ln for ln in columns_without_galaxies if ln < gj])
    return (gi, gj)

the_map = lines
factor = 2

galaxies = [(i,j) for i in range(len(the_map)) for j in range(len(the_map[i])) if the_map[i][j] == '#']
galaxies = [expanded(g, factor) for g in galaxies]

combinations = [[galaxies[i], galaxies[j]] for i in range(len(galaxies)) for j in range(i, len(galaxies)) if i != j]

first_star = 0
for comb in combinations:
    first_star += manhattan(*comb)

print('first star', first_star)

factor = 1000000

galaxies = [(i,j) for i in range(len(the_map)) for j in range(len(the_map[i])) if the_map[i][j] == '#']
galaxies = [expanded(g, factor) for g in galaxies]

combinations = [[galaxies[i], galaxies[j]] for i in range(len(galaxies)) for j in range(i, len(galaxies)) if i != j]

second_star = 0
for comb in combinations:
    second_star += manhattan(*comb)

print('second star', second_star)