import time

start = time.time()
lines = list(map(lambda l: l.strip(), open('input.txt').readlines()))
equations = list(map(lambda eq: (int(eq[0]), list(map(int, eq[1].strip().split(' ')))), list(map(lambda l: l.split(':'), lines))))

result = 0
for (target, numbers) in equations:
    operator_count = len(numbers)-1
    permutation_idx = 1 << operator_count # 2 ^ operator_count
    
    for perm in range(permutation_idx):
        tmp = numbers[0]
        for shift in range(0, operator_count):
            if perm & (1 << shift):
                tmp *= numbers[shift+1]
            else:
                tmp += numbers[shift+1]
                
        if tmp == target:
            result += target
            break
        
end = time.time()
        
print(f"{result}, took: {(end - start) * 1000.0}ms")