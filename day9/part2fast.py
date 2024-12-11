import time

def find_free_range(free_ranges: list, size: int, end: int):
    for (index, [range_start, range_size]) in enumerate(free_ranges):
        if range_start >= end:
            break
        
        if range_size >= size:  
            return index
        
    return -1

start = time.time() 

data = list(map(int, open('message.txt').read().strip()))

free_ranges = list()
file_ranges = list()

file_id = 0
block_index = 0
for i in range(len(data)):
    region_is_file = (i % 2 == 0)
    region_size = data[i]
    
    if region_size == 0:
        continue
    
    if region_is_file:
        file_ranges.append([block_index, region_size, file_id])
        file_id += 1
    else:
        free_ranges.append([block_index, region_size])
        
    block_index += region_size

checksum = 0

for id in reversed(range(len(file_ranges))):
    [file_range_start, file_range_size, file_range_id] = file_ranges[id]

    free_range_index = find_free_range(free_ranges, file_range_size, file_range_start)
    if free_range_index != -1:
        [free_range_start, free_range_size] = free_ranges[free_range_index]
        
        checksum += (2 * free_range_start + file_range_size - 1) * file_range_size * id // 2 # sum first n elements of an arithmetic sequence 
            
        if file_range_size >= free_range_size:
            del free_ranges[free_range_index]
        else:
            free_ranges[free_range_index] = [free_range_start + file_range_size, free_range_size - file_range_size]
    else:
        checksum += (2 * file_range_start + file_range_size - 1) * file_range_size * file_range_id // 2 # sum first n elements of an arithmetic sequence 
        
end = time.time()

print(f"{checksum}, took: {(end-start) * 1000.0}ms")
