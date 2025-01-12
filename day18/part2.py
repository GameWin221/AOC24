from heapq import heappush, heappop
import time

width = 71
height = 71
fallen = 1024
start = (0, 0)
goal = (width-1, height-1)

time_start = time.time()
space = [[False] * width for _ in range(height)]
bytes = list(map(lambda x: list(map(int, x.strip().split(','))), open('input.txt').readlines()))

for i in range(fallen):
    [x, y] = bytes[i]
    space[y][x] = True

result = (-1, -1)
visited = [[False] * width for _ in range(height)]
for i in range(1024, len(bytes)):
    (nx, ny) = bytes[i]
    space[ny][nx] = True
    
    # Skip further pathfinding if not in the way of the previously checked tiles
    if not visited[ny][nx] and i > 1024:
        continue
    
    frontier = []
    heappush(frontier, (0, start))
    
    visited = [[False] * width for _ in range(height)]
    visited[start[1]][start[0]] = True

    while len(frontier) > 0:
        current = heappop(frontier)[1]
        
        if current == goal:
            break
        
        neighbors = []
        if current[0] >= 1:
            if space[current[1]][current[0]-1] == False:
                neighbors.append((current[0]-1, current[1]))
        if current[0] < width-1:
            if space[current[1]][current[0]+1] == False:
                neighbors.append((current[0]+1, current[1]))
        if current[1] >= 1:
            if space[current[1]-1][current[0]] == False:
                neighbors.append((current[0], current[1]-1))
        if current[1] < height-1:
            if space[current[1]+1][current[0]] == False:
                neighbors.append((current[0], current[1]+1))
            
        for next in neighbors:
            if not visited[next[1]][next[0]]:
                priority = abs(goal[0] - next[0]) + abs(goal[1] - next[1])
                
                heappush(frontier, (priority, next))
                
                visited[next[1]][next[0]] = True
            
    if not visited[goal[1]][goal[0]]:
        result = (nx, ny)
        break    
time_end = time.time()        

print(f"{result[0]},{result[1]} , took: {(time_end - time_start)*1000.0}ms")