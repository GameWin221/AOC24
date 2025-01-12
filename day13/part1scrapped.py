machines = list(map(lambda m: m.splitlines(), open('input.txt').read().split('\n\n')))

result = 0  
for [atext, btext, ptext] in machines:
    (ax, ay) = map(lambda l: int(''.join(filter(lambda c: c.isdigit(), l))), atext.split(','))
    (bx, by) = map(lambda l: int(''.join(filter(lambda c: c.isdigit(), l))), btext.split(','))
    (px, py) = map(lambda l: int(''.join(filter(lambda c: c.isdigit(), l))), ptext.split(','))
    
    ca = 0
    cb = 0
    
    x = 0
    y = 0
    
    i = 0
    while x < px and y < py:
        dx = px - x
        dy = py - y
        
        if dx > dy:
            if ax > bx:
                x += ax
                y += ay
                ca += 1
            else:
                x += bx
                y += by
                cb += 1
        else:
            if ay > by:
                x += ax
                y += ay
                ca += 1
            else:
                x += bx
                y += by
                cb += 1
    
    if x == px and y == py:
        result += 3*ca + cb
        print(ca, cb)
    
        #print('yippe')

print(result)