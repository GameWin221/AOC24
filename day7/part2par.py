
import time
import multiprocessing as mp

def solve(state: int, nums: list, op_count: int, i: int, type: int, target: int):
    if type == 0:
        state += nums[i]
    elif type == 1:
        state *= nums[i]
    elif type == 2:
        decimal_shift = 1
        
        if nums[i] >= 100:
            decimal_shift = 3
        elif nums[i] >= 10:
            decimal_shift = 2
            
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

def process(pair: tuple[int, list]):
    return solve(0, pair[1], len(pair[1]) - 1, 0, 0, pair[0])

if __name__ == '__main__':
    start = time.time()
    lines = list(map(lambda l: l.strip(), open('input.txt').readlines()))
    equations = list(map(lambda eq: (int(eq[0]), list(map(int, eq[1].strip().split(' ')))), list(map(lambda l: l.split(':'), lines))))
    
    result = 0
    with mp.Pool(mp.cpu_count()-4) as p:
        result = sum(p.map(process, equations))

    end = time.time()

    print(f"{result}, took: {(end - start) * 1000.0}ms")