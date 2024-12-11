import itertools as it
import time

start = time.time()
lines = list(map(lambda l: l.strip(), open('input.txt').readlines()))
equations = list(map(lambda eq: (int(eq[0]), list(map(int, eq[1].strip().split(' ')))), list(map(lambda l: l.split(':'), lines))))

result = 0
for (target, numbers) in equations:
    operator_count = len(numbers) - 1
    
    for prod in it.product("*+|", repeat=operator_count):
        state = numbers[0]
        for (i, c) in enumerate(prod, 1):
            if c == '+':
                state += numbers[i]
            elif c == '*':
                state *= numbers[i]
            else:
                decimal_shift = 1
        
                if numbers[i] >= 100:
                    decimal_shift = 3
                elif numbers[i] >= 10:
                    decimal_shift = 2

                state = state * (10**decimal_shift) + numbers[i]
                
            if state > target:
                break
                
        if state == target:
            result += target
            break
                  
end = time.time()
        
print(f"{result}, took: {(end - start) * 1000.0}ms")

