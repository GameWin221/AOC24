import time

def find_guard(lines: list):
    for (y, line) in enumerate(lines):
        for (x, c) in enumerate(line):
            if c == '^':
                return (x, y)
            
    return (-1, -1)

def check(lines: list, width: int, height: int, s_px: int, s_py: int, s_dx: int, s_dy: int):
    move_map = [0] * (width*height)
    
    px = s_px
    py = s_py
    dx = s_dx
    dy = s_dy
    
    while True:
        nx = px + dx
        ny = py + dy
        
        # finish
        if nx < 0 or nx >= width or ny < 0 or ny >= height:
            return False
        
        # rotate
        if lines[ny][nx] == '#':
            old_dy = dy
            dy = dx
            dx = -old_dy
            continue
        
        # move onwards
        d_id = 0
        if dx == 0:
            if dy > 0:
                d_id = 1
            else:
                d_id = 2
        else:
            if dx > 0:
                d_id = 4
            else:
                d_id = 8
                   
        t_id = py * width + px
        if move_map[t_id] & d_id:
            return True
        
        move_map[t_id] |= d_id
        
        px = nx
        py = ny

def find_path(lines: list, width: int, height: int, s_px: int, s_py: int, s_dx: int, s_dy: int):
    move_set = set()
    
    px = s_px
    py = s_py
    dx = s_dx
    dy = s_dy
    
    while True:
        nx = px + dx
        ny = py + dy
        
        # finish
        if nx < 0 or nx >= width or ny < 0 or ny >= height:
            move_set.add((px, py))   
            return move_set
        
        # rotate
        if lines[ny][nx] == '#':
            old_dy = dy
            dy = dx
            dx = -old_dy
            continue
        
        # move onwards  
        if px != s_px or py != s_py:
            move_set.add((px, py))
        
        px = nx
        py = ny

start = time.time()

lines = list(map(lambda l: list(l.strip()), open('input.txt').readlines()))

height = len(lines)
width = len(lines[0])

(s_dx, s_dy) = (0, -1)
(s_px, s_py) = find_guard(lines)
lines[s_py][s_px] = '.'

result = 0
for (x, y) in find_path(lines, width, height, s_px, s_py, s_dx, s_dy):
    lines[y][x] = '#'
    
    if check(lines, width, height, s_px, s_py, s_dx, s_dy):
        result += 1
        
    lines[y][x] = '.'

end = time.time()
print(f"{result}, took: {(end-start) * 1000.0}ms")