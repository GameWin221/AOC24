import time

start = time.time()
(warehouse, move_lines) = list(map(lambda x: list(map(lambda st: list(st), x.splitlines())), open('input.txt').read().split('\n\n')))
moves = []
for line in move_lines:
    moves.extend(line)

robot = [0, 0]
for (y, line) in enumerate(warehouse):
    if '@' in line:
        robot = [line.index('@'), y]
        break

warehouse[robot[1]][robot[0]] = '.'

width = len(warehouse[0])
height = len(warehouse)

for move in moves:
    [rx, ry] = robot
    [dx, dy] = [0, 0]
    match move:
        case '<': [dx, dy] = [-1, 0]
        case '>': [dx, dy] = [1, 0]
        case '^': [dx, dy] = [0, -1]
        case 'v': [dx, dy] = [0, 1]
        
    x = rx+dx
    y = ry+dy
    if warehouse[y][x] == 'O':
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