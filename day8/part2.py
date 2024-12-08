import time

width = 0
height = 0

start = time.time()

allAntennas = dict()
for (y, line) in enumerate(open('input.txt').readlines()):
    for (x, c) in enumerate(line.strip()):
        if c == '.':
            continue
        
        if c in allAntennas:
            allAntennas[c].append((x, y))
        else:
            allAntennas[c] = [(x, y)]
            
    width = len(line)    
    height = y+1

antinodes = set()
for (frequency, antennas) in allAntennas.items():
    for i in range(0, len(antennas)):
        for j in range(i+1, len(antennas)):
            (ax, ay) = antennas[i]
            (bx, by) = antennas[j]
            (dx, dy) = (bx-ax, by-ay)
            
            (anti_x1, anti_y1) = (ax, ay)
            (anti_x2, anti_y2) = (bx, by)
            
            while anti_x1 >= 0 and anti_x1 < width and anti_y1 >= 0 and anti_y1 < height:
                antinodes.add((anti_x1, anti_y1))
                anti_x1 += dx
                anti_y1 += dy
                
            while anti_x2 >= 0 and anti_x2 < width and anti_y2 >= 0 and anti_y2 < height:
                antinodes.add((anti_x2, anti_y2))
                anti_x2 -= dx
                anti_y2 -= dy
         
end = time.time()     
           
print(f"{len(antinodes)}, took: {(end-start) * 1000.0}ms")