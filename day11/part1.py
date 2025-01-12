import time
import math

def blink_n_times(stone: int, blink_i: int, blinks: int) -> int:
    if blink_i == blinks:
        return 1
    
    next_blink_i = blink_i + 1

    if stone == 0:
        return blink_n_times(1, next_blink_i, blinks)
    else:
        stone_n_len = int(math.log10(stone))+1
        if stone_n_len % 2 == 0:
            div = (10**(stone_n_len//2))
            return blink_n_times(stone // div, next_blink_i, blinks) + blink_n_times(stone % div, next_blink_i, blinks)
        else:
            return blink_n_times(stone * 2024, next_blink_i, blinks)
    
start = time.time()

blinks = 25
stones = list(map(int, open('input.txt').read().strip().split(' ')))
result = 0
for stone in stones:
    result += blink_n_times(stone, 0, blinks)
    
end = time.time()
    
print(f"{result}, took: {(end - start) * 1000.0}ms")