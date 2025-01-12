data = list(map(lambda x: x.strip(), open('input.txt').readlines()))

height = len(data)
width = len(data[0])

start = None
end = None

for (y, line) in enumerate(data):
    if start is not None and end is not None:
        break
    
    for (x, c) in enumerate(line):
        if c == 'S':
            start = (x, y)
        elif c == 'E':
            end = (x, y)

costs = [[-1]*width for _ in range(height)]
path = dict()
traveller = start
cost = 0

while traveller != end:
    (x, y) = traveller
    costs[y][x] = cost
    path[traveller] = list()
    
    if data[y-1][x] == '#' and y-1 > 0:
        path[traveller].append((0, -1))
    if data[y+1][x] == '#' and y+1 < height-1:
        path[traveller].append((0,  1))
    if data[y][x-1] == '#' and x-1 > 0:
        path[traveller].append((-1, 0))
    if data[y][x+1] == '#' and x+1 < width-1:
        path[traveller].append(( 1, 0))
    
    if data[y-1][x] != '#' and (x, y-1) not in path:
        traveller = (x, y-1)
    elif data[y+1][x] != '#' and (x, y+1) not in path:
        traveller = (x, y+1)
    elif data[y][x+1] != '#' and (x+1, y) not in path:
        traveller = (x+1, y)
    elif data[y][x-1] != '#' and (x-1, y) not in path:
        traveller = (x-1, y)
        
    cost += 1
    
path[traveller] = list()
costs[traveller[1]][traveller[0]] = cost

result = 0
for ((x,y), dirs) in path.items():
    for (dx, dy) in dirs:
        (nx, ny) = (x + 2*dx, y + 2*dy)
        if data[ny][nx] != '#':
            if costs[ny][nx] - costs[y][x] - 2 >= 100:
                result += 1

print(result)
