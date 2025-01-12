import math
import time

blinks = 75
memo = [dict() for _ in range(blinks)]

def blink_n_times(stone: int, blink_i: int, blinks: int) -> int:
    if blink_i == blinks:
        return 1
    
    if stone in memo[blink_i]:
        return memo[blink_i][stone]
    
    next_blink_i = blink_i + 1

    if stone == 0:
        memo[blink_i][stone] = blink_n_times(1, next_blink_i, blinks)
    else:
        stone_n_len = int(math.log10(stone))+1
        
        if stone_n_len % 2 == 0:
            div = (10**(stone_n_len//2))
            memo[blink_i][stone] = blink_n_times(stone // div, next_blink_i, blinks) + blink_n_times(stone % div, next_blink_i, blinks)
        else:
            memo[blink_i][stone] = blink_n_times(stone * 2024, next_blink_i, blinks)
        
    return memo[blink_i][stone]

start = time.time()

stones = list(map(int, open('input.txt').read().strip().split(' ')))
result = 0
for stone in stones:
    result += blink_n_times(stone, 0, blinks)    
end = time.time()
    
print(f"{result}, took: {(end - start) * 1000.0}ms")