robots = list(map(lambda l: list(map(lambda x: list(map(int, x[2:].split(','))), l.strip().split(' '))), open('input.txt').readlines()))

width = 101
height = 103
seconds = 100
[qtl, qtr, qbl, qbr] = [0, 0, 0, 0]
for [[px, py], [vx, vy]] in robots:
    (nx, ny) = (px + vx*seconds, py + vy*seconds)
    (wx, wy) = (nx % width, ny % height)
    
    if wx > width // 2:
        if wy > height // 2:
            qbr += 1
        elif wy < height // 2:
            qtr += 1
    elif wx < width // 2:
        if wy > height // 2:
            qbl += 1
        elif wy < height // 2:
            qtl += 1
            
        
print(qtl*qtr*qbl*qbr)
