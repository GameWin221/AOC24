import time

dirtable = [
    [ 1, 0], # E
    [ 0,-1], # N
    [-1, 0], # W
    [ 0, 1]  # S
]

data = list(map(lambda l: l.strip(), open('input.txt').readlines()))

def traverse(dir: int, px: int, py: int, cost: int, visited: list[list[list[bool]]], dp: dict) -> int:
    if data[py][px] == 'E':
        return cost
    
    if (px, py, dir) in dp:
        if dp[(px, py, dir)] < cost:
            return cost + dp[(px, py, dir)]
        
    visited[py][px][dir] = True
    
    fd = dir
    ld = (dir + 1) % 4
    rd = (dir - 1) % 4
    
    [fx, fy] = [px + dirtable[fd][0], py + dirtable[fd][1]]
    [lx, ly] = [px + dirtable[ld][0], py + dirtable[ld][1]]
    [rx, ry] = [px + dirtable[rd][0], py + dirtable[rd][1]]
    
    result = 0xffffffffffffffff
    if data[fy][fx] != '#' and not visited[fy][fx][fd]:
        result = min(result, traverse(fd, fx, fy, cost+1, visited, dp))
    if data[ly][lx] != '#' and not visited[ly][lx][ld]:
        result = min(result, traverse(ld, lx, ly, cost+1001, visited, dp))
    if data[ry][rx] != '#' and not visited[ry][rx][rd]:
        result = min(result, traverse(rd, rx, ry, cost+1001, visited, dp))
      
    #if result != 0xffffffffffffffff:
        #print("bubu")
    dp[(px, py, dir)] = result - cost
        
    visited[py][px][dir] = False  

    return result

width = len(data[0])
height = len(data)

[sx, sy] = [0, 0]
[ex, ey] = [0, 0]
for (y, line) in enumerate(data):
    for (x, c) in enumerate(line):
        if c == 'S':
            [sx, sy] = [x, y]
        elif c == 'E':
            [ex, ey] = [x, y]

start = time.time()
print(traverse(0, sx, sy, 0, [[[False]*4 for _ in range(width)] for _ in range(height)], dict()))
end = time.time()
print((end-start) * 1000.0)