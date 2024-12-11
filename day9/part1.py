import time


data = list(map(int, open('input.txt').read().strip()))
filesystem = list()

start = time.time() 

total_blocks = 0
file_id = 0
for i in range(len(data)):
    is_file = (i % 2 == 0)
    
    n = data[i]
    
    if is_file:
        filesystem += [file_id]*n
        total_blocks += n
    else:
        filesystem += [-1]*n
    
    if is_file:
        file_id += 1

checksum = 0
last_n_id = len(filesystem)-1
for i in range(total_blocks):
    if filesystem[i] == -1:
        while filesystem[last_n_id] == -1:
            last_n_id -= 1
            
        checksum += i * filesystem[last_n_id]
        last_n_id -= 1
    else:
        checksum += i * filesystem[i]

end = time.time()

print(f"{checksum}, took: {(end-start) * 1000.0}ms")
