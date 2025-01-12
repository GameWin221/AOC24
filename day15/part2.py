import time

start = time.time()
(warehouse_old, move_lines) = list(map(lambda x: list(map(lambda st: list(st), x.splitlines())), open('input.txt').read().split('\n\n')))

robot = [0, 0]
for (y, line) in enumerate(warehouse_old):
    if '@' in line:
        robot = [line.index('@')*2, y]
        break
    
warehouse_old[robot[1]][robot[0]//2] = '.'

moves = []
for line in move_lines:
    moves.extend(line)

width = len(warehouse_old[0])*2
height = len(warehouse_old)

warehouse = [['.']*width for _ in range(height)]
for (y, line) in enumerate(warehouse_old):
    for (x, c) in enumerate(line):
        if c == 'O':
            warehouse[y][2*x+0] = '['
            warehouse[y][2*x+1] = ']'
        else:
            warehouse[y][2*x+0] = c
            warehouse[y][2*x+1] = c
for line in warehouse:
    print(*line)


for move in moves:
    [rx, ry] = robot
    [dx, dy] = [0, 0]
    match move:
        case '<': [dx, dy] = [-1, 0]
        case '>': [dx, dy] = [1, 0]
        case '^': print('bruhhh')
        case 'v': print('bruhhh')    
            
    x = rx+dx
    y = ry+dy
    if warehouse[y][x] == '[' or warehouse[y][x] == ']':
        while warehouse[y][x] != '#':
            if warehouse[y][x] == '.':
                warehouse[ry+dy][rx+dx] = '.'
                warehouse[y][x] = 'O'
                robot[0] += dx
                robot[1] += dy
                break
            x += dx
            y += dy
            
    elif warehouse[y][x] != '#':
        robot[0] += dx     
        robot[1] += dy     
    
result = 0
for (y, line) in enumerate(warehouse):
    for (x, c) in enumerate(line):
        if c == 'O':
            result += 100*y + x

end = time.time()      

print(f"{result}, took: {(end-start) * 1000.0}ms")