import time

def find_free_range_index(file_ranges: list, size: int, end_id: int):
    for i in range(end_id):
        [a_start, a_size, a_id] = file_ranges[i]
        [b_start, b_size, a_id] = file_ranges[i+1]
        
        new_start = a_start + a_size
        
        if b_start - new_start >= size:
            return (i+1, new_start)
        
    return (-1, -1)

start = time.time()
data = list(map(int, open('input.txt').read().strip())) 

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

for id in reversed(range(len(file_ranges))):
    index = [range_id for [_, _, range_id] in file_ranges].index(id)
    r = file_ranges[index]
    
    (new_index, new_start) = find_free_range_index(file_ranges, r[1], index)
    if new_index != -1:
        del file_ranges[index]
        r[0] = new_start
        file_ranges.insert(new_index, r)


checksum = 0
for [range_start, range_size, range_id] in file_ranges:
    for offset in range(range_size):
        checksum += (range_start+offset) * range_id

end = time.time()

print(f"{checksum}, took: {(end-start) * 1000.0}ms")
