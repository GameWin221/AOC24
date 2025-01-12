garden = list(map(lambda l: l.strip(), open('input.txt').readlines()))
height = len(garden)
width = len(garden[0])

visited = [[False for _ in range(width)] for _ in range(height)]

def floodfill(sx: int, sy: int) -> tuple[int, int]:
    flood = [(sx, sy)]
    area = 0
    perimeter = 0

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
                    perimeter += 1
            else:
                perimeter += 1
                
            if fx < width-1:
                if garden[fy][fx+1] == ch:
                    if not visited[fy][fx+1]:
                        nextflood.append((fx+1, fy))
                else:
                    perimeter += 1
            else:
                perimeter += 1
                
            if fy > 0:
                if garden[fy-1][fx] == ch:
                    if not visited[fy-1][fx]:
                        nextflood.append((fx, fy-1))
                else:
                    perimeter += 1
            else:
                perimeter += 1
                
            if fy < height-1:
                if garden[fy+1][fx] == ch:
                    if not visited[fy+1][fx]:
                        nextflood.append((fx, fy+1))
                else:
                    perimeter += 1
            else:
                perimeter += 1
                    
        flood = nextflood
    return (area, perimeter)          

result = 0
for y in range(height):
    for x in range(width):
        if visited[y][x]:
            continue
        
        (area, perimeter) = floodfill(x, y)
        result += area * perimeter
    
print(f"{result}")