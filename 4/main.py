
INPUT = 'input.txt'

def check_adjacent8(grid, coords):
    new_coords = [
        [coords[0]-1, coords[1]-1],
        [coords[0]-1, coords[1]],
        [coords[0]-1, coords[1]+1],
        [coords[0], coords[1]-1],
        [coords[0], coords[1]+1],
        [coords[0]+1, coords[1]-1],
        [coords[0]+1, coords[1]],
        [coords[0]+1, coords[1]+1],
    ]
    values = [grid[x[0]][x[1]] for x in new_coords]
    values = "".join(values).replace('.', '')
    return len(values)<4

grid = []
with open(INPUT, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = '.'+line.strip()+'.'
        grid.append([x for x in line.strip()])
    grid_size = len(line)
grid.append(['.']*grid_size)
grid.insert(0, ['.']*grid_size)

c = 0
c_before = 0

while True:
    for x in range(1, grid_size-1):
        new_line = ""
        for y in range(1, grid_size-1):
            new_line += grid[x][y]
            if(grid[x][y] == "@"):
                smth = check_adjacent8(grid, [x, y])
                if smth:
                    grid[x][y] = '.'
                    c += 1
    if c_before == c:
        break
    else:
        c_before = c
print(c)