import time
import keyboard
import math

robots = list(map(lambda l: list(map(lambda x: list(map(int, x[2:].split(','))), l.strip().split(' '))), open('input.txt').readlines()))

width = 101
height = 103
visited = set()

def calc_entropy(m: list):
    densities = []
    for y in range(height-2):
        for x in range(width-2):
            density = 0
            for yy in range(2):
                for xx in range(2):
                    if m[y+yy][x+xx] != ' ':
                        density += 1
                        
            densities.append(density*density*density)
    
    return sum(densities) / len(densities)

def calc_entropy_r(robots: list):
    densities = [[0]*int(math.ceil(width / 2)) for _ in range(int(math.ceil(height / 2)))]
    for [[px, py], [vx, vy]] in robots:
        densities[py//2][px//2] += 1
    
    s = 0
    for line in densities:
        for density in line:
            s += density*density*density
    
    return s / (len(densities) * len(densities[0]))
    
for sec in range(0, 1000000):
    for (i, [[px, py], [vx, vy]]) in enumerate(robots):
        (nx, ny) = (px + vx, py + vy)
        (wx, wy) = (nx % width, ny % height)
        robots[i][0] = [wx, wy]
      
    # some nice magic number cutoff
    entropy = calc_entropy_r(robots)
    if entropy < 0.6:
        continue
    
    m = [[' ']*width for _ in range(height)]
    for [[px, py], [vx, vy]] in robots:
        m[py][px] = '█'
    
    print(entropy)
    print(sec+1)
    for line in m:
        print(*line, sep=' ')
        
    if keyboard.is_pressed('S'):
        keyboard.wait('W')
            
    time.sleep(0.05)
