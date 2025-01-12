import time

garden = list(map(lambda l: l.strip(), open('input.txt').readlines()))
height = len(garden)
width = len(garden[0])

visited = [[False for _ in range(width)] for _ in range(height)]
dir_table = [
    ( 0, -1),
    ( 1,  0),
    ( 0,  1),
    (-1,  0)
]

def count_edges(edges: set) -> int:
    edgestreak = 0
    start_edge = edges.pop()
    
    (x, y, d) = start_edge
    while True:
        (lx, ly) = dir_table[d-1 if d > 0 else 3]
        (fx, fy) = dir_table[d]
            
        ld = d-1 if d > 0 else 3
        rd = (d+1) % 4
        
        next_fl = (x+lx+fx, y+ly+fy, ld)
        next_f = (x, y, rd)
        next_r = (x+fx, y+fy, d)
        
        if next_fl in edges: #try to rotate left
            edges.remove(next_fl)
            (x, y, d) = next_fl
            edgestreak += 1
        elif next_f in edges: # try to rotate right
            edges.remove(next_f)
            (_, _, d) = next_f
            edgestreak += 1
        elif next_r in edges: # if can't rotate left and right try to step forward      
            edges.remove(next_r)
            (x, y, _) = next_r
        else: # if all previous check fail it means that it looped back
            if next_fl == start_edge or next_f == start_edge: # if ends in a turn add one edge
                edgestreak += 1
            break
    
    return edgestreak

def floodfill(sx: int, sy: int) -> tuple[int, int]:
    flood = [(sx, sy)]
    area = 0
    edges = set()

    while len(flood) > 0:
        nextflood = []
        for (fx, fy) in flood:
            if visited[fy][fx]:
                continue
            
            visited[fy][fx] = True
            area += 1

            ch = garden[fy][fx]
            
            # mark edges and then move along them looking for curves
            if fx > 0:
                if garden[fy][fx-1] == ch:
                    if not visited[fy][fx-1]:
                        nextflood.append((fx-1, fy))
                else:
                    edges.add((fx, fy, 0))
            else:
                edges.add((fx, fy, 0))
    
            if fx < width-1:
                if garden[fy][fx+1] == ch:
                    if not visited[fy][fx+1]:
                        nextflood.append((fx+1, fy))
                else:
                    edges.add((fx, fy, 2))
            else:
                edges.add((fx, fy, 2))
                
            if fy > 0:
                if garden[fy-1][fx] == ch:
                    if not visited[fy-1][fx]:
                        nextflood.append((fx, fy-1))
                else:
                    edges.add((fx, fy, 1))
            else:
                edges.add((fx, fy, 1))
                
            if fy < height-1:
                if garden[fy+1][fx] == ch:
                    if not visited[fy+1][fx]:
                        nextflood.append((fx, fy+1))
                else:
                    edges.add((fx, fy, 3))
            else:
                edges.add((fx, fy, 3))
                    
        flood = nextflood
        
    edgestreak = 0
    while len(edges) > 0:
        edgestreak += count_edges(edges)
        
    return (area, edgestreak)          

start = time.time()
result = 0
for y in range(height):
    for x in range(width):
        if visited[y][x]:
            continue
        
        (area, edgestreak) = floodfill(x, y)
        result += area * edgestreak
end = time.time()

print(f"{result}, took:{(end-start)*1000.0}ms")