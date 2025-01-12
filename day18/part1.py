from heapq import heappush, heappop
import time

width = 71
height = 71
fallen= 1024
start = (0, 0)
goal = (width-1, height-1)

time_start = time.time()
space = [[False] * width for _ in range(height)]
bytes = list(map(lambda x: list(map(int, x.strip().split(','))), open('input.txt').readlines()))

for i in range(fallen):
    [x, y] = bytes[i]
    space[y][x] = True

frontier = []
heappush(frontier, (0, (0, 0)))

came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0

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
        new_cost = cost_so_far[current] + 1
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
        
            priority = new_cost + abs(goal[0] - next[0]) + abs(goal[1] - next[1])
            
            heappush(frontier, (priority, next))
            came_from[next] = current
            
time_end = time.time()        

print(f"{cost_so_far[goal]}, took: {(time_end - time_start)*1000.0}ms")