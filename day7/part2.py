
import time
import math

def solve(state: int, nums: list, op_count: int, i: int, type: int, target: int):
    if type == 0:
        state += nums[i]
    elif type == 1:
        state *= nums[i]
    elif type == 2:
        decimal_shift = int(math.log10(nums[i]))+1
        state = state * (10**decimal_shift) + nums[i]
        
    if i == op_count:
        if state == target:
            return target
        else:
            return 0
    else:
        if state > target:
            return 0
        else:
            return max(solve(state, nums, op_count, i+1, 0, target), solve(state, nums, op_count, i+1, 1, target), solve(state, nums, op_count, i+1, 2, target))

start = time.time()
lines = list(map(lambda l: l.strip(), open('input.txt').readlines()))
equations = list(map(lambda eq: (int(eq[0]), list(map(int, eq[1].strip().split(' ')))), list(map(lambda l: l.split(':'), lines))))

result = 0
for (target, numbers) in equations:
    result += solve(0, numbers, len(numbers) - 1, 0, 0, target)
        
end = time.time()
        
print(f"{result}, took: {(end - start) * 1000.0}ms")