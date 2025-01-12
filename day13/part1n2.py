def solve(ax: int, ay: int, bx: int, by: int, px: int, py: int) -> tuple[int, int]:
    Wm = ax*by-ay*bx
    if Wm == 0:
        return (0, 0)
    
    Wa = px*by-py*bx
    Wb = ax*py-ay*px
    if Wa % Wm != 0 or Wb % Wm != 0:
        return (0, 0)
    
    return (Wa // Wm, Wb // Wm)

machines = list(map(lambda m: m.splitlines(), open('input.txt').read().split('\n\n')))
result1 = 0  
result2 = 0  

for [atext, btext, ptext] in machines:
    (ax, ay) = map(lambda l: int(''.join(filter(lambda c: c.isdigit(), l))), atext.split(','))
    (bx, by) = map(lambda l: int(''.join(filter(lambda c: c.isdigit(), l))), btext.split(','))
    (px, py) = map(lambda l: int(''.join(filter(lambda c: c.isdigit(), l))), ptext.split(','))

    (a1, b1) = solve(ax, ay, bx, by, px, py)
    (a2, b2) = solve(ax, ay, bx, by, px+10000000000000, py+10000000000000)
    
    result1 += 3*a1 + b1
    result2 += 3*a2 + b2
    
print(result1, result2)