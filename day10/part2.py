import time

topo = list(map(lambda l: list(map(lambda x: int(x) if x.isdigit() else -1, l.strip())), open('input.txt').readlines()))

start = time.time_ns()
starting_points = []
width = len(topo[0])
height = len(topo)
for (y, line) in enumerate(topo):
    for (x, n) in enumerate(line):
        if n == 0:
            starting_points.append((x, y))
            
result = 0
for starting_point in starting_points:
    ending_points_reached = list()
    travellers = [starting_point]
    
    while len(travellers) > 0:
        next_travellers = list()
        for (tx, ty) in travellers:
            curr = topo[ty][tx]
            if curr == 9:
                ending_points_reached.append((tx, ty))
                continue
            
            if tx > 0:
                if topo[ty][tx-1] - curr == 1:
                    next_travellers.append((tx-1, ty))
            if tx < width-1:
                if topo[ty][tx+1] - curr == 1:
                    next_travellers.append((tx+1, ty))
            
            if ty > 0:
                if topo[ty-1][tx] - curr == 1:
                    next_travellers.append((tx, ty-1))
            if ty < height-1:
                if topo[ty+1][tx] - curr == 1:
                    next_travellers.append((tx, ty+1))
            
        travellers = next_travellers
        
    result += len(ending_points_reached)
end = time.time_ns()

print(f"{result}, took: {(end-start) / 1000.0}us")